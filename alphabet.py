string = "123abc456"
if any(char.isalpha() for char in string):
    print("The string contains alphabetic characters.")
else:
    print("The string does not contain any alphabetic characters.")