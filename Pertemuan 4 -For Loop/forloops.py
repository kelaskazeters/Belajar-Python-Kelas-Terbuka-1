#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 07:55:16 2019

@author: rafliano
"""
## list sebagai iterable
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
#for g in gorengan:
#    print(g)
#    print(len(g))
#
## string sebagai iterable
#
#bakwan = 'bakwan'
#
#for i in bakwan:
#    print(i)

# for didalam for

buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

Daftar_belanja = [gorengan,buah,sayur]

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)