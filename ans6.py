# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 10:22:10 2021

@author: Administrator
"""

ans = input()
dict1={}
ll = ans.split(" ")
for i in ll:
    if i in dict1:
        n = dict1.get(i)
        dict1[i] = n+1
    else:
        dict1.update({i:1})
print(dict1)