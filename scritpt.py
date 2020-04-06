from os import rename
import sys
import math


import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Joe"))

response = requests.get("https://google.com")
print(response.status_code)
# name = input('Your name? ')
# print("Hello " + name)
