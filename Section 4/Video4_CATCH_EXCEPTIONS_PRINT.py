'''
Created on Mar 11, 2019
A big Thanks to James Mukuya
@author: Burkhard A. Meier
'''






# Simply import this module into your Python/PyQt5 module to catch exceptions

import sys
from PyQt5 import QtWidgets

 
def catch_exceptions(t, val, tb):
    '''Catch any exceptions and display in QMessage box
       t=exception type
       val=exception value
       tb=traceback
    '''   
   
    QtWidgets.QMessageBox.critical(None,'An Exception was Raised',
                                   'Value: {}'.format(val))
    old_hook(t, val, tb) 
          
old_hook = sys.excepthook

sys.excepthook = catch_exceptions       # this sets up the hook to catch any uncaught exceptions










