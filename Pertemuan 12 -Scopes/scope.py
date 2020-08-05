#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:43:08 2019

@author: rafliano
https://www.youtube.com/watch?v=xkenVaGZ8aU&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=16
"""

# scope variable : glocal

namaKucing = 'cassandra'
makanKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # variable global
    nama = namaBaru # variable local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('rayyan')

kasihMakanKucing('alya','kety')

print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)

