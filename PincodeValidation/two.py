pincode_list = ('560084', '560001', '560043',
                '560074', '560053', 'devkum', '#$%123')


def validate_pincode(pincode):
    if pincode in pincode_list:
        return True
    else:
        return False


pincode = input("Enter your pincode: ")
if validate_pincode(pincode):
    print("congrats! you have enterd valid pincode")
else:
    print("sorry! you have entered invalid pincode")
