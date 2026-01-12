#!/usr/bin/python3
numeric_input = input("Enter a number less than 25\n")
try:
    start_number = int(numeric_input)
    if start_number >= 25:
        raise Exception("Error")
    i = start_number
    while i <= 25:
        print(f"Inside the loop, my variable is {i}")
        i += 1
except:
    print("Error")
