#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        amount = len(sys.argv) - 1
        for i in range(1, amount + 1):
            if sys.argv[i].find("ism") == -1:
                print(f"{sys.argv[i]}ism")
    else:
        print("none")
