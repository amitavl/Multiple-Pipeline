# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:53:26 2019

@author: AL00470544
"""

import monkey
def monkey_fun(self):
    print("in monkey fun being called")
    
monkey.A.fun=monkey_fun
obj=monkey.A()
print(obj)
obj.fun()