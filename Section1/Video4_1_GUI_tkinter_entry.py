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
    button_one.config(text=entry_one_str.get())         # 3. call get() on the StringVar 

def click_event_two():                                    
    button_two.config(text=entry_two_str.get())         


button_one = ttk.Button(gui, text="Click Me", command=click_event_one)  
button_one.grid(column=0, row=0)   

entry_one_str = tk.StringVar()                                          # 1. class instance variable to hold string
# entry_one_str = tk.StringVar(value='<default text>')                  # 
entry_one = ttk.Entry(gui, width=20, textvariable=entry_one_str)        # 2. assign variable to textvariable                   
entry_one.grid(column=1, row=0) 

button_two = ttk.Button(gui, text="Click Me", command=click_event_two)  
button_two.grid(column=0, row=1)                       

entry_two_str = tk.StringVar(value='<default text>')                    # 1. with optional default value
entry_two = ttk.Entry(gui, width=20, textvariable=entry_two_str)                   
entry_two.grid(column=1, row=1)



gui.mainloop()                          






















