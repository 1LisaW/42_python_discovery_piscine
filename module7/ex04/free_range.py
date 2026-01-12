#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            if start >= end:
                print("none")
                sys.exit()
            array = list(range(start, end + 1))
            print(array)
        except ValueError:
            print("none")
            sys.exit()
    else:
        print("none")
