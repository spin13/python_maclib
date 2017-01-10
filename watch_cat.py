# -*- coding: utf-8 -*-

import os, sys
import time
import shutil
import util
import urllib, urllib2
import requests
import env

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

END_POINT = env.END_POINT
BASE_DIR = "/Users//SS"
DEST_DIR = "C:\\GDrive\\icloud\\2017"

def getext(filename):
    return os.path.splitext(filename)[-1].lower()

def post_data(filename):
    print(1)
    files = {'files': open(filename, "rb")}
    print os.path.getsize(filename)
    res = requests.post(END_POINT, files=files)
    print(2)
    return res.text


class WatchHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.jpg','.png','.txt'):
            # shutil.copy(event.src_path, DEST_DIR)
            print(event.src_path)
            a = post_data(event.src_path)
            print(a)


if __name__ in '__main__':
    while 1:
        event_handler = WatchHandler()
        observer = Observer()
        observer.schedule(event_handler,BASE_DIR,recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
