'''
Created on Mar 5, 2019
@author: Burkhard A. Meier
'''




import unittest
from Section2.Video5_1_GUI_Advanced_oop import GuiOOP


class GuiUnitTests(unittest.TestCase):
    
    def setUp(self):
        print('inside setUp...')
        self.gui_instance = GuiOOP()
    
    def tearDown(self):
        print('inside tearDown...\n')
        self.gui_instance = None
    
    def test_label_default(self):
        label_text = self.gui_instance.update_label.cget('text')
        print('label is:', label_text)
        self.assertEqual(label_text, '<Label>')    # assert <Label>
    
    def test_label_blank(self):     
        self.gui_instance.click_event_one()
        label_text = self.gui_instance.update_label.cget('text')
        print('label is:', label_text)
        self.assertEqual(label_text, '')    # assert ''

# Uncomment: Sanity check        
    def test_label_should_fail(self):     
        self.gui_instance.click_event_one()
        label_text = self.gui_instance.update_label.cget('text')
        print('label is:', label_text)       
        self.assertEqual(label_text, 'a')    # ** this should fail **
     
    def test_label_new_text(self):    
        new_text = 'Test text'
        self.gui_instance.entry_one_str.set(new_text)
        self.gui_instance.click_event_one()
        label_text = self.gui_instance.update_label.cget('text')
        print('label is:', label_text)
        self.assertEqual(label_text, new_text)    # assert new_text
    

#==========================
if __name__ == '__main__':
    unittest.main()
    
    
    