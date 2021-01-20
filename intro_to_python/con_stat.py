# A python program for conditional statement. 
"""
Created by @Hrishikesh Salunkhe
"""
age = 18
# if block executed when condition is True
if age > 18:
    print("You can Vote")
    
# elif block executed when condition is True
elif age<0:
    print("Invalid age")

# else block is executed when none of if and elif block is executed
else:
    print("You are too young")
    
list_1 = [12,23,34,45,56]
num = 11
if num in list_1:
    print("Yes")
num_2=23
if num_2 in list_1:
    print("Yes")