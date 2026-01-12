#!/usr/bin/env python

import sys


def downcase_all(str) -> str:
    return str.lower()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for item in sys.argv[1:]:
            print(downcase_all(item))
    else:
        print("none")
