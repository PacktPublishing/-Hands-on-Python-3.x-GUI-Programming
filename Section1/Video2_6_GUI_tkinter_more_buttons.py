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

def click_event():                                      # call back function
    gui.title('Button has been clicked')                # update window title
    button_one.config(text='I have been clicked!')      # update button text
    another_button = ttk.Button(gui, text="Another", command=click_event)    # add same callback function to new button
    another_button.pack() 
    
button_one = ttk.Button(gui, text="Click Me", command=click_event)  # define command
button_one.pack()                        

gui.mainloop()                          # run main event loop






















