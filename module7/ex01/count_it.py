#!/usr/bin/python3

import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        amount = len(sys.argv) - 1
        print(f"parameters: {amount}")
        for i in range(1, amount + 1):
            print(f"{sys.argv[i]}: {len(sys.argv[i])}")
    else:
        print("none")
