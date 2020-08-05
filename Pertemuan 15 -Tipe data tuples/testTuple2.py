#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:48:14 2019

@author: rafliano
"""

import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

print("waktu untuk memproses list:",data_list)
print("waktu untuk memproses tuple:",data_tuple)