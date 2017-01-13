# -*- coding: utf-8 -*-
import subprocess

# set data to clibboard
def clipboard_set_data(data):
    process = subprocess.Popen('pbcopy', stdin=subprocess.PIPE)
    process.communicate(data.encode('utf-8'))

# get current clipboard data
def clipboard_get_data():
    return subprocess.Popen('pbpaste', stdout=subprocess.PIPE).communicate()[0]

if __name__ == '__main__':
    # clipboard_set_data("aaa")
    a = clipboard_get_data()
    print(a)

