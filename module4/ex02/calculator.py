#!/usr/bin/python3

first_number = input("Give me the first number: ")
second_number = input("Give me the second number: ")
try:
    first = int(first_number)
    second = int(second_number)
    print("Thank you!")
    print(f"{first} + {second} = {first + second}")
    print(f"{first} - {second} = {first - second}")
    div = first / second
    if div % 1 == 0:
        div = int(div)
    print(f"{first} / {second} = {div}")
    print(f"{first} * {second} = {first * second}")
except:
    print("Error")

