#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:05:17 2019

@author: rafliano
https://www.youtube.com/watch?v=vWuSLG_6rxA&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=13
"""
# fungsi dengan argumen sederhana
def siswa(nama):
    print('siswa ini bernama:',nama)
    
siswa('sowang')

# fungsi dengan menggunakan keywords arguments

def guru(nama,pelajaran):
    print('guru ini bernama:',nama)
    print('guru ini mengajar:',pelajaran)

guru(nama='pare',pelajaran='seni rupa')
guru(pelajaran='olahraga',nama='imam')
guru('olahraga','raihan')

# fungsi dengan menggunakan default argument

def penjagaSekolah(nama,shift='siang',galak='tidak galak'):
    print('penjaga sekolah ini bernama:',nama)
    print('shiftnya:',shift)
    print('sifatnya:',galak)

penjagaSekolah('Entis')
penjagaSekolah('Maman',shift='malam')
penjagaSekolah('Asep',galak='Galak Sangat')
