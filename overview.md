# Introduction
For our graph theory project 2020 we were tasked to write a program using Python that can build a non-deterministic finite automaton (NFA) from a regular expression. In simpler terms, I had to create a program that tests a given string and sees if it is a match for a given regular expression. 
I used Thomson's construction to transform my regular expression into a NFA

![thomsonPic](https://i.ibb.co/WfJCR6q/thomson1.png)

When taking in regular expressions, the computer reads the RE's in a different way to humans so for example humans would read a.b (a concatinate b) while computers would read ab.-> I used a shunting yard algorithm to convert human readable RE's (infix notation) into computer readable (postfix notion). 

![shuntingHowTo](https://i.ibb.co/bzVcCzt/shunting2.png)

This was done by seperating the operators from the regular characters and then re-shuffling the regular expression into human readable postfix notation.

![shuntingPic](https://i.ibb.co/5MyDRt3/shunting1.png)

# Run
## To Run the program
- Type 'python3 runner.pi'
- Type regular expression in human readable form (e.g. 'aaa.b')
- Type string to check against regular expression (e.g. 'aaab')
- Alternatively: Type 'python3 runner.py --string1 (regular expression) --string2 (string)'
## Other options:
- Type python3 runner.py --version -> to see the current version of the program
- Type python3 runner.py --info -> to see information about the developer

# Test
Testing was done through multi test assertion which is a debugging aid that tests a condition! If the condition is true, it does nothing and the program just continues to execute. But if the assert condition evaluates to false, it raises an AssertionError exception with an optional error message. So if the expected result for the NFA doesn't match the actual result, there will be an error message.
I added a number of groups of tests by using a test function which contained lists of different test cases which were layed out as follows: 
testType [
  ["regular expression", "string", expected result]
]

![testPic1](https://i.ibb.co/rf2TRxj/test1.png)

I then ran these lists through a loop, asserting each test case and validating them by using the assert keyword (https://www.programiz.com/python-programming/assert-statement)

![testPic2](https://i.ibb.co/4F30T75/test2.png)

# Algorithm
I have 2 python scripts. 1 called regex.py which does all of the calculations, the other called runner.py which is the one that the user runs... this is where to user enters their regular expression and string, these are sent to a function in regex.py which returns whether or not the regex matches the string. 

In regex.py: I have 2 classes containing only constructors, State and Fragment... State represents a state that the NFA is in and it has either 1 or two arrows pointing from it. 

Fragment class represents an NFA fragment and has a start state and an accept state.

After these classes, I have a shunt method. This is basically the shunting yard algorithm... Basically, it takes a regular expression which uses infix notation, easily read by the human eye (eg a.b) and first converts this RE into postfix, which is more easily read by the computer (eg ab.). It does this by turning the infix string into a stack-ish list, looping through the input 1 character at a time, popping a character from the input and adding it to either the new operator stack or the new postfix stack, ensuring that the right symbol is added according to its order in precedence. We then add the operators to the end of the postfix stack and output as a postfix NFA.

The next method created is the compile method, which calls the shunt method! Then, it takes the returned postfix expression, reverses it so that it can be used as part of a stack. It then decides which operator is being used by popping a character from the reversed postfix list, and constructs the relevent state and fragment(s) for that symbol and adds this new fragment onto the NFA Stack.

The next followe(psilon)s method is a method which ensures all of the epsilon edges are followed by the NFA. It does this by using the current state and the state to be checked. It is very important that all epsilon edges are followed.

The match method is the method which implements all of the pre-defined methods and uses them together to check and see if the regular expression fully matches the string (No partial matches, only full matches will be accepted). This function returns true if, and only if the NFA fully matches the string, otherwise it returns false.

Finally, I have a method called Test(), which contains a range of tests consisting of regular expressions, strings and Expected results. The call for the method has been commented out for efficiency purposes, and because it has already been tested and running developer-side tests every time in regex.py would just be very inefficient.


# References
- Python help - (https://www.python.org/) and (https://realpython.com/)
- VI help - (https://linuxacademy.com/blog/linux/vi-short-cuts-for-beginners/ and https://vim.fandom.com/wiki/Copy,_cut_and_paste)
- Thomsons Construction - https://en.wikipedia.org/wiki/Thompson%27s_construction
- Shunting yard algorithm - https://www.youtube.com/watch?v=Wz85Hiwi5MY
- Operator order presedence - https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html
- Taking user input in python - https://www.geeksforgeeks.org/taking-input-in-python/
- Graph Theory module moodle (must have permission to access) - https://learnonline.gmit.ie/course/view.php?id=1599  
- Assert in Python - https://www.programiz.com/python-programming/assert-statement
