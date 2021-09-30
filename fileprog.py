# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:36:06 2021

@author: Administrator
"""

import csv
with open("realestate.csv","r") as fobj:
    reader = csv.reader(fobj,delimiter=",")
    for line in reader:
        print(line)
        

import csv
with open("realestate.csv","r") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj,delimiter=",")
    for line in reader:
        print(line[1]+ " "+ line[3])
        

import csv
newset = set()
with open("realestate.csv","r") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj,delimiter=",")
    for line in reader:
        newset.add(line[1])
print(newset)


import csv
newset = dict()
with open("realestate.csv","r") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj,delimiter=",")
    for line in reader:
        if line[1] in newset:
            n = newset.get(line[1])
            newset[line[1]] = n+1
        else:
            newset.update({line[1]:1})
print(newset)

words=0
records=0
columns=0
chars=0
digits=0
vowels=0
with open("realestate.csv","r") as fobj:
    header = fobj.readline()
    ll = header.split(",")
    columns = len(ll)
    reader = csv.reader(fobj,delimiter=",")
    for line in reader:
        records+=1
        for word in line:
            words+= 1
            for c in word:
                if c.isdigit():
                    digits+=1
                chars+=1
                if c in ['a','e','i','o','u','A','E','I','O','U']:
                    vowels+=1
print(words)
print(chars)
print(digits)
print(records)
print(columns)
print(vowels)

import csv
with open("realestate.csv","r") as fobj:
    reader = csv.reader(fobj,delimiter=",")
    for line in reader:
        tot=""
        for i in line:
            ll = list(i)
            ll.reverse()
            string = "".join(ll)
            tot = tot+string
        print(tot)
