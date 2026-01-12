#!/usr/bin/env python


def famous_births(persons: dict) -> None:
    sorted_keys = sorted(persons.keys(), key=lambda x: persons[x]
                         ["date_of_birth"])
    for key in sorted_keys:
        name = persons[key]["name"]
        dob = persons[key]["date_of_birth"]
        print(f"{name} was born in {dob}.")


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}
famous_births(women_scientists)
