#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:49:11 2019

@author: rafliano
"""

from PIL import Image

im = Image.open("foto.jpg")

print("format file:" + im.format)
print("format file:" + str(im.size))
print("format file:" + im.mode)

im.show