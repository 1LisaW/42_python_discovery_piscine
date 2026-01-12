#!/usr/bin/python3

password = "Python is awesome"
users_password = input()
success_response = "ACCESS GRANTED"
fail_response = "ACCESS DENIED"

if users_password == password:
    print(success_response)
else:
    print(fail_response)
