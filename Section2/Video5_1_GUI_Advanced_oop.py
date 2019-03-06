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
    def __init__(self):  
        self.gui = tk.Tk()                           
        self.gui.geometry('660x400+450+150')                 
        self.gui.title('GUI written in tkinter')   
        self.gui.resizable(False, False)                     
        
        self.img = PhotoImage(file='LightsInTheCity.gif')   
        self.create_widgets()
        self.create_menu()


    def read_url(self, url="https://docs.python.org/3/"):
        f = urlopen(url)
        web_text = f.read()
        return web_text
    
    def tab_two_widgets(self, parent, width=78, height=21):
        text = self.read_url()
        scroll = scrolledtext.ScrolledText(parent, width=width, height=height, wrap=tk.WORD)  
        scroll.insert(tk.INSERT, text)
        scroll.grid(column=0, row=0, padx=8, pady=2)
           
    def tab_three_widgets(self, parent, data=None):
        if not data:
            data = [x + 1 for x in range(50)]       # list comprehension to create data
        combo_str = tk.StringVar()
        combo = ttk.Combobox(parent, width=20, textvariable=combo_str)
        combo.grid(column=0, row=0, padx=8, pady=6, sticky='N')
        combo['values'] = data                                      # insert list data 
        combo.current(0)                            
        
        def update_title_icon():
            new_title = splitext(self.img.cget('file'))[0]               # remove file extension
            combo_value = combo.get()
            if combo_value:
                new_title +=  ' -- ' + combo_value                       # update if combobox value
            self.gui.title(new_title)                                    # display  
            self.gui.iconbitmap('py.ico')                                # change icon (expected inside the same folder)
        
        # image exception occurs when running multiple unit tests 
        try:   
            button_img = ttk.Button(parent, image=self.img, command=update_title_icon)   
            button_img.grid(column=1, row=0)
        except Exception as ex:
            pass
#             print(ex)
              
    # create the controls in a function
    def create_widgets(self):    
        tab_control = ttk.Notebook(self.gui)             # create tab control (aka Notebook)
        
        tab_one = ttk.Frame(tab_control)            # create a frame       
        tab_control.add(tab_one, text='Tab 1')
        self.tab_one_widgets(parent=tab_one)
        
        tab_two = ttk.LabelFrame(tab_control, text=' Webpage source ')            # create a frame       
        tab_control.add(tab_two, text='Tab 2')  
        self.tab_two_widgets(parent=tab_two)
        
        tab_three = ttk.Frame(tab_control) 
        tab_control.add(tab_three, text='Tab 3')
        self.tab_three_widgets(parent=tab_three)
            
        tab_control.pack(fill='both')
  
    
    def click_event_one(self):      
        text_one = self.entry_one_str.get()                            
        self.update_label.config(text=text_one)      

    def click_event_two(self):    
        text_two = self.entry_two_str.get()                                
        self.update_label.config(text=text_two)
            
    # update progressbar in callback loop
    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i   # increment progressbar
            self.progress_bar.update()       # have to call update() in loop
        self.progress_bar["value"] = 0       # reset/clear progressbar  
    
    def start_progressbar(self):
        self.progress_bar.start()
        
    def stop_progressbar(self):
        self.progress_bar.stop()
     
    def progressbar_stop_after(self, wait_ms=1000):    
        self.gui.after(wait_ms, self.progress_bar.stop)
                        
    def tab_one_widgets(self, parent):       
        # Create a container to hold buttons
        entries_frame = ttk.LabelFrame(parent, text=' Entries ')
        entries_frame.grid(column=0, row=0, sticky='W') 
            
        # Prefix several widgets with self so we can access them during unit testing
        self.button_one = ttk.Button(entries_frame, text="Click Me", command=self.click_event_one)  
        self.button_one.grid(column=0, row=0, sticky='W')
        
        self.entry_one_str = tk.StringVar(value='')      # variable to hold string
        self.entry_one = ttk.Entry(entries_frame, width=20, textvariable=self.entry_one_str)                   
        self.entry_one.grid(column=1, row=0, sticky='W') 
        
        self.button_two = ttk.Button(entries_frame, text="Click Me", command=self.click_event_two)  
        self.button_two.grid(column=0, row=1, sticky='W')                       
        
        self.entry_two_str = tk.StringVar(value='')      # variable to hold string
        self.entry_two = ttk.Entry(entries_frame, width=20, textvariable=self.entry_two_str)                   
        self.entry_two.grid(column=1, row=1, sticky='W')
        
        self.update_label = tk.Label(entries_frame, text='<Label>', height=8)
        self.update_label.grid(column=0, row=2, sticky='W')
               
        # add some padding
        for child in entries_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
    
           
        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(parent, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=3, sticky='W')        
        
        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ",  command=self.run_progressbar).grid(column=0, row=0, sticky='W')  
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop immediately ",   command=self.stop_progressbar).grid(column=0, row=2, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop after second ",  command=self.progressbar_stop_after).grid(column=0, row=3, sticky='W')  
      
        # add some padding
        for child in buttons_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
            
        # Add a Progressbar
        self.progress_bar = ttk.Progressbar(parent, orient='horizontal', length=640, mode='determinate')
        self.progress_bar.grid(column=0, row=4, pady=4, columnspan=2) 
        
        for child in parent.winfo_children():  
            child.grid_configure(padx=8, pady=2) 
                    
    def quit_gui(self):
        self.gui.quit()
        self.gui.destroy()
        sys.exit()
    
    def create_menu(self):              
        menu_bar = Menu(self.gui)            
    
        file_menu = Menu(menu_bar, tearoff=False)               
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_gui)
        
        menu_bar.add_cascade(menu=file_menu, label="File")     
        self.gui.config(menu=menu_bar)    
    
    
    def run_gui(self):
        self.gui.mainloop()                          
    

if __name__ == '__main__':
    gui_instance = GuiOOP()
    gui_instance.run_gui()


















