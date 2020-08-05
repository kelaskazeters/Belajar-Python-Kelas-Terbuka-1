#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:31:48 2019

@author: rafliano
"""

import sys

data_list = [1,2,3,4,5,"syahrini","dompet","via vallen", False, 3.14]
data_tuple = (1,2,3,4,5,"syahrini","dompet","via vallen", False, 3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

#print(data_list)
#print(data_tuple)

print("besar data list:", besar_datalist)
print("besar data tuple:", besar_datatuple)