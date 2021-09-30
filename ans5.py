# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:00:52 2021

@author: Administrator
"""
pas = input()
a=b=c=d=0
if len(pas)>=8 and len(pas)<=12:
    for i in pas:
        if i.islower():
            a+=1
        if i.isupper():
            b+=1
        if i.isdigit():
            c+=1
        if i=='$' or i=='#' or i=='a':
            d+=1
if a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(pas):
    print("valid")
else:
    print("invalid")