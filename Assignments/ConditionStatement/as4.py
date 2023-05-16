# Program to check if a number is a 3-digit number or not?

num = int(input("Enter number: "))

if num >= 100 and num <= 999:
    print(num, "is 3-digit number")
else:
    print(num, "is not 3-digit number")
