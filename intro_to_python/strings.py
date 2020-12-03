# A Program to create  string  variable, and oprations on strings 
"""
Created by @Hrishikesh Salunkhe
"""

#create a string variable
string_1 = "Hello Python!"
print(string_1)

#We can perform Concatenation operation on string
string_2 = "Hello" + "World!"
print(string_2)

# Multiplication on strings
string_3= string_1*2
print(string_3)

#spilt operation to spilt a string
print(string_3.split())

#We can split the string by passing some valid attributes like comma in below example
string_4= "a, b, c, d, e"
print(string_4.split(","))

#We can join two strings
string_5 ="a"
print(string_5.join(string_4))

#We can replace a string, convert into upper case as well as lower case, and strip the string
string_6 = "   Hello World   "
print(string_6.strip())
print(string_6.upper())
print(string_6.lower())

#To strip from left and right side of the string we use
print(string_6.lstrip())
print(string_6.rstrip())

#To calculate the length of string
print(len(string_6))