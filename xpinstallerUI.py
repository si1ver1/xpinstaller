#!/usr/bin/env python
import os
import requests
from datetime import datetime
from time import time as timer
from multiprocessing.pool import ThreadPool
from shutil import rmtree

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

def url_response(entry):
    path, uri = entry
    if not os.path.exists(path):
        r = requests.get(uri, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
    return path



now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
urls = [
("./temp/1mb.txt", "https://rantcell.com/1mb.txt"),
("./temp/5mb.txt", "https://rantcell.com/5mb.txt"),
("./temp/10mb.txt", "https://rantcell.com/10mb.txt")
]

print(dt_string, 'Starting XchangePoint Installer')
print(dt_string, 'Checking network connection:', internet_on())
print(dt_string, 'Downloading files')

# Create temp folder and download files into it
if not os.path.exists("./temp"):
    os.mkdir("./temp")

start = timer()
results = ThreadPool(4).imap_unordered(url_response, urls)
for path in results:
    print(path)
print("Elapsed Time: %s" % (timer() - start,))

# Remove temp folder and files
# rmtree("./temp")