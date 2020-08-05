#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:35:24 2019

@author: rafliano
https://www.youtube.com/watch?v=S8PxQTcme9k&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=11
"""
# else, break, continue

angka = 0

while angka < 10:
    
    if angka is 5:
        #print('checkpoint1')
        break 
        continue
        pass
        #print('checkpoint2')
    print('nilai angka adalah', angka)
    angka = angka + 1
else:
    print('nilai angka diakhir while adalah',angka)

print('diluar while')
