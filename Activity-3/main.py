# Program make a simple calculator
# This function add two numbers def add(x,y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x- y
# This function multiplies two numbers
def multiplies(x, y):
    return x * y
# This function divides two numbers
def divides(x, y):
    return x / y
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
print("Sum :", add(num1, num2))
print("Differences :"subtract(num1, num2))
print("Product :"multiply(num1, num2))
print("Quotient :"divide(num1, num2))
