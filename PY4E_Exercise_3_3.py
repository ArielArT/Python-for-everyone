# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:08:17 2019

@author: Zakochani

3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
"""
#zmienne uzywane
test = -1

while(test<0):
    print("Please input a score from 0.0 to 1.0")
    score = input("Enter Score: ")
    
    try:
        float_score = float(score)
        if(float_score >= 0 and float_score <= 1):
            test = 2
        else:
            print("Wrong score - out of range !")
    except:
        print("does it not a numeric number !")
    if(test>0):
        if(float_score >= 0.9):
            print("You have grade A")
        elif(float_score >= 0.8):
            print("You have grade B")
        elif(float_score >= 0.7):
            print("You have grade C")
        elif(float_score >= 0.6):
            print("You have grade D")
        elif(float_score < 0.6):
            print("You have grade F")
              
print("END")              