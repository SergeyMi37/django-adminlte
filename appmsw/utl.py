# Utilites
import os
import json

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

def get_env_appmsw(name=""):
    _={}
    _["logotitle"]=os.environ.get("APPMSW_LOGO_TITLE")
    _["logofooter"]=os.environ.get("APPMSW_LOGO_FOOTER")
    return _