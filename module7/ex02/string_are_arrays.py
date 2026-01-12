#!/usr/bin/env python

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        amount = 0
        for char in sys.argv[1]:
            if char == 'z':
                amount += 1
                print("z", end='')
        if amount == 0:
            print("none")
        else:
            print()
    else:
        print("none")
