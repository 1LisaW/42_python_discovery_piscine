#!/usr/bin/env python

import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("none")
    else:
        user_input = input("What was the parameter? ")
        if user_input == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")
