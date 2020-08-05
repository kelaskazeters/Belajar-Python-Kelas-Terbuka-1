#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:08:57 2019

@author: rafliano
"""
# class
class mahasiswa():
    
    jurusan = 'tehnik'
    __nilai = 0 # private
    def __init__(self,input_nama, input_kode):
        self.nama = input_nama # public
        self.kode = input_kode # public
        
    def uts(self,input_nilai):
        self.__nilai += input_nilai
        
    def uas(self,input_nilai):
        self.__nilai += input_nilai
        
    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama, 'lulus')

# main programnya

ali = mahasiswa("muhammad ali", 121212129090)
ucup = mahasiswa("ucub binucup", 121212129091)

ali.uts(10)
ali.uas(50)
ali.check_status()
ucup.uts(5)
ucup.uas(25)
ucup.check_status()
