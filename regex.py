# Nathan Garrihy
# Thomson Construction Classes

class State:
    """A state with one or two arrows, all edges labeled by label."""
    # Constructor for State class
    def __init__(self, label=None, edges=[]):   #   Arguments with default values
        # Every state has 0,1, or 2 edges from it
        self.edges = edges if edges else []
        # Label for the arrows. None = E(psilon)
        self.label = label

class Fragment:
    """An NFA fragment with a start state and an accept state."""
    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

# Shunting yard algorithm
def shunt(infix):
    """Return the infix regular expression in postfix."""
    # Convert the input into a stack-ish
    infix = list(infix)[::-1] # returns reversed list

    # Operator stack.
    opers = []

    # Output list (postfix regular expression)
    postfix = []

    # Operator precedence
    prec = {'*' : 100, '+' : 90, '?':85, '.': 80, '|': 60, ')' : 40, '(' : 20}

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
            # Push any operators on the operators stack 
            # with higher precidence to the output
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
    """Return an NFA Fragment representing the infix regular expression."""
    # Convert infix to postfix
    postfix = shunt(infix)
    # Make postfix a stack of characters
    postfix = list(postfix) [::-1]
    
    # A stack for NFA fragments
    nfaStack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        # Concatinate
        if (c == '.'):
            # Pop 2 fragments off the stack
            fragment1 = nfaStack.pop()
            fragment2 = nfaStack.pop()
            # Point fragment 2's accept state at fragment 1's start state
            fragment2.accept.edges.append(fragment1.start)
            # The new start state is frag2's
            start = fragment2.start
            # The new accept state is frag1's
            accept = fragment1.accept
        # One or more
        elif (c == '+'):
            # Pop last fragment off the stack
            fragment = nfaStack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[fragment.start])
            # Point the arrows
            fragment.accept.edges.append = [fragment.start]
            fragment.accept.edges.append(accept)
        # None or one
        elif c == '?':
            # Get the last fragment off the stack
            fragment = nfaStack.pop()

            # New start and accept states
            accept = State()
            start = State(edges=[fragment.start, fragment.accept])
            # Point the arrows
            fragment.start.edges.append(fragment.accept)
            fragment.accept.edges.append(accept)
        # Or
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
        # Any number of
        elif c == '*':
            # Pop last fragment off the stack (LIFO)
            fragment = nfaStack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[fragment.start, accept])
            # Point the arrows
            fragment.accept.edges = [fragment.start, accept]
        # Any other character
        else:
            # Push a character to the nfaStack
            accept = State()
            start = State(label=c, edges=[accept])
        # The nfa stack should have exactly 1 nfa on it (the answer) 
        newFragment = Fragment(start, accept)
        # Push new fragment to NFA stack    
        nfaStack.append(newFragment)
    return nfaStack.pop()

def followes(state, current):
    """Add a state to a set and follow all of the E(psilon) arrows."""
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
    """Returns true ONLY if regular expression fully matches the string."""
    # Compile the regular expression into an NFA
    nfa = compile(regex)
    
    # Try to match the regular expression to the string s
    # The current set of states
    current = set()
    # Add the first state and follow all E(psilon) arrows
    followes(nfa.start, current)
    # The previous set of states
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

# Multi test assertion
if __name__ in "__main__":
    # Concatinate tests (.)
    concatTests = [
        ["a.b", "", False],
        ["a.b", "ab", True],
        ["a.b", "aaab",False]
        
            
    ]
        
    # One or more tests

    # None or one tests
            
    # Or tests
        
    # Any number of tests
    
          
            
    ]

    for test in concatTests:
        assert match(test[0], test[1]) == test[2], test[0] + \
               (" should match " if test[2] else " should not match ")+ test[1]

