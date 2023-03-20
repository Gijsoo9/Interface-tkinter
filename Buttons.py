# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:22:44 2023

@author: Gebruiker
"""
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I pressed the button!!")
    myLabel.pack()
    
myButton = Button(root, text='Press me!', pady=50, command=myClick, fg='blue', bg='red')
myButton.pack()

root.mainloop()
