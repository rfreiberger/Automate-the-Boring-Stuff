# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:00:54 2016

@author: Robert Freiberger 
"""

def collatz(number):
    if number % 2 == 0: # even
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    evenOddLoop(number)
        
def evenOddLoop(number):
    if number == 1:
        print("Done!")
    else:
        collatz(number)
    
print("What is your number?")
try:
    yourNumber = int(input())
    evenOddLoop(yourNumber)

except ValueError:
    print("You did not enter a number.")
