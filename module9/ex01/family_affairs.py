#!/usr/bin/python3


def find_the_redheads(family: dict) -> list:
    filtered_members = filter(lambda member: family[member] == "red", family)
    return list(filtered_members)


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))
