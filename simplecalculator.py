#Simple Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b != 0:
        return a/b
    else:
        print("undefined")

print("select operation: '+', '-', '*', '/' ")
c= input("enter operator: ")
a= float(input("Enter first number"))
b= float(input("Enter Second number"))
if c== '+':
    print(add(a,b))
elif c== '-':
    print(sub(a,b))
elif c== '*':
    print(mul(a,b))
elif c== '/':
    print(div(a,b))
else:
    print("invalid operator")