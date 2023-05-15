import re


def validate_pincode(pincode):
    regex = re.compile(r'^\d{6}$')

    if regex.match(pincode):
        return True
    else:
        return False


pincode_list = ['560084', '560001', '560043', '560074', '560053']
user_input = input("Enter your pincode: ")

if validate_pincode(user_input):
    if user_input in pincode_list:
        print("congrats! you have entered valid pincode")
    else:
        print("sorry! you have entered invalid pincode")
else:
    print("enter 6 digit code")
