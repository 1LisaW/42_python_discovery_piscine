#!/usr/bin/env python

import sys


def shrink(s: str) -> None:
    print(s[0:8:1])


def enlarge(s: str) -> None:
    new_str = s
    while len(new_str) < 8:
        new_str += "Z"
    print(new_str)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            if len(item) < 8:
                enlarge(item)
            else:
                shrink(item)
    else:
        print("none")
