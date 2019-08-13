# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:01:28 2019

@author: Zakochani
"""

# Kurs PY4E

print("Hello ")

hrs = "A"
rate = "A"
error_rate = 0
error_hrs = 0
pay = -1
float_hrs = 0
float_rate = 0


#M dzialac az bedzie prawidlowy wynik
while (pay <0):
    
    # Podanie ilosci godzin
    hrs = input("Enter Hours:")
    try:
        float_hrs = float(hrs)
        error_hrs = 2
    except:
        error_hrs = 1
    
    #Wpisanie stawki za godzine
    rate = input("Enter your rate: ")

    try:
        float_rate = float(rate)
        error_rate = 2
    except:
        error_rate = 1
        
    if (error_rate != 1 and error_hrs != 1):
        pay = float_hrs * float_rate
        pay = round(pay,2)
        print("Your paymant is" , pay , "zlociszy")
        #print("Your salary is:" , "%.2f" % pay)
    elif (error_hrs ==1 and error_rate == 1):
        print("you put every thing wrong !!")
    elif (error_hrs ==1):
        print("you put wrong hours")
    elif (error_rate == 1):
        print("you put wrong rate")

    
    
print("The end")
input("Press Enter to continue...")

