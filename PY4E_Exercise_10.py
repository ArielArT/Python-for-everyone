# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:16:39 2019

@author: Zakochani
"""

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
print(t)
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)

print(res)

#%% Exercise 10.1
"""
Revise a previous program as follows: Read and parse the "From" lines and4
 pull out the addresses from the line. Count the number of messages from 4
 each person using a dictionary
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

lista = list()
for k,v in (dictionary.items()):
    lista.append((v,k))

lista.sort(reverse=True)

value, name = lista[0]
print(name, value)


#%% Exercise 10.2
"""
This program counts the distribution of the hour of the day for each of the 
messages. You can pull the hour from the "From" line by finding the time 
string and then splitting that string into parts using the colon character.
 Once you have accumulated the counts for each hour, print out the counts, 
 one per line, sorted by hour as shown below.
 
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
    if len(words) > 5 and words[0] == "From" :
        time = words[5]
        hours = time.split(":")
        hour = hours[0]
        if not hour in dictionary:
            dictionary[hour] = 1
        else:
            dictionary[hour] = dictionary[hour] + 1

lista = list()
for k,v in (dictionary.items()):
    lista.append((k,v))

lista.sort()

for k,v in lista:
    print(k,v)


#%% 10.3

"""
Write a program that reads a file and prints the letters in decreasing order
 of frequency. Your program should convert all the input to lower case and 
 only count the letters a-z. Your program should not count spaces, digits,
 punctuation, or anything other than the letters a-z. Find text samples 
 from several different languages and see how letter frequency varies between 
 languages.
"""

import string 


dictionary = dict()
znaki = ['(', ')', '?', ':', ';', ',', '.', '!', '/', ' ', '@']



def sprawdz(letter):
    if letter in list(string.ascii_lowercase):
        if not letter in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] = dictionary[letter] + 1 
        

file = input("Enter file name:")

open_file=open(file)
try:
    open_file = open(file)
except:
    print("wrong name")
    exit()

for line in open_file:
    words = line.split()
    for word in words:
        wyraz = word.lower()
        if len(wyraz) > 1:
            for letter in wyraz:
                sprawdz(letter)     
        else:
            sprawdz(wyraz) 


lista = list()
for k,v in (dictionary.items()):
    lista.append((k,v))

lista.sort()

for k,v in lista:
    print(k,v)



