# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:38:58 2021

@author: Administrator
"""
ip = input()
ll = ip.split(".")
corr=0
if len(ll)==4:
    for i in ll:
        if int(i)<=0 or int(i)>255:
            print("error wrnog ip")
            break
        else:
            corr+=1
else:
    print("wrong ip")
if(corr==4):
    print("right ip")