#A  Program to create set. Operations like union, intersection and difference on sets. Add items in sets
"""
Created by @Hrishikesh Salunkhe
"""
set_1 = {1,2,3,4,5}
print(set_1)

# Creating a empty set is little but tricky. Because, it is a Dictionary.
# As we can see below 
# Sets are non-mutable(Cannot ne changed) and Duplicate entries are removed. 
set_2={}
print(type(set_2))
# We can create a empty list by using set() funtion 
set_3=set()
print(type(set_3))

# Now, to combine two dictionaries, union function is used 
set_4 = {1,2,3,4,5}
set_5={4,5,6,7,8,9}
print(set_4.union(set_5))
print(set_4)
print(set_5)
# Here original set is not updated. It will return a new set 

# To get the elements which are present in two sets, 
# Intersection method is used. It will return a new set
print(set_4.intersection(set_5))

# To get elements which are not common in two sets but present in first set,
# defference function is used. Here also, it will retun a new set
print(set_4.difference(set_5))
# Another method is 
print(set_4- set_5)

# issubset method is used to check subset of another set or not
set_6 = {1,3, 5, 7, 9}
set_7={1,3,5}
print(set_6.issubset(set_7))
print(set_7.issubset(set_6))
# Another method for subset is subtraction symbol
print(set_6 < set_7)
print(set_7 <set_6)

# add() method add items to the set
set_8={2,4,6}
set_8.add(8)
print(set_8)

# update() method add items to the set
set_8.update([1,3,5,7])
print(set_8)

# remove() method to remove items from the set