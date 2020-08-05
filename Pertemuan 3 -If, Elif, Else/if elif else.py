#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 07:17:59 2019

@author: rafliano
"""

nilai = 50

if nilai == 75: # equal explisit
    print("nilai anda:", nilai)
 
if nilai == 60: # equal
    print("nilai anda:", nilai)

if nilai != 60: # not equal
    print("nilai anda bukan: 60")

print(100*"=")

nilai = 90

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C")
elif 50 <= nilai <= 60:
    print("nilai anda adalah F, lakukan perbaikan")
else:
    print("maaf anda tidak lulus ujian ini")

print(100*"+")

print("operator logika untuk list dan string")
print(" ")

gorengan=["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"] 
beli = "sepatu"

if beli in gorengan:
    print('Mamang Bilang, " ya, saya jual',beli,'"')
if not beli in gorengan:
    print('"saya gak jual',beli,'"')

karakter = "z"
if karakter in beli:
    print("ada", karakter,"di",beli)
else:
    print("tidal ada", karakter,"di",beli)












