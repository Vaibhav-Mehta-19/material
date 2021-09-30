# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:40:29 2021

@author: Administrator
"""

colors = [
   {
     "colors": "red",
     "values": "#f00"
   },
   {
     "colors": "green",
     "values": "#0f0"
   },
   {
     "colors": "blue",
     "values": "#00f"
   },
   {
     "colors": "cyan",
     "values": "#0ff"
   },
   {
     "colors": "magenta",
     "values": "#f0f"
   },
   {
     "colors": "yellow",
     "values": "#ff0"
   },
   {
     "colors": "black",
     "values": "#000"
   }]
for i in colors:
    print(i.get('colors')+"("+i.get('values')+")")