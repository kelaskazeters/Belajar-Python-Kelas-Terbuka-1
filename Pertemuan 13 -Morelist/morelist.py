#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:18:01 2019

@author: rafliano
"""

Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

# beberapa method yang biasa digunakan untuk memanipulasi list
# method untuk menambah data kedalam list
Barang.append('sepeda')
print(Barang)

Barang.extend('dompet')
print(Barang)

Barang.insert(3,'sepeda')
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda')
print("jumlah sepeda adalah: ",jumlahSepeda)

# meremove data
Barang.remove('sepeda')
print(Barang)

Barang.reverse()
print(Barang)

print(100*'=')
Stuff = Barang.copy()
Stuff.append('gelas')
print(Stuff)
print(Barang)





