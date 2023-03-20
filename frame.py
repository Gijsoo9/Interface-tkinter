# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:44:30 2023

@author: Gebruiker
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')

frame = LabelFrame(root, text='This is my Frame...', padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here")
b.pack()
root.mainloop()