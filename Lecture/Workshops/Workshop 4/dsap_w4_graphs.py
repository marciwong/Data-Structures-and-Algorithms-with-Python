# -*- coding: utf-8 -*-
"""

DSAP workshop 4 graph and queue implementations

"""

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
        Inherits the methods and attributes of Digraph
        """
    def addEdge(self, src, dest):
        Digraph.addEdge(self, src, dest)
        Digraph.addEdge(self, dest, src)



class QueueNode:
    """ Node class: contains unspecified data in stuff and link to next Node
        """
    def __init__(self, stuff=None, next=None):
        self.stuff = stuff
        self.next  = next

    def __str__(self):
        return str(self.stuff)    
 
class Queue:
    """ 
    Queue using linked QueueNodes
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
        

