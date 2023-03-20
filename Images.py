# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:59:57 2023

@author: Gebruiker
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
#Change the icon in the left hand corner 
    #root.iconbitmap('path to the icon')

my_img = ImageTk.PhotoImage(Image.open('GunsNRoses.jpg'))
my_label = Label(image=my_img)
my_label.pack()





button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()
root.mainloop()