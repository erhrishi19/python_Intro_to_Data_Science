#A  Program to create tuples. Operations like union, intersection and difference on sets. Add items in sets
"""
Created by @Hrishikesh Salunkhe
"""

# Create a empty tuple 
tup_1 = tuple()
print(type(tup_1))

tup_2 = (1,2,3,4,5)
print(type(tup_2))

# Concatenation of Tuples
tup_3 = (1,2,3,4)
tup_4 =('apple','ball')
print(tup_3 + tup_4)

# Nesting of tuples
tup_5 = (tup_3,tup_4)
print(tup_5)

#Repitition of Tuples
tup_6 = ('python \n')*5
print(tup_6)

# Tuples are immutable (unchangeable), unordered.
#Slicing a tuple
tup_7=(1,2,3,4,5,6,7,8)
print(tup_7[::1])

# To delete tuple, del function is used
tup_8=(1,2,3)
del tup_8

