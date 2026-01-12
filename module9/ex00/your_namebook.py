#!/usr/bin/env python


def array_of_names(dict_of_people: list[dict[str, str]]) -> list[str]:
    names = []
    for person in dict_of_people:
        # if 'name' in person:
        first_name = person.capitalize()
        last_name = dict_of_people[person].capitalize()
        names.append(f"{first_name} {last_name}")
    return names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))
