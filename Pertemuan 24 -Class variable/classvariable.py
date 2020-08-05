#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:26:55 2019

@author: rafliano
"""

# class
class mahasiswa():
    
    jumlah_mahasiswa = 0
    
    def __init__(self,input_nama, input_kode):
        self.nama = input_nama # public
        self.kode = input_kode # public
    
        mahasiswa.jumlah_mahasiswa += 1
    
# main programnya

ali = mahasiswa("muhammad ali", 121212129090)
ucup = mahasiswa("ucub binucup", 121212129091)
cassandra = mahasiswa('cassandra aja', 1212121229092)

print(mahasiswa.jumlah_mahasiswa)