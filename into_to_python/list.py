#A  Program to create lists, and some basic operations
"""
Created by @Hrishikesh Salunkhe
"""

# Create a List. It is created using square bracket
list_1 =[]
print(list_1)

list_2=[1,2,3,4,5]
print(list_2)

#We can enter any kind of data in list
list_3=[1, "Hey",3.0, "What's up" ,5]
print(list_3)

#Now we will access List Items by Index
print(list_3[0])
print(list_3[3])

#Slicing of List
#To print all the elements in the list 
print(list_3[:])
#To print the elements from index 1 to end (Keep in Mind : Indexing always starts from 0 )
print(list_3[1:])
#To print elements for index 0 to index 3
#In slicing, before colon position is starting position of list, and after colon is upto but not included position
print(list_3[:4])


#To delete the elements from list
list_4= [1,2,3,4,5,6,7,8]
print(list_4)
del list_4[0]
print(list_4)

#Concatenation of list
list_6 = ["a", "b", "c"]
list_7 = [1,2,3]
print(list_6 + list_7)

#Multiplication of lists
print(list_7 * 2)