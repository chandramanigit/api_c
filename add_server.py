#!/usr/bin/python

import collections
import json
import requests
import argparse
import sys
from getpass import getpass

try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
except:
    from urllib3.exceptions import InsecureRequestWarning
    import urllib3
baseurl = "https://ctmtest.mylab.com:8443/automation-api"
username = 'emuser'
password = 'emuser'

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
		print(json.dumps(loginresponse)['errors']) 	
	print(token)

def define_server():
    global data
    data = json.loads('{"Authorization": "Bearer ' + token + '"}')  # the jobs statues call should have the token in the header as JSON
    define_server_url = baseurl + '/config/server'
    body=json.loads('{"ctm": "ctmtest" , "host": "ctmtest", "id": "ABC", "port": 2369 }')
    r2 = requests.post(define_server_url, headers=data , json=body , verify=False)
    print(r2.text)


def logouturl1():
	logouturl = baseurl + '/session/logout'
	body = json.loads('{ "token":"' + token + '", "username": "' + username + '"}')
	r3 = requests.post( logouturl , data=body, verify=False)
	print(r3.text)
	
tokengen()
define_server()
logouturl1()
