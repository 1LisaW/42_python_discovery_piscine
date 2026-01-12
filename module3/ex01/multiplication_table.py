#!/usr/bin/python3

user_number = input("Enter a number\n")
try:
    number = int(user_number)
    for i in range(0, 10):
        result = i * number
        print(f"{i} x {number} = {result}")
except:
    print("Error")
