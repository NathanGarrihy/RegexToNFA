# Nathan Garrihy
# Shunting yard algorithm for regular expression

infix = "(A|b).c"
print("input is: ", infix)
# expected output = "ab|c."
print("Expected: ", "ab|c.")
# Convert input to a stack-ish list
infix = list(infix)[::-1] # returns reversed list

# Operator stack.
opers = []

# Output list
postfix = []

# Operator precedence
prec = {'*' : 100, '+' : 90, '.': 80, '|': 60, ')' : 40, '(' : 20}

# loop through the input 1 character at a time
while infix:
        #   Pop a character from the input
        c = infix.pop()
        
        #   decide what to do based on the character
        if c == '(':
            #   push an open bracket to the opers stack
            opers.append(c)
        elif c == ')':
            #   Pop the operators stack until you find an (
            while opers[-1] != '(':
                postfix.append(opers.pop())
            #   get rid of the '('
            opers.pop()
        elif c in prec:  #   if c is an operator or a bracket do something
        #   push any operators on the operators stack with higher precidence to the output
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.push())
            #   push c to the operator stack
            opers.append(c)
        else:
            #   Typically we just push the character to the output
            postfix.append(c)

while opers:    #   while theres still something in operators
    postfix.append(opers.pop())


# convert output lsit to string
postfix = ''.join(postfix) # take list in postfix, convertthen  to strings then join them with ''

# Print the results
print("Output =", postfix)

