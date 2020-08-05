#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:10:54 2019

@author: rafliano
https://www.youtube.com/watch?v=ZnBZWAUusj8&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=22
"""
# tehnik looping

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             'Syahrini']
kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro',
        'Jodohku']

# enumerate

for index,band in enumerate(nama_band):
    print(index,':',band)

# zip

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul:',lagu)
    
playlist = {'baby baby', 'ada apa dengan cinta', 'cenat-cenut', 'hidup 100 tahun', 'kuda', 'kucing'}

for lagu in sorted(playlist):
    print(lagu)

# dictionary

print(100*'=')

playlist2 = {'Payung Teduh':'Akad',
             'Fourtwnty':'Zona Nyaman',
             'Dialog Dini Hari':'Rumahku'}

for i,v in playlist2.items():
    print(i,'lagunya:',v)

for i in reversed(range(1,10,1)):
    print(i)
