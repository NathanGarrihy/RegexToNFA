# Nathan Garrihy
# Thomson Construction Classes

class State:
    # Every state has 0,1, or 2 edges from it
    edges = []
    
    # Label for the arrows, None means epsilon
    label = None
    
    # Constructor for State class
    def __init__(self, label=None, edges=[]):   #   Arguments with default values
        self.edges = edges if edges else []
        self.label = label

class Fragment:
    # Start & accept states for NFA fragments
    start = None
    accept = None
    
    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

# Shunting yard algorithm
def shunt(infix):
    infix = list(infix)[::-1] # returns reversed list

    # Operator stack.
    opers = []

    # Output list
    postfix = []

    # Operator precedence
    prec = {'*' : 100, '+' : 90, '.': 80, '|': 60, ')' : 40, '(' : 20}

    # Loop through the input 1 character at a time
    while infix:
        # Pop a character from the input
        c = infix.pop()

        # Decide what to do based on the character
        if c == '(':
            # Push an open bracket to the opers stack
            opers.append(c)
        elif c == ')':
            # Pop the operators stack until you find an (
            while opers[-1] != '(':
                postfix.append(opers.pop())
                # Get rid of the '('
            opers.pop()
        elif c in prec:    # If c is an operator or a bracket do something
            # Push any operators on the operators stack with higher precidence to the output
            while opers and prec[c]<prec[opers[-1]]:
                postfix.append(opers.pop())
            # Push c to the operator stack
            opers.append(c)
        else:
            # Typically we just push the character to the output
            postfix.append(c)

    # Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string
    return''.join(postfix)

def compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix) [::-1]
    
    nfaStack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        if (c == '.'):
            # Pop 2 fragments off the stack
            fragment1 = nfaStack.pop()
            fragment2 = nfaStack.pop()
            # Point fragment 2's accept state at fragment 1's start state
            fragment2.accept.edges.append(fragment1.start)
            # Create new instance of Fragment to represent the new NFA
            newFragment = Fragment(fragment2.start, fragment1.accept)
        elif c == '|':
            # Pop 2 fragments off the stack
            fragment1 = nfaStack.pop()
            fragment2 = nfaStack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[fragment2.start, fragment1.start])
            # Point the old accept states at the new one
            fragment2.accept.edges.append(accept)
            fragment1.accept.edges.append(accept)
            newFragment = Fragment(start, accept)
        elif c == '*':
            # Pop 1 fragment off the stack
            fragment = nfaStack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[fragment.start, accept])
            # Point the arrows
            fragment.accept.edges = [fragment.start, accept]
            # Create new instance of Fragment to represent the new NFA
            newFragment = Fragment(start, accept)
        else:
            #   push a character to the nfaStack
            accept = State()
            start = State(label=c, edges=[accept])
            # Create new instance of Fragment to represent the new NFA
            newFragment = Fragment(start, accept)
        # Push new fragment to NFA stack    
        nfaStack.append(newFragment)

    #The nfa stack should have exactly 1 nfa on it (the answer) 
    return nfaStack.pop()

# Add a state to a set and follow all of the E(psilon) arrows
def followes(state, current):
    # Only do something if we haven't already seen the state
    if state not in current:
        # Put the state itself into current
        current.add(state)
        # See whether state is labeled by E(psilon)
        if state.label is None:
            # Loop through the states pointed to by this sate
            for x in state.edges:
                # Follow all of their E(psilon)s too
                followes(x, current)


def match(regex, s):
    # This function will return true if and ONLY if the regular expression
    # (regex) fullly matches the string s. It returns false otherwise.

    # Compile the regular expression into an NFA
    nfa = compile(regex)
    
    # Try to match the regular expression to the string s
    # The current & previous sets of states
    current = set()
    # Add the first state and follow all E(psilon) arrows
    followes(nfa.start, current)
    previous = set()

    # Loop through characters in s
    for c in s:
        # Keep track of where we were
        previous = current
        # Create a new empty set for states we're about to be in
        current = set()
        # Loop through the previous states
        for state in previous:
            # Only follow arrows not labeled by E(psilon)
            if state.label is not None:
                # If the label of the state = the character read
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0], current)
    
    # Ask the NFA if it matches the string s
    return nfa.accept in current

print(match("a.b|b*", "bbbbbbbbbbbbbbbb"))
