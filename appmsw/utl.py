# Utilites
import os
import json
from appmsw.iris import classMethod, classMethodFooter, classMethodPortal

def get_env_appmsw(request,name=""):
    _={}
    _["logotitle"]=os.environ.get("APPMSW_LOGO_TITLE")
    _["logofooter"]=os.environ.get("APPMSW_LOGO_FOOTER")
    _img=str(os.environ.get("APPMSW_LOGO_IMG"))
    if _img !="None":
        _["logoimg"]=_img
    if name=="": 
        return _
    elif name=="title":
        return _.get("logotitle","undef")
    elif name=="footer":
        return _.get("logofooter","undef")
    elif name=="img":
        return _.get("logoimg","undef")
    
    _url=os.environ.get("APPMSW_IRIS_URL")
    if _url:
        _i = json.loads(classMethodFooter(request,url=_url))
        #print(_i)
        try:
            if _i['status'] !='ok':
                return _i['status']
            if name=="iris_footer":
                return _i
            elif name=="iris_instance":
                return _i['instance'].split("*")[1]
            elif name=="iris_host":
                return _i['host']
        except Exception as err:
            print("---err-classMethod--------",err)
            _i = f'{{"status":"Error get_env_appmsw {err} for :{name}"}}'
            return _i
    return ""