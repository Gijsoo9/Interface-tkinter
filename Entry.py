# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:22:44 2023

@author: Gebruiker
"""
from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='red', fg='white', borderwidth=5)
e.pack()
e.insert(0, 'Enter Your Name: ')

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
myButton = Button(root, text='Enter Your Name', padx=50, pady=50, command=myClick, fg='blue', bg='red')
myButton.pack()

root.mainloop()
