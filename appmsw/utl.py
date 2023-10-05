# Utilites
import os
import json
from appmsw.iris import classMethod, classMethodFooter, classMethodPortal

def get_env_appmsw(name=""):
    _={}
    _["logotitle"]=os.environ.get("APPMSW_LOGO_TITLE")
    _["logofooter"]=os.environ.get("APPMSW_LOGO_FOOTER")
    _img=str(os.environ.get("APPMSW_LOGO_IMG"))
    #print('img===',_img)
    if _img !="None":
        _["logoimg"]=_img
    _url=os.environ.get("APPMSW_IRIS_URL")
    if _url:
        _["iris_footer"]= json.loads(classMethodFooter(""))
    return _