

def add(q,w):
    return q + w

def subtract(q,w):
    return q - w

def multiply(q,w):
    return q * w

def divide(q,w):
    return q // w

print('''Below are 4 options, please pick their letters
        a) add
        b) subtract
        c) multiply
        d) divide
        
After choosing what operation you would like to perform enter the two numbers you would like it done with''')

uc = input("Enter the operation's letter that you would like to perform")

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

if uc == "a":
    z=add(num1 , num2)
    print(num1, "+", num2,"=",z)
elif uc == "b":
    z=subtract(num1 , num2)
    print(num1, "-", num2,"=",z)
elif uc == "c":
    z=multiply(num1 , num2)
    print(num1, '''×''', num2,"=",z)
elif uc == "d":
    z=divide(num1 , num2)
    print(num1, "÷", num2,"=",z)
else:
    print("INVALID INPUT! Read the instructions and try again")