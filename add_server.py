#!/usr/bin/python

import collections
import json
import requests
import sys

try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except:
    from urllib3.exceptions import InsecureRequestWarning
    import urllib3
baseurl = "https://<EMSERVER>:8446/automation-api"   #8446 in 19.200 onwards 
username = ''
password = ''

def tokengen():
   global token
   global data
   loginurl = baseurl + '/session/login'  # The login ur
   body = json.loads('{ "password": "' + password + '", "username": "' + username + '"}')

   r = requests.post(loginurl, json=body, verify=False)
   loginresponse=json.loads(r.text)

   if 'token' in loginresponse:
       token = json.loads(r.text)['token']
   if 'error' in loginresponse:
      print((json.dumps(loginresponse)['errors']))
   print(token)
   data=json.loads('{"Authorization": "Bearer '+token+'"}')

def define_server():
    global data
    data = json.loads('{"Authorization": "Bearer ' + token + '"}')  # the jobs statues call should have the token in the header as JSON
    define_server_url = baseurl + '/config/server'
    body=json.loads('{"ctm": "<CTM-DC>" , "host": "<EMSERVER>", "id": "ABC", "port": 2369 }')
    r2 = requests.post(define_server_url, headers=data , json=body , verify=False)
    print((r2.text))


def logouturl1():
   logouturl = baseurl + '/session/logout'
   #body = json.loads('{ "token":"' + token + '", "username": "' + username + '"}')  - iold method not work now
   #r3 = requests.post( logouturl , data=body, verify=False)
   r3 = requests.post(logouturl , headers=data , verify=False)
   print((r3.text))


tokengen()
define_server()
logouturl1()
