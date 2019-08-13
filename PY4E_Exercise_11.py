# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:13:41 2019

@author: Zakochani
Write a simple program to simulate the operation of the grep command on Unix. 
Ask the user to enter a regular expression and count the number of lines that
 matched the regular expression:

$ python grep.py
"""
import re

# dane od uzytkownika
plik = input("Enter file name:")
try:
    file = open(plik)
except:
    print("wrong name")
    exit()
    
szukaj = input("Enter expresion :")

#szukanie i liczenie lini z fraza
count =0
for line in file:
    if re.search(szukaj,line):
        count = count +1
        
print(plik , "had" , count, "lines that matched",szukaj)

#%% Exercise 11.2 Nie kumam co mam szukać ?

"""
Write a program to look for lines of the form
"""
import re

# dane od uzytkownika
plik = input("Enter file name:")
try:
    file = open(plik)
except:
    print("wrong name")
    exit()
    
szukaj = 

#szukanie i liczenie lini z fraza
count =0
for line in file:
    if re.search(szukaj,line):
        count = count +1
        
print(plik , "had" , count, "lines that matched",szukaj)

#%% 11.3
"""
Extract the number from each of the lines using a regular expression and 
the findall() method. Compute the average of the numbers and print 
out the average
"""
import re

lista=list()
znalazl = None
suma1 =0
suma2 = 0
suma = 0
count = 0
# dane od uzytkownika
plik = input("Enter file name:")
try:
    file = open(plik)
except:
    print("wrong name")
    exit()
    
for line in file:
    znalazl = re.findall(r"\d+",line)
    lista.append(znalazl)

for line in lista:
    if line == []:
        continue
    elif len(line) < 2:
        liczba = float(line[0])
        suma1 = suma1 + liczba
        count = count +1
    elif len(line) > 1:
        for lb in line:
            liczba = float(lb)
            suma2 = suma2 + liczba
            count = count +1
suma = suma1 + suma2            
print(suma)










