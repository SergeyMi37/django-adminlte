# -*- coding: utf-8 -*-
#pip install pandas
import requests
import json
from openpyxl import Workbook
import datetime
#print(datetime.datetime.today())

base_url="https://openexchange.intersystems.com"
fdir="d:\\mosvodokanal\\!\\_tarif\\"
suff="test"
fname=str(datetime.datetime.today().strftime("%Y-%m-%d_%H.%M"))

# Updates 
_url=base_url+"/mpapi/packages/find_pagination?term=&cats=&ww=&ind=&sorting=d.desc&zpm=1&fresh=6&pageSize=300"
_url=base_url+"/mpapi/packages/find_pagination?term=&cats=&ww=&ind=&sorting=d.desc&fresh=6&pageSize=300"
# sort name zpm
_url=base_url+"/mpapi/packages/find_pagination?term=&cats=&ww=&ind=&sorting=t.asc&zpm=1&pageSize=300"

url_pm="https://pm.community.intersystems.com/packages/-/all"

headers = {'Accept': 'application/json;odata=verbose'}

responce_pm = requests.get(url_pm,verify=False,headers=headers)
response_pm_list=responce_pm.json()
#print(response_pm_list)
zpm={}
for iname in response_pm_list:
    print(iname["name"])
    zpm[iname["name"]]={"repository":iname["repository"],"versions":iname["versions"],"description":iname["description"]}
    #_out.append([iname["nameWithoutSpaces"], iname["DownloadsCount"], iname["Objectscriptquality"],iname["ImageURL"], iname["Description"]])

#print(zpm)

responce = requests.get(_url,verify=False,headers=headers)

response_list=responce.json()
#print(response_list["items"])
_out=[["Перечень проектов из OEX и PM ресерсов"],["Name","Source","DownloadsCount", "Objectscriptquality","Repo","Ver", "Description"]]
_out.append(["","OEX",_url])
zpm_oex={}
for iname in response_list["items"]:
    _name=iname["Name"].lower()
    #print(_name)
    _ver=""
    _repo=""
    _val=zpm.get(_name)
    if _val:
        _ver=str(_val["versions"])
        _repo=_val["repository"]
        #print(_ver,_repo)
        zpm_oex[_name]=1
        zpm_oex[iname["Name"]]=1
        zpm_oex[iname["nameWithoutSpaces"]]=1
    
    _out.append([_name,"OEX", iname["DownloadsCount"], iname["Objectscriptquality"],_repo,_ver, iname["Description"]])
_out.append(["","PM",url_pm])

for key, val in zpm.items():
    if not zpm_oex.get(key):
        #print(key,val)
        _out.append([key, "PM","", "",val["repository"],str(val["versions"]), val["description"]])

#print(_out)
print("Всего ",response_list["total"])

wb = Workbook() # creates a workbook object.
ws = wb.active # creates a worksheet object.

for row in _out:
    #print(row)
    ws.append(row) # adds values to cells, each list is a new row.

ws.column_dimensions.__getitem__("A").width = "30"
ws.freeze_panes="B3"
wb.save(fdir+"oex-zpm"+fname+".xlsx") # save to excel file.
