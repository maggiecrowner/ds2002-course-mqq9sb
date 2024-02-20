#!/opt/anaconda3/bin/python3

import os

os.environ["FAV_COLOR"] = "Pink"
os.environ["NAME"] = "Maggie"
os.environ["MAJOR"] = "Statistics"

FAV_COLOR = input("What is your favorite color? ")
NAME = input("What is your name? ")
MAJOR = input("What is your major? ")

print(os.getenv("FAV_COLOR"))
print(os.getenv("NAME"))
print(os.getenv("MAJOR"))
