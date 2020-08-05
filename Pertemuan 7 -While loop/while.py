#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:27:45 2019

@author: rafliano
https://www.youtube.com/watch?v=S8PxQTcme9k&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=11
"""

angka = 0

while angka < 5:
    print('nilai angka adalah', angka)
    angka = angka + 1

print('diluar while')

start = True # variable bolean
angka = 0

while start:
    print("didalam while")
    if angka is 100:
        start = False
        print('oke angka 100 diketemukan')
    angka += 1