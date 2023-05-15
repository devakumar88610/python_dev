# variables
x = 3
y = 5

# if condition
if x > y:
    print("x is greater than", y)  # True

# if else condition
if x > y:
    print("x is greater than", y)
else:
    print("x is less than", y)  # False

# elif condition
marks = int(input("Enter your Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade E")
elif marks >= 50:
    print("Grade D")
else:
    print("Grade F")
