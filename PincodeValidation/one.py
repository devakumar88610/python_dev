import re


def val_pincode(pincode):
    regex = re.compile(r'^\d{6}$')

    if regex.match(pincode):
        return True
    else:
        return False


pincode_list = ['560084', '560001', '560043',
                '560074', '560053', '000', '*25#85' 'devkum']
user_input = input("Enter your pincode: ")

if val_pincode(user_input):
    if user_input in pincode_list:
        print("perfect! you have enterd valid pincode")
    else:
        print("sorry! you have entered invalid pincode")
else:
    print("pls enter 6 digit code")
