'''
Created on Feb 24, 2019
@author: Burkhard A. Meier
'''






import tkinter as tk        
from tkinter import ttk     

gui = tk.Tk()                           
gui.geometry('400x200+300+300')         

gui.title('GUI written in tkinter')     
gui.iconbitmap('py.ico')                

def click_event_one():                                  
    update_label.config(text=entry_one_str.get())      

def click_event_two():                                    
    update_label.config(text=entry_two_str.get())

button_one = ttk.Button(gui, text="Click Me", command=click_event_one)  
button_one.grid(column=0, row=0)   

entry_one_str = tk.StringVar(value='<default text ONE>')      # variable to hold string
entry_one = ttk.Entry(gui, width=20, textvariable=entry_one_str)                   
entry_one.grid(column=1, row=0) 

button_two = ttk.Button(gui, text="Click Me", command=click_event_two)  
button_two.grid(column=0, row=1)                       

entry_two_str = tk.StringVar(value='<default text TWO>')      # variable to hold string
entry_two = ttk.Entry(gui, width=20, textvariable=entry_two_str)                   
entry_two.grid(column=1, row=1)

update_label = tk.Label(gui, text='Label')
update_label.grid(column=0, row=2, columnspan=2)        # columnspan to place label across cols


gui.mainloop()                          






















