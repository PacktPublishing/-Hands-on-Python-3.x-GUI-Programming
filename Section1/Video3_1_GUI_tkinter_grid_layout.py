'''
Created on Feb 24, 2019
@author: Burkhard A. Meier
'''






import tkinter as tk        # alias as tk
from tkinter import ttk     # themed tk

gui = tk.Tk()                           # create class instance
gui.geometry('400x200+300+300')         # specify window width, height and position

gui.title('GUI written in tkinter')     # give the GUI a window title
gui.iconbitmap('py.ico')                # icon expected inside the same folder

def click_event_one():                                  # call back function
    gui.title('Button 1 has been clicked')              # update window title
    button_one.config(text='I have been clicked!')      # update button text

def click_event_two():                                    # call back function
    gui.title('Button 2 has been clicked')                # update window title
    button_two.config(text='I have been clicked too!')    # update button text

button_one = ttk.Button(gui, text="Click Me", command=click_event_one)  # define command
button_one.grid(column=0, row=0)        # use grid layout manager                

button_two = ttk.Button(gui, text="Click Me", command=click_event_two)  # define command
button_two.grid(column=1, row=0)        # use grid layout manager                

gui.mainloop()                          # run main event loop






















