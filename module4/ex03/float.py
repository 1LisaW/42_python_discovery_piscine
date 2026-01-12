#!/usr/bin/python3

usr_number = input("Give me a number: ")

try:
    float_nb = float(usr_number)
    if float_nb % 1 == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except:
    print("Error: Not a number")
