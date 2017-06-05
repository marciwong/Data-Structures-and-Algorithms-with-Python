# -*- coding: utf-8 -*-
"""

DSAP Workshop 

"""

from dsap_w4_graphs import Digraph, Graph, QueueNode, Queue


##########################################
# Graphs and breadth-first search


# Create an undirected graph
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


def BFS(graph, start):
    """ 
    Breadth-first search 
    Input: a graph (directed/undirected), a starting node in the graph
    Returns dists, a dictionary of explored vertices
    Returns edgesTo, to track the algorithm paths
    """
    q = Queue() # Initialize a queue
    q.enqueue(start) # Add first node to queue
    explored = set() # Initialize set of explored nodes
    explored.add(start) # Mark startin node explored
#    dists = {} # Keep track of distances from start to all other nodes
#    dists[start] = 0
    while # code: condition for queue not empty? hint: look at Queue methods
        v = q.dequeue() # get first item of queue
        #print(v)
        for w in # code: how to loop through edges starting from v? hint: look at graph methods
            if w not # code: condition?
                # code: mark w explored
                # code: update dists[w] based on dists[v]
                # code: add w to queue - use q.enqueue(...)
    return dists


BFS(graph,'1')


# Add the following to your BFS implementation: 
# Similarly to dists, use a dictionary called edgesTo to keep track of the actual paths
# edgesTo[w] stores the previous node on the shortest path to the node 
# Ie if we explore w from v, edgesTo[w] = v

# If we know the previous node for any node, we can reconstruct shortest paths
# You can use the following function to print out the entire path from s to v

#### 
# To print out path
def printPath(edgesTo,v):
    """ Based on BFS result edgesTo, prints out path from starting node to v
    """
    path = str()
    while v is not None:
        print(v) 
        path += str(v) + ' -> ' 
        v = edgesTo[v]
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
    Prints out the children nodes of a node
    """
    if v == None: v = input('Enter name: ')
    print(v)
    if graph.hasNode(v):
        for w in graph.childrenOf(v):
            print('  ' + w)
                   
s = 'Bacon, Kevin'
prList(g,s) #  He's been fairly prolific...

# Now run BFS on the graph starting from Kevin Bacon...

# Write a piece of code that prints out the path from Kevin Bacon to Nicole Kidman, Al Pacino, Marlon Brando, etc



