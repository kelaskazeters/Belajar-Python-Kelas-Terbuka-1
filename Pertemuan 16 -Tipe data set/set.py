#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:36:29 2019

@author: rafliano
https://www.youtube.com/watch?v=Fn6073uEifE&list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1&index=20
"""
# sets, himpunan:

superhero = set()

superhero.add('wiro sableng')
superhero.add('gundala')
superhero.add('hmei7')
superhero.add(212)

print(superhero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))
print(ganjil.intersection(prima))
