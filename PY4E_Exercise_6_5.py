# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:34:48 2019

6.5 Write code using find() and string slicing 
(see section 6.10) to extract the number at the
 end of the line below. Convert the extracted value 
 to a floating point number and print it out.

@author: Zakochani
"""

#przerobione na kazda liczba na koncu
text = "X-DSPAM-Confidence:    "+ input("wal:");
check = None
lower = None
dlugosc = len(text)
sprawdza = "0123456789"
for i in sprawdza:
    check = text.find(i)
    if lower == None : lower = dlugosc
    if (check < lower and check >0) : lower = check

number = text[lower:]
number_float = float(number)
print(number_float)