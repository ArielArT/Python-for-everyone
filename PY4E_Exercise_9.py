# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:53:40 2019

Write a program that reads the words in words.txt and stores them as keys in
 a dictionary. It doesn't matter what the values are. Then you can use the
 in operator as a fast way to check whether a string is in the dictionary.
"""

file = input("Enter file name:")
open_file = open(file)

dictionary = dict()
count = 0

for line in open_file:
    words = line.split()
    for word in words:
        if not word in dictionary :
            dictionary[word] = 1
        else : dictionary[word] = dictionary[word] + 1
            
print (dictionary)

#%% Exercise 9.2
"""
Exercise 2: Write a program that categorizes each mail message by which day 
of the week the commit was done. To do this look for lines that start with 
"From", then look for the third word and keep a running count of each of 
the days of the week. At the end of the program print out the contents of 
your dictionary (order does not matter).
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
"""
dictionary = dict()

file = input("Enter file name:")
try:
    open_file = open(file)
except:
    print("wrong name")
    exit()
    
for line in open_file:
    words = line.split()
    if len(words) > 2 and words[0] == "From" :
        if not words[2] in dictionary:
            dictionary[words[2]] = 1
        else:
            dictionary[words[2]] = dictionary[words[2]] + 1

print(dictionary)


#%% Exercise 9.3
"""
Exercise 3: Write a program to read through a mail log, build a histogram 
using a dictionary to count how many messages have come from each email 
address, and print the dictionary.
"""

dictionary = dict()

file = input("Enter file name:")
try:
    open_file = open(file)
except:
    print("wrong name")
    exit()
    
for line in open_file:
    words = line.split()
    if len(words) > 2 and words[0] == "From" :
        if not words[1] in dictionary:
            dictionary[words[1]] = 1
        else:
            dictionary[words[1]] = dictionary[words[1]] + 1

print(dictionary)

#%% Exercise 9.4
"""
Add code to the above program to figure out who has the most messages in the
 file. After all the data has been read and the dictionary has been created, 
 look through the dictionary using a maximum loop (see Chapter 5: Maximum and 
 minimum loops) to find who has the most messages and print how many messages
 the person has.
"""

dictionary = dict()

file = input("Enter file name:")
try:
    open_file = open(file)
except:
    print("wrong name")
    exit()
    
for line in open_file:
    words = line.split()
    if len(words) > 2 and words[0] == "From" :
        if not words[1] in dictionary:
            dictionary[words[1]] = 1
        else:
            dictionary[words[1]] = dictionary[words[1]] + 1
email_max = None
maximum = None
for email,count in dictionary.items():
    if maximum == None or count > maximum :
        maximum = count
        email_max = email

email_min = None
minimum = None
for email,count in dictionary.items():
    if minimum == None or count < minimum :
        minimum = count
        email_min = email    

print(email_max,maximum)

#%% Exercise 9.5
"""
This program records the domain name 
(instead of the address) where the message was sent 
from instead of who the mail came from (i.e., the whole email address).
 At the end of the program, print out the contents of your dictionary.
"""

dictionary = dict()

file = input("Enter file name:")
try:
    open_file = open(file)
except:
    print("wrong name")
    exit()
    
for line in open_file:
    words = line.split()
    if len(words) > 2 and words[0] == "From" :
        word = words[1]
        #print(word)
        number = word.find("@")
        domain = word[number:]
        if not domain in dictionary:
            dictionary[domain] = 1
        else:
            dictionary[domain] = dictionary[domain] + 1
  

print(dictionary)



