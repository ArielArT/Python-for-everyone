# -*- coding: utf-8 -*-
#%% Exercise 7.1
"""
Created on Thu Apr  4 21:24:13 2019
Write a program to read through a file and print the contents of 
the file (line by line) all in upper case.
@author: Zakochani
"""
file = input("Enter the file name :" )

try:
    open_file = open(file)
except:
    print("problem with file", file)
    quit()
    exit()
for line in open_file:
    line=line.strip()
    print(line)
    
print ("The end")

#%%Exercise 7.2

"""
rite a program to prompt for a file name, and then read through the file
 and look for lines of the form:

X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with "X-DSPAM-Confidence:" 
pull apart the line to extract the floating-point number on the line.
 Count these lines and then compute the total of the spam confidence 
 values from these lines. When you reach the end of the file, print out 
 the average spam confidence.

"""
file = input("Enter file name :" )

try:
    open_file = open(file)
except:
    print("problem with open file")
    exit()

count = 0  
sum_avarage = 0  
#szukanie "X-DSPAM-Confidence:"
for line in open_file:
    line.strip
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    zmienna = line.split()
    try:
        avarage = float(zmienna[1])
    except:
        print("problem z float")
        exit()
    sum_avarage = sum_avarage + avarage

wynik = sum_avarage / count
print("Average spam confidence:",wynik)
            
#%% Exercise 7.3
"""
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
 they add a harmless Easter Egg to their program Modify the program that 
 prompts the user for the file name so that it prints a funny message when 
 the user types in the exact file name "na na boo boo". The program should
 behave normally for all other files which exist and don't exist. Here is
 a sample execution of the program:
"""


file = input("Enter file name :")
try:
    open_file = open(file)
except:
    if file == "na na boo boo": #fragment z na na boo boo
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()

    print("problem with open file")
    exit()
    
for line in open_file:
    count = count + 1  
    
print("There were", count , " subject lines in " , file)

#%%

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)




