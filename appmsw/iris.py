import irisnative
import os
from django.conf import settings
from dtb.settings import DEBUG
import json
# For Docker
#ISC_Host=iris
#ISC_Port=1972
#ISC_Username=_system
#ISC_Password=SYS
#ISC_Namespace=USER
ISC_Host = os.getenv("ISC_Host")
ISC_Port = os.getenv("ISC_Port")
ISC_Username = os.getenv("ISC_Username")
ISC_Password = os.getenv("ISC_Password")
ISC_Namespace = os.getenv("ISC_Namespace")

from telegram import Bot
from dtb.settings import TELEGRAM_TOKEN
bot_info = Bot(TELEGRAM_TOKEN).get_me()
bot_link = f"https://t.me/{bot_info['username']}"

def classMethod(request,_class,_method, _arg=""):
    try:
        _args={
            "basedir":str(settings.BASE_DIR),
            "irishost":ISC_Host,
            "irisport":str(ISC_Port),
            "arg":_arg,
            "bot_link":bot_link,
        }
        if request:
            _args["user"]= str(request.user)
            _args["authenticated"]=request.user.is_authenticated
            _args["superuser"]=request.user.is_superuser
            _args["absoluteuri"]=request.build_absolute_uri()
        
        if ISC_Host=="":
            return f'{{"status":"Error Iris Host is empty"}}'
        else:
            connection = irisnative.createConnection(ISC_Host, int(ISC_Port), ISC_Namespace, ISC_Username, ISC_Password)
            appiris = irisnative.createIris(connection)
            _val = str(appiris.classMethodValue(_class, _method, json.dumps(_args)))
    except Exception as err:
        print("---err-classMethod--------",err)
        _val = f'{{"status":"Error FAIL Iris connection {err}"}}'
    return _val

def classMethodFooter(request):
    try:
        _val=classMethod(request,"apptools.core.telebot", "GetFooter", "")
        #if DEBUG:print('---return-classMethod Footer-----',_val)
    except Exception as err:
        if DEBUG:print("---err-footer--------",err)
        _val = f"{{ 'status':'Error Iris Footer :{err}' }}"
    return _val

def classMethodPortal(request,mp_list=""):
    try:
        _val=classMethod(request,"apptools.core.telebot", "GetPortal",mp_list)
        if DEBUG:print('---return-classMethod Portal-----',_val)
    except Exception as err:
        if DEBUG:print("---err-portal--------",err)
        _val = f"{{ 'status':'Error Iris Portal :{err}' }}"
    return _val
    
    '''
Python 3.8.10 (default, Jun 23 2021, 15:19:53)
>>>
>>> import irisnative
>>> connection = irisnative.createConnection("a3011d1fe174", int(1972), "USER", "superuser", "SYS")
>>> appiris = irisnative.createIris(connection)
>>> nodeVal = str(appiris.classMethodValue("apptools.core.telebot", "TS", ""))
>>> print(nodeVal)
>>>
    '''