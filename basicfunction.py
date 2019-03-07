# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:17:38 2019

@author: AL00470544
"""

class BasicFunction(object): 
    def __init__(self): 
        self.state = 0
 
    def increment_state(self): 
        self.state += 1
 
    def clear_state(self): 
        self.state = 0