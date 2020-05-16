# Runner for regex.py
# Nathan Garrihy - G00354922
import regex
import argparse

def Run():
    print("Execute regular expression on Strings using Ken Thomson's Construction: ")
    myExp = input("Enter regular expression: ")
    myStr = input("Enter string to check against regular expression (or -1 to exit): ")

    while myStr != "-1":
        if(regex.match(myExp, myStr)):
            print(myExp, " is a match for string: ", myStr)
        else:
            print(myExp, " is not a match for string: ", myStr)
        myStr = input("Enter string to check against regular expression (or -1 to exit): ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False) 

    parser.add_argument("--string1", help="Enter regular expression in human readable form (e.g. aaa.b)")
    parser.add_argument("--string2", help="Enter string to check against regular expression (e.g. aaab)")

    parser.add_argument('-v', '--version', action='version',
                    version='RE checker v1.1', help="Display programs version number")

    parser.add_argument('-i', '--info', action='version',
                    version='Dev= Nathan Garrihy, Student @ GMIT Galway, Graph Theory Project 2020', help="Information about the developer")

    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
            help="||||Option 1: 1: Type python3 runner.pi||"+ 
                    "||2: Enter regular expression in human readable form (e.g. aaa.b)||"+ 
                    "||3: Enter string to check against regular expression (e.g. aaab)||"+
                    "||||Option 2: type python3 runner.py --string1 (regular expression) --string2 (string)||||")

    args = parser.parse_args()
    if(args.string1 != None and args.string2 != None):
        if(regex.match(args.string1, args.string2)):
            print(args.string1, " is a match for string: ", args.string2)
        else:    
            print(args.string2, " is not a match for string: ", args.string2) 
    else:
        Run() 

"""
print("Enter: '--help' / '1' for help on how to use the program") 
print("'regex' / '2' to run the program")
print("'quit' / '-1' to exit)")

choice = "init" # initialization of choice variable
while(choice != "quit" and choice != "-1"):
    print("Please choose an option")
    print("Enter: '--help' / '1' for help on how to use the program") 
    print("'regex' / '2' to run the program")
    print("'quit' / '-1' to exit)")

    choice = input()
    if(choice == "--help" or choice == "1"):
        print("List of things that helps the user")
    elif(choice == "regex" or choice == "2"):
        Run()
    else:
        print("invalid choice")
"""
