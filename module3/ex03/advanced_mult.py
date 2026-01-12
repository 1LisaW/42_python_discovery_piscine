#!/usr/bin/python3

i = 0
j = 0
while i <= 10:
    print(f"Table of {i}:", end="")
    while j <= 10:
        res = i * j
        print(f" {res}", end="")
        j += 1
    print("")
    i += 1
    j = 0
