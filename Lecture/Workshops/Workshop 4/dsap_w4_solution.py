# -*- coding: utf-8 -*-
"""

DSAP Workshop 

"""

##########################################
# Graphs and breadth-first search


class Digraph():
    """ edges is a dict mapping each node to a list of its children nodes
    """
    def __init__(self):
        self.edges = {}
        self.numEdges = 0
    
    def addNode(self,node):
        # Adds a node to graph (based on key value)       
        self.edges[node] = set()

    def addEdge(self,src,dest):
        # Adds the (v,w) edge, making sure the two nodes exist
        if not self.hasNode(src): 
            self.addNode(src)
        if not self.hasNode(dest): 
            self.addNode(dest)
        if not self.hasEdge(src, dest):
            self.numEdges += 1
            self.edges[src].add(dest)
            
    def childrenOf(self, v):
        # Returns a node's children
        return self.edges[v]
        
    def hasNode(self, v):
        # Checks whether the node is in graph already
        return v in self.edges
        
    def hasEdge(self, v, w):
        return w in self.edges[v]
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src + '->'\
                         + dest + '\n'
        return result[:-1] # omit final newline

class Graph(Digraph):
    """ Undirected graph: two one-way edges for every edge
        """
    def addEdge(self, src, dest):
        Digraph.addEdge(self, src, dest)
        Digraph.addEdge(self, dest, src)


# Create an unidrected graph
graph = Graph()
graph.addEdge('1','2')
graph.addEdge('2','3')
graph.addEdge('1','3')
graph.addEdge('3','4')
graph.addEdge('3','6')
graph.addEdge('4','5')
graph.addEdge('5','6')
graph.addEdge('5','7')


#####

class QueueNode:
    """ Node class: contains unspecified data in stuff and link to next Node
        """
    def __init__(self, stuff=None, next=None):
        self.stuff = stuff
        self.next  = next

    def __str__(self):
        return str(self.stuff)    
 
class Queue:
    """ Queue using linked Nodes
        Supports inserting and deleting nodes
        """
    def __init__(self):
        """ Keep track of both first and last node for fast operations"""
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, stuff):
        # Insert a Node into queue
        node = QueueNode(stuff)
        #print(node)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

   
    def dequeue(self):
        # Returns first node of the queue
        removed = self.first.stuff
        #print(removedNode)
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return removed

    def isEmpty(self):
        return self.length == 0
    
    def __str__(self):
        s = ''
        item = self.first
        while item is not None:
            s += str(item.stuff) + ' '
            item = item.next
        return s
        
    def __len__(self):
        return self.length
        

def BFS(graph, start):
    """ 
    Breadth-first search 
    Input: a graph (directed/undirected), a starting node in the graph
    Returns dists, a dictionary of explored vertices
    Returns edgesTo, to track the algorithm paths
    """
    q = Queue() # Initialize a queue
    q.enqueue(start)
    explored = set() # Initialize explored nodes
    explored.add(start)
    dists = {} # Keep track of distances from start to all other nodes
    dists[start] = 0
    edgesTo = {} # Keep track of next edges on shortest path
    edgesTo[start] = None
    while not q.isEmpty():
        v = q.dequeue()
        for w in graph.childrenOf(v):
            if w not in explored:
                explored.add(w)
                dists[w] = dists[v] + 1
                q.enqueue(w)
                edgesTo[w] = v
    return dists,edgesTo


BFS(graph,'1')


# Add to your BFS implementation: similarly to dists, a dictionary that keeps track of the previous node on the shortest path to a node
# Then use the following function to print out the path from s to v

#### 
# To print out path
def printPath(edgesTo,v):
    """ Based on BFS result edgesTo, prints out path from starting node to v
    """
    path = str()
    while v is not None:
        #print(v) 
        path += str(v) + ' -> ' 
        v = edgesTo[v]
    path = path[:-3]
    print(path)



##### 
# Small worlds and Kevin Bacon

def readMovieData(filename):
    """ Reads movie data from text file into a graph data structure
        Reads each line as connections from first instance of line to other instances
        Assumes file delimited by /
        Returns graph
    """
    graph = Graph()
    with open(filename, "r", encoding="latin-1") as ins:
        array = []
        delimiter = '/'
        for line in ins:
            names = line.split(delimiter)
            array.append(names)
            for i in range(1, len(names)):
                graph.addEdge(names[0], names[i])
    return graph

g = readMovieData("movies.txt")


def prList(graph, v = None):
    """
    Prints out children nodes
    """
    if v == None: v = input('Enter name: ')
    print(v)
    if graph.hasNode(v):
        for w in graph.childrenOf(v):
            print('  ' + w)
                   
s = 'Bacon, Kevin'
prList(g,s)

# Now run BFS on the graph starting from Kevin Bacon...
dists, edgesTo = BFS(g,s)


# Write a piece of code that prints out the path from Kevin Bacon to Nicole Kidman, Al Pacino, Marlon Brando, etc

dists['Kidman, Nicole'] # note this gives DOUBLE the actual distance (actor->movie->actor = two steps in the graph)
edgesTo['Kidman, Nicole'] # the edge leading to Nicole Kidman

v = 'Kidman, Nicole' # two
v = 'Brando, Marlon' # two
v = 'Heston, Charlton' # two
v = 'Hepburn, Audrey' # two...

printPath(edgesTo,v)

# What is the maximum distance?

v=list(dists.values())
k=list(dists.keys())
print(max(v)) # just five movies away...

# But who are the furthest away from Kevin Bacon?
# Let's sort dists: dists.items() first get a list of items which we can sort
distList = list(dists.items())
distList[0] # This is a tuple

# How can we sort this? This is tricky - need to sort by the distances.
# We sort in Python using sorted(), which takes as argument a sortable data type, a key - a function by which to sort, and other arguments
# We want to sort by the second item in the tuple (distance) - this should be our sorting key
# For sorted, the key should be a function that tells Python to get the second item in the tuples
def sortHelper(item):
    return item[1]

# Now we can sort
sorted(distList, key=sortHelper, reverse = True)[:10]

# Simpler way: keyword lambda allows us to create an "anonymous" function without explicitly defining it 
# Notice we don't need the list conversion either...
sorted(dists.items(), key=lambda item: item[1], reverse=True)[:10]

# That's a lot of Python in a single line of code.
