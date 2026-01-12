#!/usr/bin/env python

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[i])
    else:
        print("none")
