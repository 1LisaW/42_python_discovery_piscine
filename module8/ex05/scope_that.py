#!/usr/bin/env python

def add_one(num: int) -> int:
    num += 1
    return num


variable = 10
print(variable)
print(add_one(variable))
print(variable)  # Should still be 10
