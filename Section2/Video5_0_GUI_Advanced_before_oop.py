'''
Created on Mar 5, 2019
@author: Burkhard A. Meier
'''






import tkinter as tk        
from tkinter import ttk, Menu, scrolledtext, PhotoImage    
import sys
from urllib.request import urlopen
from os.path import splitext
from time import sleep         # careful - this can freeze the GUI


class GuiOOP():    
    gui = tk.Tk()                           
    gui.geometry('660x400+450+150')                 # widen gui width to fit button image
    gui.title('GUI written in tkinter')   
    gui.resizable(False, False)                     # disable resizing the GUI
    
    img = PhotoImage(file='LightsInTheCity.gif')    # module-level variable
    
    
    def read_url(url="https://docs.python.org/3/"):
        f = urlopen(url)
        web_text = f.read()
        return web_text
    
    def tab_two_widgets(parent, width=78, height=21):
        text = read_url()
        scroll = scrolledtext.ScrolledText(parent, width=width, height=height, wrap=tk.WORD)  
        scroll.insert(tk.INSERT, text)
        scroll.grid(column=0, row=0, padx=8, pady=2)
    
           
    def tab_three_widgets(parent, data=None):
        if not data:
            data = [x + 1 for x in range(50)]       # list comprehension to create data
        combo_str = tk.StringVar()
        combo = ttk.Combobox(parent, width=20, textvariable=combo_str)
        combo.grid(column=0, row=0, padx=8, pady=6, sticky='N')
        combo['values'] = data                                      # insert list data 
        combo.current(0)                            
        
        def update_title_icon():
            new_title = splitext(img.cget('file'))[0]               # remove file extension
            combo_value = combo.get()
            if combo_value:
                new_title +=  ' -- ' + combo_value                  # update if combobox value
            gui.title(new_title)                                    # display  
            gui.iconbitmap('py.ico')                                # change icon (expected inside the same folder)
            
        button_img = ttk.Button(parent, image=img, command=update_title_icon)   # use module-level variable 
        button_img.grid(column=1, row=0)
    
              
    # create the controls in a function
    def create_widgets():    
        tab_control = ttk.Notebook(gui)             # create tab control (aka Notebook)
        
        tab_one = ttk.Frame(tab_control)            # create a frame       
        tab_control.add(tab_one, text='Tab 1')
        tab_one_widgets(parent=tab_one)
        
        tab_two = ttk.LabelFrame(tab_control, text=' Webpage source ')            # create a frame       
        tab_control.add(tab_two, text='Tab 2')  
        tab_two_widgets(parent=tab_two)
        
        tab_three = ttk.Frame(tab_control) 
        tab_control.add(tab_three, text='Tab 3')
        tab_three_widgets(parent=tab_three)
            
        tab_control.pack(fill='both')
    
        
    # tab one refactored into function to better match the rest of the code
    def tab_one_widgets(parent):   
        # inner functions
        def click_event_one():      
            text_one = entry_one_str.get()                            
            update_label.config(text=text_one)      
    
        def click_event_two():    
            text_two = entry_two_str.get()                                
            update_label.config(text=text_two)
    
        # Create a container to hold buttons
        entries_frame = ttk.LabelFrame(parent, text=' Entries ')
        entries_frame.grid(column=0, row=0, sticky='W') 
            
        # make entries_frame the parent instead of gui
        button_one = ttk.Button(entries_frame, text="Click Me", command=click_event_one)  
        button_one.grid(column=0, row=0, sticky='W')
        
        entry_one_str = tk.StringVar(value='')      # variable to hold string
        entry_one = ttk.Entry(entries_frame, width=20, textvariable=entry_one_str)                   
        entry_one.grid(column=1, row=0, sticky='W') 
        
        button_two = ttk.Button(entries_frame, text="Click Me", command=click_event_two)  
        button_two.grid(column=0, row=1, sticky='W')                       
        
        entry_two_str = tk.StringVar(value='')      # variable to hold string
        entry_two = ttk.Entry(entries_frame, width=20, textvariable=entry_two_str)                   
        entry_two.grid(column=1, row=1, sticky='W')
        
        update_label = tk.Label(entries_frame, text='<Label>', height=8)
        update_label.grid(column=0, row=2, sticky='W')
               
        # add some padding
        for child in entries_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
        
          
        # update progressbar in callback loop
        def run_progressbar():
            progress_bar["maximum"] = 100
            for i in range(101):
                sleep(0.05)
                progress_bar["value"] = i   # increment progressbar
                progress_bar.update()       # have to call update() in loop
            progress_bar["value"] = 0       # reset/clear progressbar  
        
        def start_progressbar():            # Progress will restart itself once it finishes
            progress_bar.start()
            
        def stop_progressbar():
            progress_bar.stop()
         
        def progressbar_stop_after(wait_ms=1000):    
            gui.after(wait_ms, progress_bar.stop)
    
           
        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(parent, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=3, sticky='W')        
        
        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ",  command=run_progressbar).grid(column=0, row=0, sticky='W')  
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop immediately ",   command=stop_progressbar).grid(column=0, row=2, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop after second ",  command=progressbar_stop_after).grid(column=0, row=3, sticky='W')  
      
        # add some padding
        for child in buttons_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
    
            
        # Add a Progressbar
        progress_bar = ttk.Progressbar(parent, orient='horizontal', length=640, mode='determinate')
        progress_bar.grid(column=0, row=4, pady=4, columnspan=2) 
        
        for child in parent.winfo_children():  
            child.grid_configure(padx=8, pady=2) 
                    
    
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
    
    
    def run_gui():
        create_widgets()
        create_menu()
        gui.mainloop()                          
    

if __name__ == '__main__':
    run_gui()


















