'''
Created on Mar 5, 2019
@author: Burkhard A. Meier
'''




from Section2.Video5_1_GUI_Advanced_oop import GuiOOP

# Create instance of Gui class
gui_instance = GuiOOP()

# Test 1: Verify default value is displayed
print(gui_instance.update_label.cget('text'))    # assert <Label>

# Test 2: Verify that clicking on button one clears the label to an empty string
gui_instance.click_event_one()
print(gui_instance.update_label.cget('text'))    # assert ''

# Test 3: Verify that entering new text and then clicking the button gets displayed in the label
new_text = 'Test text'
gui_instance.entry_one_str.set(new_text)
gui_instance.click_event_one()
print(gui_instance.update_label.cget('text'))    # assert new_text

# display the gui
gui_instance.run_gui()












