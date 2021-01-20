# A python program for functions 
"""
    Created by @Hrishikesh Salunkhe
"""
# Let's create a basic calculator using functions

a = int(input("En1ter a First number:"))
b = int(input("Enter a Second number:"))
# input method alwaays returns a string so we need to convert user input in required format

# Let's define a function
# Function Definition-> def function_name(Parameters):
def calculator(a,b):
    print("Addition ",a+b)
    print("Subtraction",a-b)
    print("Multiplication",a*b)
    print("Division",a/b)
    print("Modulo",a%b)
    print("Power",a**b)

calculator(a,b)


# Now see a function with return
def cal(a,b):
    return a+b
sum= cal(a,b)
print(sum)

# When we don't know numbe of parametes to be passed to a function
# Variable Length parameters are used. 
# These are arguments that can take an unspecified amount of input. 

def average(*args):
    sum=0
    for i in args:
        sum += i
    total= len(args)
    Average=sum/total
    print("Average is :",Average)
    
average(10,12,23,34,56,76,3,4,1,4)
average(4,8,15,16)
average(3,5)


def main():
    print("Main function executed")

# The reason we use below code is to execute our file as own program.
# It is useful when we import these module in another program

if __name__ == "__main__":
    main()