# Program to print the least/small number is given two numbers?

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    print(num1, "is smallest than", num2)
elif num2 < num1:
    print(num1, "is not smallest than", num2)
else:
    print(num1, "is equal to", num2)
