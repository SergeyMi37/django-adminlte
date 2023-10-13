# -*- coding: utf-8 -*-
#pip install pandas
import requests
import json
from openpyxl import Workbook
import datetime
#print(datetime.datetime.today())

base_url="https://openexchange.intersystems.com"
fdir="" #"d:\\mosvodokanal\\!\\_tarif\\"
_debug="" # zpm
suff="test"
fname=str(datetime.datetime.today().strftime("%Y-%m-%d_%H.%M"))

# Updates 
#_url=base_url+"/mpapi/packages/find_pagination?term=&cats=&ww=&ind=&sorting=d.desc&zpm=1&fresh=6&pageSize=300"
#_url=base_url+"/mpapi/packages/find_pagination?term=&cats=&ww=&ind=&sorting=d.desc&fresh=6&pageSize=300"
_suburl=base_url+"/mpapi/packages/get/"
# sort name zpm
_url=base_url+"/mpapi/packages/find_pagination?term=&cats=&ww=&ind=&sorting=t.asc&zpm=1&pageSize=300"
headers = {'Accept': 'application/json;odata=verbose'}
responce = requests.get(_url,verify=False,headers=headers)
response_list=responce.json()
#print(response_list["items"])

url_pm="https://pm.community.intersystems.com/packages/-/all"
responce_pm = requests.get(url_pm,verify=False,headers=headers)
response_pm_list=responce_pm.json()
#print(response_pm_list)
zpm={}
zpm_name={}
for iname in response_pm_list:
    _z_r=iname["repository"]
    _z_n=iname["name"]
    #if _z_n=="zpm":
    #    _z_r="https://github.com/intersystems-community/zpm/"
    print(_z_n)
    print(_z_r)
    zpm[_z_r]={"name":_z_n, "repository":_z_r}   #iname #{"name":iname["name"],"versions":iname["versions"],"description":iname["description"]}
    zpm_name[_z_n]={"repository":_z_r, "name":_z_n} #iname #{"repository":iname["repository"],"versions":iname["versions"],"description":iname["description"]}

_out=[["Перечень проектов из OEX"],["Name","DownloadsCount", "Objectscriptquality","LastApprovalDate","FirstApprovalDate","Stars","Rating","Rewards","UserName","ZPM","Repo","Ver","ZPM-Repo", "Description"]]
_out.append(["OEX","-------------",_url])

for iname in response_list["items"]:
    _name=iname["Name"].lower()
    #print(_name)
    _ver=""
    _repo=""
    _LastApprovalDate=""
    _FirstApprovalDate=""
    _Rewards=""
    _user=""
    _zpm=""
    _zpmRepo=""
    _name_wsp=iname["nameWithoutSpaces"]
    if _debug:
        _name_wsp=_debug
        _name=_debug
    response_one = requests.get(_suburl+_name_wsp,verify=False,headers=headers)
    if response_one:
        response_one_list=response_one.json()
        #print("------------------",response_one_list)
        _repo=response_one_list["ProductURL"]
        _ver=response_one_list["Version"]
        _LastApprovalDate=response_one_list["ApprovalDate"].split(" ")[0]
        _Rewards=len(response_one_list["Rewards"])
        _user=response_one_list["UserID"]["firstName"]

        for i,_ve in reversed(list(enumerate(response_one_list["Versions"]))):
            if _ve["approvalDate"]:
                #print(i,_ve)
                _FirstApprovalDate=_ve["approvalDate"].split(" ")[0]
                break
    print("===",_name)
    _val=zpm.get(str(_repo+"/"))
    if _val:
        _zpm=str(_val["name"])
        _zpmRepo=str(_val["repository"])
    if _zpm=='': #Если не нашли сопоставление по Репо, то поищем по имени в нижнем регистре
        _val=zpm_name.get(_name)
        if _val:
            _zpm=_val["name"]
            _zpmRepo=str(_val["repository"])
    _out.append([_name_wsp, iname["DownloadsCount"], iname["Objectscriptquality"],_LastApprovalDate,_FirstApprovalDate,iname["Stars"],iname["Rating"],_Rewards,_user,_zpm,_repo,_ver, _zpmRepo,iname["Description"]])
 
    if _debug:
        break
#print(_out)
print("Всего "+_debug+" ",response_list["total"])

wb = Workbook() # creates a workbook object.
ws = wb.active # creates a worksheet object.

for row in _out:
    #print(row)
    ws.append(row) # adds values to cells, each list is a new row.

ws.column_dimensions.__getitem__("A").width = "30"
ws.column_dimensions.__getitem__("D").width = "15"
ws.column_dimensions.__getitem__("E").width = "15"
ws.column_dimensions.__getitem__("I").width = "30"
ws.column_dimensions.__getitem__("J").width = "30"
ws.column_dimensions.__getitem__("K").width = "40"
ws.freeze_panes="B3"
wb.save(fdir+"oex-zpm"+fname+".xlsx") # save to excel file.
