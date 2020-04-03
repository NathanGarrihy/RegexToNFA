Project:
Thomson's Construction in Python - Graph Theory 2020 - G00354922

Project Description:
The goal for this project is to write a program in the Python programming language that can
build a non-deterministic finite automaton (NFA) from a regular expression,
and can use the NFA to check if the regular expression matches any given
string of text.

Research:
Before really attempting this project, I watched the various associated videos which our lecturer uploaded to moodle as well as taking a good look at (https://www.python.org/) and (https://realpython.com/) since I had not done python before, I tried to understand how it worked when compared to other programming languages I had previously worked with. All of the code was done through VI using google cloud platform and this was also new to me so I was able to find a couple websites that made working with VI a lot easier, they are (https://linuxacademy.com/blog/linux/vi-short-cuts-for-beginners/ and https://vim.fandom.com/wiki/Copy,_cut_and_paste)

The first task was to fully understand Thomson's construction and how it works as well as the shunting yard algorithm... Most of this was clearly explained in the practical videos our lecturer put on moodle but I still had to do a little bit of online research just to make things clear for myself... I found some very useful information on Thomson's construction on the wikipedia page (https://en.wikipedia.org/wiki/Thompson%27s_construction), while I know wikipedia isn't always the most reliable source, I was able to compare the information on the wiki page with the information my lecturer provided me to develop a better understanding of Thomsons construction and how it transforms a RE into a NFA.

For the shunting yard algorithm, fortunately I didn't really find to be too difficult to get my head around how it works with thanks to the 2 videos my lecturer put on learnonline, these really helped as they clearly explained the process of the shunting yard algorithm. I also found a great youtube video which spells it out as clear as day here: (https://www.youtube.com/watch?v=Wz85Hiwi5MY)

Aside from the stuff that we were taught by our lecturer, I didn't have a whole lot of research to do by myself in order to complete the project... The main research I did was to find the orders of precedence for the symbols used for the regular expressions, since I was adding a + symbol (one or more) and a ? symbol (None or one) and did not know where they occured in precedence... Thankfully I found a resource which perfectly explained anything I needed to know about order of precedence here (https://www.gnu.org/software/gcal/manual/html_node/Regexp-Operators.html). I found that the '*', '+' and '?' operators have highest precedence followed by (.) concat and (|) or.
I also decided to make a file to take in user input and allow them to see if a RE matches a NFA... Since I had no background in python I had to look this up online but found a perfect solution easily enough here (https://www.geeksforgeeks.org/taking-input-in-python/)
Precedence orders found & symbols used (7 = highest precedence, 1 = lowest) '*' : 7, '+' : 6, '?':5, '.': 4, '|': 3, ')' : 2, '(' : 1  

How my code works:
I have 2 python scripts. 1 called regex.py which does all of the calculations, the other called runner.py which is the one that the user run's... this is where to user enters their regular expression and string, these are sent to a function in regex.py which returns whether or not the regex matches the string. I think the comments in my code clearly outline where everything occurs, but just in case it may be unclear here's what happens:
in regex.py: I have 2 classes containing only constructors, State and Fragment...  State represents a state that the NFA is in and it has either 1 or two arrows pointing from it. Fragment class represents an NFA fragment and has a start state and an accept state.

After these classes, I have a shunt method. This is basically the shunting yard algorithm... Basically, it takes a regular expression which uses infix notation, easily read by the human eye (eg a.b) and first converts this RE into postfix, which is more easily read by the computer (eg ab.). It does this by turning the infix string into a stack-ish list, looping through the input 1 character at a time, popping a character from the input and adding it to either the new operator stack or the new postfix stack, ensuring that the right symbol is added according to its order in precedence. We then add the operators to the end of the postfix stack and output as a postfix NFA.

The next method created is the compile method, which calls the shunt method! Then, it takes the returned postfix expression, reverses it so that it can be used as part of a stack. It then decides which operator is being used by popping a character from the reversed postfix list, and constructs the relevent state and fragment(s) for that symbol and adds this new fragment onto the NFA Stack.

The next followe(psilon)s method is a method which ensures all of the epsilon edges are followed by the NFA. It does this by using the current state and the state to be checked. It is very important that all epsilon edges are followed.

The match method is the method which implements all of the pre-defined methods and uses them together to check and see if the regular expression fully matches the string (No partial matches, only full matches will be accepted). This function returns true if, and only if the NFA fully matches the string, otherwise it returns false.

Finally, I have a method called Test(), which contains a range of tests consisting of regular expressions, strings and Expected results. This is done through multi test assertion and the call for the method has been commented out for efficiency purposes, and because it has already been tested and running developer-side tests every time in regex.py would just be very inefficient.

Any feedback would be much appreciated and any queries may be directed towards my GMIT email address = G00354922@gmit.ie

## License
[MIT](https://choosealicense.com/licenses/mit/)