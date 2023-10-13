# Utilites
import os
import json
from appmsw.iris import classMethod, classMethodFooter, classMethodPortal
from appmsw.models import Param
from functools import lru_cache
from django.core import serializers

def get_sidemenu(context):
    _js={}
    _pn=os.environ.get("APPMSW_PARAM_NANE")
    #print("---",_pn)
    if _pn:
         _js = get_param(par_name=_pn,par_name_return="json")
    #print("===",type(_js),_js.get("SideMenu",""))
    return _js.get("SideMenu","")

def get_param(par_name="",par_name_return="Desc",json_key=""):
    #params = Param.objects.all()
    #param = Param.objects.get(pk=id)
    param = Param.objects.filter(name=par_name)
    _e={}
    for e in param:
        #print(type(e))
        _e=getattr(e, par_name_return)
        if par_name_return=="json":
            if json_key:
                try:
                    _j=json.loads(_e)
                    _e=_j.get(json_key,{})
                    return _e
                except:
                    return {}
            else:
                try:
                    return json.loads(_e)
                except:
                    return {}
    #print(param)
    return _e

@lru_cache()
def get_env_appmsw(request,name="",fieldname="",name_return="",jsonkey=""):
    if name.find("APPMSW_")>-1:
        return str(os.environ.get(name))
    _e={}
    _e["APPMSW_PARAM_NANE"]=os.environ.get("APPMSW_PARAM_NANE")
    _e["APPMSW_LOGO_TITLE"]=os.environ.get("APPMSW_LOGO_TITLE")
    _e["APPMSW_LOGO_FOOTER"]=os.environ.get("APPMSW_LOGO_FOOTER")
    _e["APPMSW_LOGO_IMG"]=str(os.environ.get("APPMSW_LOGO_IMG"))
    _e["APPMSW_IRIS_URL"]=os.environ.get("APPMSW_IRIS_URL")
 
    # Variables from the Parameter object will override those explicitly specified in the .env
    if  _e["APPMSW_PARAM_NANE"]: 
        for it in ["APPMSW_LOGO_IMG","APPMSW_LOGO_TITLE","APPMSW_LOGO_FOOTER","APPMSW_IRIS_URL"]:
            _it = get_param(par_name=_e["APPMSW_PARAM_NANE"],par_name_return="json",json_key=it)
            #print(it,_it)
            if _it:  _e[it]=_it
 
    if name=="": 
        return _e
    elif name=="param_name_all":
        param = Param.objects.filter(name=_e["APPMSW_PARAM_NANE"])
        data = serializers.serialize("json", param)
        return data
    elif name=="param":
        if fieldname:
            return get_param(par_name=fieldname,par_name_return=name_return,json_key=jsonkey)
    elif name=="title":
        return _e.get("APPMSW_LOGO_TITLE","undef")
    elif name=="footer":
        return _e.get("APPMSW_LOGO_FOOTER","undef")
    elif name=="img" and _e["APPMSW_LOGO_IMG"]!="None":
        return _e.get("APPMSW_LOGO_IMG","undef")

    if _e["APPMSW_IRIS_URL"]:
        _i = json.loads(classMethodFooter(request,url=_e["APPMSW_IRIS_URL"]))
        #print("===",_["APPMSW_IRIS_URL"],_i)
        try:
            if _i['status'] !='ok':
                return _i['status']
            if name=="iris_footer":
                #print(_i['apps'])
                _irf=f"<span title='Iris Instance'>{_i['instance'].split('*')[1]}</span> <span title='Iris Host'>{_i['host']}</span>"
                for enum in _i['apps']:
                    _irf+=f' | <a target="_blank" href="{ enum["url"] }">{ enum["name"] }</a>'
                return _irf
            elif name=="iris_instance":
                return _i['instance'].split("*")[1]
            elif name=="iris_host":
                return _i['host']
            elif name=="iris":
                return _i
        except Exception as err:
            print("---err-classMethod--------",err)
            _i = f'{{"status":"Error get_env_appmsw {err} for :{name}"}}'
            return _i
    return ""