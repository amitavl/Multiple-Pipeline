# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:16:37 2019

@author: AL00470544
"""

import unittest
from basicfunction import BasicFunction
 
class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.func = BasicFunction()
 
    def test_1(self):
        self.assertTrue(True)
 
    def test_2(self):
        self.assertTrue(True)
 
    def test_3(self):
        self.assertEqual(self.func.state, 0)
 
    def test_4(self):
        self.func.increment_state()
        self.assertEqual(self.func.state, 1)
 
    def test_5(self):
        self.func.increment_state()
        self.func.increment_state()
        self.func.clear_state()
        self.assertEqual(self.func.state, 0)
 
if __name__ == '__main__':
    unittest.main()