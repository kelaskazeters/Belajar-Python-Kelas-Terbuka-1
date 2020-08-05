#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 06:49:17 2019

@author: rafliano
"""

Data = [1,4,9,16,25,36,49,64]
# mengakses list
Subdata1 = Data[3]
Subdata2 = Data[-3]
# memotong list
Subdata3 = Data[2:4]
Subdata4 = Data[:4]
Data2 = [100,200,300,400,500,600,700,800]
# menambah list
Data3 = Data + Data2
# merubah content dari list
print(Data)
#Data[4] = 87
# mencopy list ke variable baru
a = Data[:]
a[7]= 87
#merubah content list dengan menggunakan metode slicing
Data[3:5] = [11,12]
# list dalam list
x = [Data,Data2]
#mengakses list dalam multidimensional list
y = x[0][3]
# methods untuk list
Data.append(30)
# function yang bisa kita gunakan kepada list
panjang_list = len(Data)

print(Data)
print(panjang_list)