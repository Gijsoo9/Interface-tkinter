# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:53:34 2023

@author: Gebruiker
"""
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')

r = IntVar()
r.set('2')

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()    

Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

root.mainloop()
