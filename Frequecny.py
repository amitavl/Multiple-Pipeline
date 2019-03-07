# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:18:46 2019

@author: AL00470544
"""

"""  
Write a Python program to count the number of characters (character frequency) in a string.  
Sample String : google.com'  
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}       
"""
def char_frequency(str1):
    dict = {}
    for i in str1:
        
        keys = dict.keys()
        
        if i in keys:
            #print(i)
            dict[i] += 1
            #print(dict[i])
        else:
            dict[i] = 1
    return dict
print(char_frequency('google.com'))