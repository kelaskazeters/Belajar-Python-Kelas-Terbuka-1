#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:32:13 2019

@author: rafliano
"""

stacks = [1,2,3,4,5,6]
print('data sekarang: ',stacks)

# memassukan data baru
stacks.append(7)
print('data masuk: ',7)
stacks.append(8)
print('data masuk: ',8)
print('data sekarang: ',stacks)

out = stacks.pop()
print('data keluar: ',out)
print('data sekarang: ',stacks)
