
#!/usr/bin/python3

# this script look for address pass in argument

import os , webbrowser , sys

sys.argv

#check if command line argument are passed
if len(sys.argv) > 1 :
        address = ' '.join(sys.argv[1:])  # joining with black space of string from list
else:
        address = " New York , USA  "  # any default adddress

url = 'https://www.google.com/maps/place/'   # default web page to search address
browser = '/usr/bin/google-chrome'              # browswe path in server

webbrowser.get(browser).open_new_tab(url + address)
