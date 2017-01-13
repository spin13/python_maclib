# -*- coding: utf-8 -*-

import os
import time
import util
import urllib, urllib2
import base64
from datetime import datetime
import env
from glob import glob


END_POINT = env.END_POINT
BASE_DIR = env.BASE_DIR
STORAGE_URL = env.STORAGE_URL

def get_latest_file(dirname):
    dest = os.path.join(dirname, '*.png')
    files = [(f, os.path.getmtime(f)) for f in glob(dest)]
    if len(files) <= 0:
        return
    latest_path = sorted(files, key=lambda files: files[1])[-1]
    return latest_path[0]

def getext(filename):
    return os.path.splitext(filename)[-1].lower()

def post_data(filename):
    print(1)
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    params = { 
        'base64_data': base64.b64encode(open(filename, 'rt').read()),
        'name': now
    }
    params = urllib.urlencode(params)
    req = urllib2.Request(END_POINT)
    req.add_data(params)
    res = urllib2.urlopen(req)
    util.clipboard_set_data(STORAGE_URL + now + '.png')
    print('ok')
    return 0


if __name__ in '__main__':
    latest_file = get_latest_file(BASE_DIR)
    latest_back_file = latest_file
    while 1:
        time.sleep(1)
        latest_file = get_latest_file(BASE_DIR)
        if latest_back_file != latest_file:
            post_data(latest_file)
            os.remove(latest_file)


