#A  Program for operations on list
"""
Created by @Hrishikesh Salunkhe
"""

#Create a nested list i.e. List in a list
list_1=[1,2,3,[5,6,7]]
print(list_1)

#Access a elements from nested list
print(list_1[3])
#To access element 5 (0th index from list which is inside of list_1) 
print(list_1[3][0])
print(list_1[3][2])

#Count function on list
list_2= [1,2,3,4,1,4,2,5,7,1,6,3,6,7,1,5,7,8,9,2]
print(list_2.count(1))

#To append a element in a list(Keep in Mind : We can add only one element at a time. 
# We can add a list at the end with any number of elements. 
# We add elements at end only using append function  )
print(list_2)
list_2.append(10)
print(list_2) 

#To add element at any position  'insert' function is used
# We can add element at any position
print(list_2)
list_2.insert(2,12)
print(list_2)

# To remove element from any position 'remove' function is used
# (Keep in mind: It will delete only element which is occurred first)
print(list_2)
list_2.remove(2)
print(list_2)

#To remove element from any position , 'pop' function is used
#we have to pass index of element  which we want to delete
print(list_2)
list_2.pop(2)
print(list_2)

#To sort elements , 'sort' function is used
#Keep in Mind: Here, oiginal list is modified
print(list_2)
list_2.sort()
print("List using 'sort' method" ,list_2)
#If we want don't want to modify then use 'sorted' method
list_3 = sorted(list_2)
print("List using 'sorted' method", list_3)

# Use of reverse function
list_3.reverse()
print(list_3)