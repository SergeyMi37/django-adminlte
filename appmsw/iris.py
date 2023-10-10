import irisnative
import os
from django.conf import settings
from core.settings import DEBUG
import json
from urllib.parse import urlparse
'''
# http://grep.cs.msu.ru/python3.8_RU/digitology.tech/docs/python_3/library/urllib.parse.html

>>> from urllib.parse import urlparse
>>> o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
>>> o   # doctest: +NORMALIZE_WHITESPACE
ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
            params='', query='', fragment='')
>>> o.scheme
'http'
'''
_url = os.getenv("APPMSW_IRIS_URL")

#from telegram import Bot
#from core.settings import TELEGRAM_TOKEN
#bot_info = Bot(TELEGRAM_TOKEN).get_me()
#bot_link = f"https://t.me/{bot_info['username']}"

def classMethod(request,_class,_method, _arg="",iris_url=""):
    o = urlparse(iris_url)
    try:
        _args={
            "basedir":str(settings.BASE_DIR),
            "irishost":o.hostname,
            "irisport":str(o.port),
            "irisnamespace":str(o.path.split("/")[1]),
            "arg":_arg,
          #  "bot_link":bot_link,
        }
        if request:
            _args["user"]= str(request.user)
            _args["authenticated"]=request.user.is_authenticated
            _args["superuser"]=request.user.is_superuser
            _args["absoluteuri"]=request.build_absolute_uri()
        #print('iris-url=====',str(o.path.split("/")[1]))        
        if not o.hostname:
            return f'{{"status":"Error Iris Host is empty {iris_url}"}}'
        else:
            connection = irisnative.createConnection( o.hostname, int(o.port), str(o.path.split("/")[1]), o.username, o.password)
            appiris = irisnative.createIris(connection)
            _val = str(appiris.classMethodValue(_class, _method, json.dumps(_args)))
    except Exception as err:
        print("---err-classMethod--------",err)
        _val = f'{{"status":"Error FAIL Iris connection {err} for {iris_url}"}}'
    #print('iris-val=====',_val, str(o.path.split("/")[1]))        
    return _val

def classMethodFooter(request,url=_url):
    try:
        _val=classMethod(request,"apptools.core.django", "GetFooter", "",iris_url=url)
        #if DEBUG:print('---return-classMethod Footer-----',_val)
    except Exception as err:
        if DEBUG:print("---err-footer--------",err)
        _val = f"{{ 'status':'Error Iris Footer :{err}' }}"
    return _val

def classMethodPortal(request,mp_list="",url=_url):
    try:
        _val=classMethod(request,"apptools.core.django", "GetPortal",mp_list,iris_url=url)
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
>>> nodeVal = str(appiris.classMethodValue("apptools.core.django", "TS", ""))
>>> print(nodeVal)
>>>
    '''