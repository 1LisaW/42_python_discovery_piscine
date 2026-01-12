#!/usr/bin/python3


numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for i in range(0, len(numbers)):
    if numbers[i] > 5:
        new_set.add(numbers[i] + 2)
print(numbers)
print(new_set)
