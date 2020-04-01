# Runner for regex.py
# Nathan Garrihy - G00354922
import regex

print("Execute regular expression on Strings using Ken Thomson's Construction: ")
print("Valid operators: (+), (.), (*), (|), (?)")
myExp = input("Enter regular expression: ")
myStr = input("Enter string to check against regular expression (or -1 to exit): ")

while myStr != "-1":
    if(regex.match(myExp, myStr)):
        print(myExp, " is a match for string: ", myStr)
    else:
        print(expression, " is not a match for string: ", myStr)
    myStr = input("\nEnter string to check against regular expression (or -1 to exit): ")

