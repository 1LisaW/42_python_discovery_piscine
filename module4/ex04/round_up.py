#!/usr/bin/python3

usr_number = input("Give me a number: ")
try:
    nb_fl = float(usr_number)
    nb_int = int(nb_fl)
    if nb_int < nb_fl:
        nb_int += 1
    print(nb_int)
except:
    print("Error: Not a number")
