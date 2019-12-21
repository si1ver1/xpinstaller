#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from config import *
from datetime import datetime
from time import time as timer
from multiprocessing.pool import ThreadPool
from shutil import rmtree
from urllib.request import urlretrieve
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
        self.entry1.insert(END, xp_url)
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Rego download url:", width=26)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        self.entry2 = Entry(frame2)
        self.entry2.insert(END, rego_url)
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        lbl3 = Label(frame3, text=".Net version download:", width=26)
        lbl3.pack(side=LEFT, padx=5, pady=5)
        self.entry3 = Entry(frame3)
        self.entry3.insert(END, net_url)
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

        frame7 = Frame(self, borderwidth=1, relief="sunken")
        frame7.pack(fill=X)
        txt7 = Text(frame7, wrap=NONE, width=96, height=16, borderwidth=0)
        scrollb7 = Scrollbar(frame7, orient=VERTICAL, command=txt7.yview)
        txt7['yscroll'] = scrollb7.set

        scrollb7.pack(side="right", fill="y")
        txt7.pack(side="left", fill="both", expand=True)
        frame7.place(x=5, y=185)

        frame6 = Frame(self)
        frame6.pack(fill=X)
        button1 = Button(frame6, text="Run", command=self.run_install)
        button1.pack(side=LEFT, padx=5, pady=5)
        button2 = Button(frame6, text="Close", command=self.close_window)
        button2.pack(side=RIGHT, padx=5, pady=5)

        sys.stdout = TextRedirector(txt7, "stdout")
        sys.stderr = TextRedirector(txt7, "stderr")

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

    def reporthook(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(totalsize)), readsofar, totalsize)
            sys.stderr.write(s)
            sys.stderr.write("\n")
            if readsofar >= totalsize:  # near the end
                sys.stderr.write("\n")
        else:  # total size is unknown
            sys.stderr.write("read %d\n" % (readsofar,))

    def run_install(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        print(dt_string, 'Starting XchangePoint Installer')
        print(dt_string, 'Downloading files')

        # Create temp folder and download files into it
        if not os.path.exists("./temp"):
            os.mkdir("./temp")

        """
        print(dt_string, 'Downloading XP: xp_url')
        myfile = requests.get(xp_url)
        open('./temp/1mb.txt', 'wb').write(myfile.content)
        print(dt_string, 'XP Download Complete')
        """
        urlretrieve(xp_url, 'downloaded_file.zip', self.reporthook)

        # Remove temp folder and files
        # rmtree("./temp")

def main():
    root = Tk()
    app = XPInstaller()
    root.mainloop()

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

if __name__ == '__main__':
    main()