# A python program for Scripts and modules
"""
Created by @Hrishikesh Salunkhe
"""
var_1=5
def add(v_list):
    c=0
    for i in range(len(v_list)):
        c += v_list[i]
    return c
list_1=[1,2,3,4,5]
print(add(list_1))
