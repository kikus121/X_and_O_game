# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 07:48:13 2018

@author: Kamil
"""
from tkinter import *
import Class2 
from Class2 import Buton






while True:
    window = Tk()
    
    button1 = Buton(window,0,0)
    button2 = Buton(window,0,1)
    button3 = Buton(window,0,2)
    
    button4 = Buton(window,1,0)
    button5 = Buton(window,1,1)
    button6 = Buton(window,1,2)
    
    button7 = Buton(window,2,0)
    button8 = Buton(window,2,1)
    button9 = Buton(window,2,2)
    
    
    
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.rowconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)
    window.rowconfigure(3, weight=1)
    
    window.mainloop()

