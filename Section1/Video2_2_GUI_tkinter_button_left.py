'''
Created on Feb 24, 2019
@author: Burkhard A. Meier
'''






import tkinter as tk        # alias as tk
from tkinter import ttk     # themed tk

gui = tk.Tk()                           # create class instance
gui.geometry('400x200')                 # specify a window width and height
gui.title('GUI written in tkinter')     # give the GUI a window title
gui.iconbitmap('py.ico')                # icon expected inside the same folder

button_one = ttk.Button(gui, text="Click Me")   # create a button, parent=gui
button_one.pack(side=tk.LEFT)                   # align button left

gui.mainloop()                          # run main event loop






















