#!/usr/bin/python
import random

print("hello whats your name")
name = raw_input()  #this is specific for python 2.7 

print("hello " + name + "lets play game to guess number between 1 to 20 ")

secretnum = random.randint(1,20)

print('secret number :', secretnum)

for turn in range(1, 7):

        print("enter a number ")
        num = raw_input()
        num = int(num)
        if num < secretnum :
                print(" you have enter too low")
        elif num > secretnum:
                print(" your number is too high")
        else:
                break
if num == secretnum:
        print(" well done , you have guess correctly")
else:
        print(" you have exceed the try , my number is ",secretnum)
