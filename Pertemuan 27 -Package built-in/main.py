#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:50:21 2019

@author: rafliano
"""

import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan ^_^")
    label2.pack()

label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana Menggunakan Python ")
tombol = tkinter.Button(main_window, text="Tekan AKuh", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()