# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:37:55 2019

5.2 Write a program that repeatedly prompts a user for integer numbers 
until the user enters 'done'. Once 'done' is entered, print out the
 largest and smallest of the numbers. If the user enters anything other
 than a valid number catch it with a try/except and put out an appropriate
 message and ignore the number. Enter 7, 2, bob, 10, and 4 and 
 match the output below.
 
@author: Zakochani
"""

largest = None
smallest = None
numbers = []

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    
    try :
        num_int = int(num)
    except :
        print("wrong number")
        continue
    numbers.append(num_int)

largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if largest < i:
        largest = i
    if smallest > i:
        smallest = i
            
print("Maximum", largest)
print("Minimum",smallest)