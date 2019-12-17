#!/usr/bin/env python
import os
import zipfile
import requests
from datetime import datetime

try:
    import httplib
except:
    import http.client as httplib

def internet_on():
    # Checks network connection by initiating a HEAD request to google.com
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def log():
    with open('installer.log', 'a') as f:
        print(dt_string, 'Starting XchangePoint Installer', file = f)
        print(dt_string, 'Checking network connection:', internet_on(), file=f)

def download():
    with open('installer.log', 'a') as f:
        print(dt_string, 'Downloading XchangePoint', file = f)
    url = 'http://files.taskretail.com.au/Aramark/1905/XP1905_20191025.zip'
    r = requests.get(url)
    with open('./', 'wb') as l:
        l.write(r.content)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
log()
download()