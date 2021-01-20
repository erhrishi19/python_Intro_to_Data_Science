#A  Program to create file 
"""
Created by @Hrishikesh Salunkhe
"""
f = open('demofile.txt', 'w+')
str_1= "Hey there, Welcome to the world of Python"
f.write(str_1)
print(f.read())
f.close()
f= open('demofile.txt','r')
print(f.read())
f.close()