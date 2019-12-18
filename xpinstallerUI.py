#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
from datetime import datetime
from time import time as timer
from multiprocessing.pool import ThreadPool
from shutil import rmtree
from tkinter import *
from tkinter.ttk import *

try:
    import httplib
except:
    import http.client as httplib


class XPInstaller(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("XchangePoint Installer")
        self.pack(fill=BOTH, expand=True)
        self.centerWindow()

        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="XchangePoint download URL:", width=26)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        self.entry1 = Entry(frame1)
        self.entry1.insert(END, 'https://rantcell.com/10mb.txt')
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Rego download url:", width=26)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        self.entry2 = Entry(frame2)
        self.entry2.insert(END, 'https://rantcell.com/5mb.txt')
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        lbl3 = Label(frame3, text=".Net version download:", width=26)
        lbl3.pack(side=LEFT, padx=5, pady=5)
        self.entry3 = Entry(frame3)
        self.entry3.insert(END, 'https://rantcell.com/1mb.txt')
        self.entry3.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)
        lbl4 = Label(frame4, text="Endpoint url:", width=26)
        lbl4.pack(side=LEFT, padx=5, pady=5)
        self.entry4 = Entry(frame4)
        self.entry4.insert(END, 'https://aramarkv2dev.xchangefusion.com/devices')
        self.entry4.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=X)
        lbl5 = Label(frame5, text="Terminal no to install:", width=26)
        lbl5.pack(side=LEFT, padx=5, pady=5)
        self.entry5 = Entry(frame5)
        self.entry5.insert(END, '10000')
        self.entry5.pack(fill=X, padx=5, expand=True)

        """
        frame6 = Frame(self, borderwidth=1)
        frame6.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH)
        """

        frame6 = Frame(self)
        frame6.pack(fill=X)
        txt6 = Text(frame6, width=90, height=16)
        txt6.pack(side=LEFT, padx=5, pady=5)
        scrollb6 = Scrollbar(frame6)
        scrollb6.pack()

        frame7 = Frame(self)
        frame7.pack(fill=X)
        button1 = Button(frame7, text="Run") #, command=self.write_file)
        button1.pack(side=LEFT, padx=5, pady=5)
        button2 = Button(frame7, text="Close", command=self.close_window)
        button2.pack(side=RIGHT, padx=5, pady=5)

    def centerWindow(self):
        w = 800
        h = 450

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def close_window(self):
        exit()


"""
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
"""


def main():
    root = Tk()
    app = XPInstaller()
    root.mainloop()


"""
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
"""
if __name__ == '__main__':
    main()