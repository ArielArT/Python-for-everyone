# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:24:02 2019
4.6 Write a program to prompt the user for hours and rate per hour using input
 to compute gross pay. Pay should be the normal rate for hours up to 40 and
 time-and-a-half for the hourly rate for all hours worked above 40 hours.
 Put the logic to do the computation of pay in a function called computepay()
 and use the function to do the computation. The function should return
 a value. Use 45 hours and a rate of 10.50 per hour to test the program 
 (the pay should be 498.75). You should use input to read a string and float()
 to convert the string to a number. Do not worry about error checking the 
 user input unless you want to - you can assume the user types numbers
 properly. Do not name your variable sum or use the sum() function.
@author: Zakochani
"""
test = -1

def computepay(h,r):
    pay_normal = h * r
    if(h>40):
        pay_extra = (h - 40) * (r * 0.5)
    if(h>40):    
        pay_all = pay_normal + pay_extra   
    else:
        pay_all = pay_normal
    return pay_all

while(test<0):
    # godziny
    hrs = input("Enter Hours:")
    try:
        float_hrs = float(hrs)
        test = 2
    except:
        print("you put wrong hours !")
    # stawka  
    rate = input("Enter Rate:")
    try:
        float_rate = float(rate)
        test = 2
    except:
        print("you put wrong rate !")

if(test>0):
    p = computepay(float_hrs , float_rate)  
    p = round(p,2) #zaokraglenie do dwoch miejsce po przecinku     
    print("Pay",p)
    
    
