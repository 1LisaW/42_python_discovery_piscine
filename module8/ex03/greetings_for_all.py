#!/usr/bin/python3

def greetings(name: str) -> None:
    if not isinstance(name, str):
        print("Error! It was not a name.")
    elif not name:
        print("Hello, noble stranger.")
    else:
        print(f"Hello, {name}.")


greetings('Alexandra')
greetings('Wil')
greetings('')
greetings(42)
