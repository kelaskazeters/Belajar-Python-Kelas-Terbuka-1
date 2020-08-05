#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:05:48 2019

@author: rafliano
"""
number = 50;

for i in range(0,40):
    print(i)
    
    if i is number:
        print('angka ditemukan',i)
        break
else:
    print('angka tidak ditemukan')

print('space diluar for')
