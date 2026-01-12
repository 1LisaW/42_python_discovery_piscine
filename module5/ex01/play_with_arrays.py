#!/usr/bin/python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
modified_array = numbers.copy()
for i in range(0, len(modified_array)):
    modified_array[i] += 2
print(f"Original array: {numbers}")
print(f"New array: {modified_array}")


