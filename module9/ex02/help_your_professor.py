#!/usr/bin/python3


def average(grades: dict[str, int]) -> float:
    if len(grades) == 0:
        return 0.0
    total = sum(grades.values())
    return total / len(grades)


class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
