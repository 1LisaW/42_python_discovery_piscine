#!/usr/bin/python3

row_number = input()

try:
    number = float(row_number)
    if number > 0:
        print("This number is positive.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")
except:
    print("Error input. Require only number input")

