#!/usr/bin/python3

number = (input());
not_zero = "This number is different from zero."
is_zero = "This number is equal to zero."
try:
    if float(number) == 0:
        print(is_zero)
    else:
        print(not_zero)
except:
    print(not_zero)

