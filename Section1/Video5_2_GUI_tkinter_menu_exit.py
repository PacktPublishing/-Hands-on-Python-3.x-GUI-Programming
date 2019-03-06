'''
Created on Feb 24, 2019
@author: Burkhard A. Meier
'''






import tkinter as tk        
from tkinter import ttk, messagebox, Menu    

gui = tk.Tk()                           
gui.geometry('400x200+300+300')         

gui.title('GUI written in tkinter')     
gui.iconbitmap('py.ico')                

# create the controls in a function
def create_widgets():
    
    # callbacks are now inner functions
    def click_event_one():      
        text_one = entry_one_str.get()                            
        if text_one:                                                
            update_label.config(text='See message box')      
            messagebox.showinfo('Info Message Box Title', text_one)
    
    def click_event_two():    
        text_two = entry_two_str.get()                                
        update_label.config(text='See message box')
        rsp = messagebox.showwarning('Warning Message Box Title', text_two)
        if rsp:
            update_label.config(text='')
    
    button_one = ttk.Button(gui, text="Click Me", command=click_event_one)  
    button_one.grid(column=0, row=0)   
    
    entry_one_str = tk.StringVar(value='')      # variable to hold string
    entry_one = ttk.Entry(gui, width=20, textvariable=entry_one_str)                   
    entry_one.grid(column=1, row=0) 
    
    button_two = ttk.Button(gui, text="Click Me", command=click_event_two)  
    button_two.grid(column=0, row=1)                       
    
    entry_two_str = tk.StringVar(value='')      # variable to hold string
    entry_two = ttk.Entry(gui, width=20, textvariable=entry_two_str)                   
    entry_two.grid(column=1, row=1)
    
    update_label = tk.Label(gui, text='Label')
    update_label.grid(column=0, row=2, columnspan=2)


def create_menu():
    menu_bar = Menu(gui)            # parent=gui

    file_menu = Menu(menu_bar, tearoff=False)               # parent=menu_bar
    file_menu.add_command(label="New")                      # add menu item to menu
    file_menu.add_separator()
    file_menu.add_command(label="Exit")                     # create a second menu item
    
    menu_bar.add_cascade(menu=file_menu, label="File")      # add menu to menu bar
    gui.config(menu=menu_bar)    



create_widgets()
create_menu()

gui.mainloop()                          






















