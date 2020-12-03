#A  Program to create dictonaries, functions in Dictionaries. 
"""
Created by @Hrishikesh Salunkhe
"""

#Combine two dictionaries
dict_1={"a" :65, "b":66, "c":67}
dict_2={"d":68, "e":69,"f":70}
dict_3={}
dict_3["dict_1"]=dict_1
dict_3["dict_2"]=dict_2
print(dict_3)

#Add values in Dictionaries
dict_1["c"] += 1
print(dict_1)

#Access values of Dictionaries
print(dict_1["a"])
#We can access values of Dictionaries with get funtion
print(dict_1.get("a"))
#'get' function is more useful than direst access
# where we want to display a custom message, when a key-value does not exists in Dictionary
print(dict_1.get("d","Key does not exists"))     

#To delete key-value pair from Dictionary, 'pop' functionis used
# Keep in mind: It takes argument as key and optional customized message if  key not found in Dictionary. 
# And it will return value of key-value pair if present in Dictionary 
dict_1["pop"]=17
print(dict_1)
print(dict_1.pop("pop"))
print(dict_1)
# 'del' function is also used to dele a key-value pair from Dictioanry
dict_1["pop"]=18
print(dict_1)
del dict_1["pop"]
print(dict_1)

#To update the values of Dictionary
dict_4 ={"apples":14, "banana":12}
dict_5 ={"apples":20, "tomatoes":12}
dict_4.update(dict_5)
print(dict_4)

#To get all the keys in Dictionary use 'keys' function
print(dict_4.keys())
#To get all the values in Dictionary use 'values' function
print(dict_4.values())

