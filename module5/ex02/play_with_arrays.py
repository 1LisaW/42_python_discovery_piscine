#!/usr/bin/python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
modified_array = []

for i in range(0, len(numbers)):
    if numbers[i] > 5:
        modified_array.append(numbers[i] + 2)
print(numbers)
print(modified_array)
