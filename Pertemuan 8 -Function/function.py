#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:55:30 2019

@author: rafliano
https://www.youtube.com/watch?v=WjM68icSw3s&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=12
"""
# membuat function sederhana

def suaraayam():
    print('kukuruyuk')

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')
    
# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'ayam adalah',hargaTotal)

hargaayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)