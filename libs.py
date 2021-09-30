# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:36:08 2021

@author: Administrator
"""

import os
print(os.listdir())

import glob
file = glob.glob('*.py')
for i in file:
    print(i+" "+str(os.path.getsize(i))+" bytes")


print(set(glob.glob('*'))-set(glob.glob('*.py')))


dirs=0
files=0
tot = os.listdir()
for i in tot:
    if os.path.isdir(i):
        dirs+=1
        print(i)
print("total dirs "+ str(dirs))
for i in tot:
    if not os.path.isdir(i):
        files+=1
        print(i)
print("total files" + str(files))


import getpass
print(getpass.getuser())
print(os.getcwd())
import platform
print(platform.system())
print(os.getpid())
import datetime
print(datetime.datetime.now())
print(datetime.date(2021,9, 23))
print(datetime.date(2021,9, 21))
print(os.environ)
import sys
print(sys.executable)


import psutil
print(psutil.disk_usage("C:\\"))
print(psutil.cpu_stats())
print(psutil.virtual_memory())



for i in range(0,100):
    os.mkdir("hi"+str(i))
for i in range(0,100):
    os.rmdir("hi"+str(i))


import glob
file = glob.glob('*.txt')
for i in file:
    os.rename(i, os.path.splitext(i)[0]+'.log')


import filecmp
res = filecmp.dircmp("C:\\Users\\Administrator\\Desktop\\lab","C:\\Users\\Administrator\\Desktop\\lab2")
res.report()
print(res.common_files)
print(res.diff_files)
print(res.left_list)
print(res.right_list)


import random
print(random.randint(1000, 9999))



import os,time
for i in os.listdir():
    if os.stat(i).st_ctime< time.time() - 10*86400:
        if os.path.isfile(i):
            os.remove(i)
            
        
import os,time
for i in os.listdir():
    if os.stat(i).st_mtime< time.time() - 10*86400:
        if os.path.isfile(i):
            os.remove(i)
            
import os,time
for i in os.listdir():
    print(str(time.ctime(os.stat(i).st_atime))+" "+ str(time.ctime(os.stat(i).st_mtime)) +" "+ str(time.ctime(os.stat(i).st_ctime))+" "+str(os.stat(i).st_size)+"bytes")



email = "he123@gmail.com"
count=0
for i in email:
    if i in '@.':
        count+=1
if count>=2 and email[-3:-1]+email[-1]=='com':
    print("correct")
else:
    print("incorrect")

import re
email = "he123@gmail.com"
reg = re.search("^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", email)
if reg:
    print("correct")
else:
    print("incorrect")


fopen = open("newtime.txt","w")
print(time.ctime(os.stat("newtime.txt").st_mtime))

from pathlib import Path
Path("newfile101.txt").touch()
print(time.ctime(os.stat("newfile101.txt").st_mtime))

