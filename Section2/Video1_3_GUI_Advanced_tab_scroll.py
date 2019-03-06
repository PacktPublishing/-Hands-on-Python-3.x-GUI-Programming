'''
Created on Mar 5, 2019
@author: Burkhard A. Meier
'''






import tkinter as tk        
from tkinter import ttk, Menu, scrolledtext    
import sys


gui = tk.Tk()                           
gui.geometry('600x400+450+150')         

gui.title('GUI written in tkinter')     


def tab_two_widgets(parent):
    scroll = scrolledtext.ScrolledText(parent, width=48, height=8, wrap=tk.WORD)
    scroll.grid(column=0, row=0)


# create the controls in a function
def create_widgets():    
    # callbacks are now inner functions
    def click_event_one():      
        text_one = entry_one_str.get()                            
        update_label.config(text=text_one)      

    def click_event_two():    
        text_two = entry_two_str.get()                                
        update_label.config(text=text_two)
    
    tab_control = ttk.Notebook(gui)             # create tab control (aka Notebook)
    
    tab_one = ttk.Frame(tab_control)            # create a frame       
    tab_control.add(tab_one, text='Tab 1')
    
    tab_two = ttk.LabelFrame(tab_control, text=' Webpage source ')            # create a frame       
    tab_control.add(tab_two, text='Tab 2')  
    
    tab_two_widgets(parent=tab_two)
    
    tab_control.pack(fill='both')
    
    # make tab one the parent instead of gui
    button_one = ttk.Button(tab_one, text="Click Me", command=click_event_one)  
    button_one.grid(column=0, row=0, padx=10, pady=4)                               # add y-padding   
    
    entry_one_str = tk.StringVar(value='')      # variable to hold string
    entry_one = ttk.Entry(tab_one, width=20, textvariable=entry_one_str)                   
    entry_one.grid(column=1, row=0) 
    
    button_two = ttk.Button(tab_one, text="Click Me", command=click_event_two)  
    button_two.grid(column=0, row=1)                       
    
    entry_two_str = tk.StringVar(value='')      # variable to hold string
    entry_two = ttk.Entry(tab_one, width=20, textvariable=entry_two_str)                   
    entry_two.grid(column=1, row=1)
    
    update_label = tk.Label(tab_one, text='Label')
    update_label.grid(column=0, row=2, columnspan=2)


def create_menu():
    def _quit():
        gui.quit()
        gui.destroy()
        sys.exit()              
        
    menu_bar = Menu(gui)            # parent=gui

    file_menu = Menu(menu_bar, tearoff=False)               # parent=menu_bar
    file_menu.add_command(label="New")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=_quit)
    
    menu_bar.add_cascade(menu=file_menu, label="File")     # add menu
    gui.config(menu=menu_bar)    



create_widgets()
create_menu()

gui.mainloop()                          






















