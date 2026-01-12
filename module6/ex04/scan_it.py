#!/usr/bin/python3

import sys
import re
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("none")
    else:
        idx = len(re.findall(sys.argv[1], sys.argv[2]))
        if idx == 0:
            print("none")
        else:
            print(idx)
