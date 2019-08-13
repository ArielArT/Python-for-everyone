

#zadanie 8.1 
"""
Write a function called chop that takes a list and modifies it, 
removing the first and last elements, and returns None. Then write a 
function called middle that takes a list and returns a new list that 
contains all but the first and last elements
"""
def chop(list):
    x = len(list)
    del list[x-1]
    del list[0]

lista = [ 'a', 'b', 'c', 'd', 'e']
print(lista)
print("funkcja chop")

chop(lista)
print(lista)

#%% zadanie 8.2 zmodyfikowac plik aby wyrzucal blad 
"""
print(words[2]) ... wystarczy ze po From bedzie za malo elementow 
trzbea zmienic 
if len(words) == 0 : continue
na
if len(words) < 3 : continue

"""

fhand = open('mbox-short2.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words)<3 : continue
    if words[0] != 'From' : continue
    print(words[2])
    
#%% 8.3 zmodyfikuj aby byla jedna instrukcja if
    
  fhand = open('mbox-short2.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words)>3 and words[0] == 'From' :
        print(words[2])  
    
#%% zadanie 8.4
"""
 czytaj plik romeo i stworzi liste wystepujacych wyrazow
 posortowana alfabetycznie, wyrazy nie moga sie powtarzac
 """
lista = list() 
 
plik = input("Enter file name : ")
dane = open(plik)

for ln in dane:
    linia= ln.split()
    if len(linia) == 0 : continue
    if lista == []: lista.append(linia[0])
    for check in linia:
        if not check in lista : lista.append(check)
        
lista.sort()
print("oto nasza lista" ,lista)

#%% 8.5
"""
Write a program to read through the mail box data and when you find line 
that starts with "From", you will split the line into words using the split
 function. We are interested in who sent the message, which is the second 
 word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

You will parse the From line and print out the second word for each From 
line, then you will also count the number of From (not From:) lines and print
 out a count at the end. This is a good sample output with a few lines removed
"""
#otwarcie dokumentu
plik = input("Enter file name: ")
dane = open(plik)

count = 0

for line in dane:
    ln = line.split()
    if len(ln) > 2 and ln[0] == "From":
        count = count + 1
        print(ln[1])

print("\nThere were" , count , "lines in the file with From as the first word")    


#%% Exercise  8.6
"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers 
and prints out the maximum and minimum of the numbers at the end when the user 
enters "done". Write the program to store the numbers the user enters in a 
list and use the max() and min() functions to compute the maximum and minimum 
numbers after the loop completes
"""
lista = list()

while True:
    wejscie = input("Podaj liczbe: ")
    if wejscie == "done" : break
    try:
        liczba = int(wejscie)
    except:
        print("tylko liczby calkowite")
        continue 
    lista.append(liczba)

print(lista)
print(" najwieksza liczba to:",max(lista))
print(" najmniejsza liczba to:",min(lista))

















