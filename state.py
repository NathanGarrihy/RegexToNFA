# Nathan Garrihy
# Thomson Construction Classes

class State:
    # Every state has 0,1, or 2 edges from it
    edges = []
    
    # Label for the arrows, None means epsilon
    label = None
    
    # Constructor for State class
    def __init__(self, label=None, edges=[]):       # Arguments with default values
        self.edges = edges
        self.label = label


class Frag:
    #   Start & accept states for NFA fragments
    start = None
    accept = None
    
    #   Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

#   Memory Addresses of Variables
myInstance = State(label='a', edges=[])
myOtherInstance = State(edges=[myInstance])
myFrag = Frag(myInstance, myOtherInstance)
print(myInstance.label)
print(myOtherInstance.edges[0])
print(myFrag)
