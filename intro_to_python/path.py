#A  Program to know the path
"""
Created by @Hrishikesh Salunkhe
"""
import os
from os import path
print(os.name)
print(path.exists("demofile.txt"))
print(path.isfile("demofile.txt"))
print(path.isdir("demofile.txt"))
print(path.realpath("demofile.txt"))