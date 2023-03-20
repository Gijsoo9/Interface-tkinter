# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:22:44 2023

@author: Gebruiker
"""
from tkinter import *

root = Tk()

#Creating a Label Widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My Name Is Gijs Wilbers')
#Shoving it onto the screen


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)


root.mainloop()
