#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:22:20 2019

@author: rafliano
"""

def kecepatan(jarak, waktu):
    print('menghitung kecepetan')
    return jarak / waktu

def waktu_tempuh(kecepetan, jarak):
    print('menghitung waktu tempuh')
    return jarak / kecepatan