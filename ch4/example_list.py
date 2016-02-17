# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 01:16:31 2016

@author: Rob
"""

# Example of chapter 4 project

sandwiches = ['chicken club', 'blt', 'pb and j']

for i in range(len(sandwiches)):
    print('Sandwiches available ' + str(i))
    
# this prints out the following
# Sandwiches available 0
# Sandwiches available 1
# Sandwiches available 2
    
lengthSandwiches = range(len(sandwiches))
print(lengthSandwiches)

# this prints out the following
# range(0,3)

lengthSandwiches2 = len(sandwiches)
print(lengthSandwiches2)