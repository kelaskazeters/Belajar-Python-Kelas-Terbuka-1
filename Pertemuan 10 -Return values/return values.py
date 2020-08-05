#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:04:44 2019

@author: rafliano
https://www.youtube.com/watch?v=23dDEp6WPH4&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=14
"""
# fungsi dengan return value

def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari',argumen,'adalah',total)
    return total

a = kuadrat(4)
print(a)

print("+"*100)

# fungsi dengan return value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'X',argumen2,'=',total)
    return total

b = kali(3,tambah(3,4))
print(b)