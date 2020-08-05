#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:40:20 2019

@author: rafliano
"""

print('ini adalah program pembagian')

while True:
    try:
        import panda
        penyebut = int(input('masukkan penyebut: '))
        pembilang = int(input('masukkan pembilang: '))
        hasil = penyebut/pembilang
        break
    
    except  ValueError:
        print('yang anda masukkan bukan angka')
    except ZeroDivisionError:
        print('angka pembilang yang anda masukkan adalah nol, pilih yang lain ya bro/sist\n')
    except ImportError:
        print('ga ada modulenya bro')
    except Exception as err:
        print(err)
        
"""
    type of exception errors:
    1. IOError
    2. Import
    3. ValueError
    4. Division by zero
    5. KeyboardInterupted
    6. EOFError
"""

print('berhasil, hasil pembagian adalah: ', hasil)