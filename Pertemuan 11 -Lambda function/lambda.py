#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:32:08 2019

@author: rafliano
"""

def jumlah(a,b):
    c = a+b
    return c

hasil1 = jumlah(4,5)

# membuat anonymous function dengan lambda

kali = lambda x,y: x*y
hasil2 = kali(3,4)
print(hasil2)