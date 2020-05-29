import math

class Heap:
    array = []
    size = 0
    maxsize = 0

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = [0]*(self.maxsize+1)
        self.array[0] = -1  #0th element of the heap is -1, to satisfy heapness property. Assuming the heap elements are > 0
        self.size = 0
    
    def parent(self, pos):
        return pos//2
    
    def leftChild(self, pos):
        return 2*pos
    
    def rightChild(self, pos):
        return 2*pos+1
    
    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
    
    def isLeaf(self, pos):  #Finding leaf nodes
        if pos >= self.size//2 and pos <= self.size:
            return True
        return False

    def minHeapify(self, pos):  #heapifying the heap
        if not self.isLeaf(pos):
            if(self.array[pos] > self.array[self.leftChild(pos)] or self.array[pos] > self.array[self.rightChild(pos)]):
                if(self.array[self.leftChild(pos)] < self.array[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
    
    def insertKey(self, element):   #inserting a new element
        if self.size >= self.maxsize:
            return
        
        self.size+=1
        self.array[self.size] = element #insert at the last

        current = self.size

        while(self.array[current] < self.array[self.parent(current)]):  #percolate up
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
    def deleteMin(self):    #delete an element
        pop = self.array[1]
        self.array[1] = self.array[self.size]
        self.size-=1
        self.minHeapify(1)  #satisfying heapify property at the pos.1 due to removal of element
        return pop
    
    def decreaseKey(self, pos, new_elt):    #changing value of an element at a particular position
        self.array[pos] = new_elt
        while(pos != 0 and self.array[self.parent(pos)] > self.array[pos]): #heapness satisfaction
            self.swap(pos, self.parent(pos))
            pos = self.parent(pos)
    
    def printHeap(self): #printing a heap with in parent-child form
        for i in range(1, (self.size//2)+1): 
            print(" Parent: " + str(self.array[i])
            +" Left Child: " + str(self.array[self.leftChild(i)])
            +" Right Child: " + str(self.array[self.rightChild(i)]))


class DirectedEdge: #contains an edge from u to v, with weight w
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.wt = weight
    
    def weight(self):
        return self.wt

    def fromVertex(self):
        return self.v

    def toVertex(self):
        return self.w


class WeightedDigraph:  #constructing a weighted digraph
    edges = []
    vertices = set()

    def __init__(self, n):
        for i in range(n):
            self.edges.append(DirectedEdge(0, 0, 0))
            self.vertices.add(0)
    
    def edgeWeightedDigraph(self, data):
        self.edges = []
        self.vertices = set()

        for edge in data:
            self.vertices.add(edge[0])
            self.vertices.add(edge[1])
            self.edges.append(DirectedEdge(edge[0], edge[1], edge[2]))

    def V(self):
        return len(self.vertices)
    
    def E(self):
        return len(self.edges)
    
    def addEdge(self, edge):
        self.edges.append(DirectedEdge(edge[0], edge[1], edge[2]))
    
    def adj(self, v):
        adjvertices = set()
        for edge in self.edges:
            if(edge.fromVertex() == v):
                adjvertices.add(edge.toVertex())
        return adjvertices
    
    def edgeLister(self):
        edgelist = []
        for edge in self.edges:
            tup = (edge.fromVertex(), edge.toVertex(), edge.weight())
            edgelist.append(tup)
        return edgelist

    def minDistance(self):
        minm = math.inf
        for v in range(self.V()):
            if self.dist[v] < minm and self.sptSet[v] == False:
                minm = self.dist[v]
                min_index = v

        return min_index

    def dijkstraSP(self, s): #based on relaxAll() method defined below
        self.adjmat = [[math.inf for i in range(self.V())] for j in range(self.V())]
        self.source = s
        self.dist = [math.inf] * self.V()
        self.dist[s] = 0
        self.sptSet = [False] * self.V()

        for edge in self.edgeLister():
            self.adjmat[edge[0]][edge[1]] = edge[2]

        for i in range(self.V()):
            u = self.minDistance()
            self.sptSet[u] = True
            for v in range(self.V()):
                if self.adjmat[u][v] > 0 and self.sptSet[v] == False and (self.dist[v] > self.dist[u] + self.adjmat[u][v]):
                    self.dist[v] = self.dist[u] + self.adjmat[u][v]
    
    def distPrinter(self):
        for i in range(len(self.dist)):
            print("Shortest Distance from %d to %d is %d" %(self.source, i, self.dist[i]))


class SP:   #class to find the shortest path with a given Weighted Digraph
    def __init__(self, G, s):
        self.graph = G
        self.source = s
        #self.adjmat = [[math.inf] * G.V()] * G.V() 
        # This process creates a SHALLOW 2D ARRAY which makes reference copies of the same 1D array. Do not use this to create 2D array
        self.adjmat = [[math.inf for i in range(G.V())] for j in range(G.V())]
        self.dist = [math.inf] * G.V()
        self.dist[s] = 0
        self.sptSet = [False] * G.V()

        for edge in G.edgeLister():
            self.adjmat[edge[0]][edge[1]] = edge[2]
        #print(self.adjmat)

        self.relaxAll()

    def minDistance(self):
        minm = math.inf
        for v in range(self.graph.V()):
            if self.dist[v] < minm and self.sptSet[v] == False:
                minm = self.dist[v]
                min_index = v

        return min_index
    
    def relax(self, edge):
        if self.adjmat[edge[0]][edge[1]] > 0 and self.sptSet[edge[1]] == False and \
            (self.dist[edge[1]] > self.dist[edge[0]] + self.adjmat[edge[0]][edge[1]]):
            self.dist[edge[1]] = self.dist[edge[0]] + self.adjmat[edge[0]][edge[1]]

    def relaxAll(self):
        for i in range(self.graph.V()):
            u = self.minDistance()
            self.sptSet[u] = True
            for edge in self.graph.edgeLister():
                self.relax(edge)
                  
    def distTo(self, v):
        return self.dist[v]

    def hasPathTo(self, v):
        if(self.dist[v] < math.inf and self.dist[v] > 0):
            return True
        return False
    
    def pathTo(self, v):
        if(self.dist[v] < math.inf):
            return self.dist[v]
        return None



if __name__ == "__main__":

    print("\t\tTesting the Min-Heap\n")
    heap = Heap(10)
    heap.insertKey(5)
    heap.insertKey(3) 
    heap.insertKey(17) 
    heap.insertKey(10) 
    heap.insertKey(84) 
    heap.insertKey(19) 
    heap.insertKey(6) 
    heap.insertKey(22)
    heap.insertKey(9)

    heap.printHeap()
    print("Minimum is: ",heap.deleteMin())

    heap.decreaseKey(4,4)   #Decreasing the value of the key at pos. 4 to 4.
    heap.printHeap()

    print("\n\n\t\tTesting the DirectedEdge Class\n")
    e = DirectedEdge(0, 1, 5)   #Testing the DirectedEdge Class
    print("From Vertex:", e.fromVertex(), "to Vertex:", e.toVertex(), "with Weight:", e.weight())

    def_graph = WeightedDigraph(5)  #Testing the WeightedDigraph Class

    print("\n\t\tTesting the Weighted Digraph Class\n")
    edgeinfo = [(0, 1, 2), (0, 2, 2), (1, 2, 1), (1, 3, 1), (2, 0, 1), (2, 3, 2), (3, 3, 2)]
    data_graph = WeightedDigraph(4)
    data_graph.edgeWeightedDigraph(edgeinfo)
    print("No. of Vertices:",data_graph.V(), "\nNo. of Edges:",data_graph.E())
    print(data_graph.vertices)
    data_graph.addEdge((3, 1, 5))
    print("\nEdge (3, 1, 5) was added.\n")
    print(data_graph.edgeLister())
    print("Vertices connected from Vertex 1: :",data_graph.adj(1)) 

    print("\n\n\t\tDijkstra's Shortest Path Algorithm\n")
    data_graph.edgeWeightedDigraph(edgeinfo)
    sp = SP(data_graph, 0) #0 is the starting/source vertex
    print("\nAdjacency Matrix of the Graph:\n")
    print(sp.adjmat,"\n")
    print("\nIs there a Path from Vertex 0 to Vertex 3? :",sp.hasPathTo(3))
    print("\nDistance from Vertex 0 to Vertex 3: ",sp.distTo(3))

    print("\nPaths to other vertices from Vertex 0:\n")
    data_graph.dijkstraSP(0)
    data_graph.distPrinter()



"""
OUTPUT:

PS D:\College Material\Second Year\4th Semester\DAA Lab\Ex7> python Dijkstra.py
                Testing the Min-Heap

 Parent: 3 Left Child: 5 Right Child: 6
 Parent: 5 Left Child: 9 Right Child: 84
 Parent: 6 Left Child: 19 Right Child: 17
 Parent: 9 Left Child: 22 Right Child: 10
Minimum is:  3
 Parent: 4 Left Child: 5 Right Child: 6
 Parent: 5 Left Child: 9 Right Child: 84
 Parent: 6 Left Child: 19 Right Child: 17
 Parent: 9 Left Child: 22 Right Child: 10


                Testing the DirectedEdge Class

From Vertex: 0 to Vertex: 1 with Weight: 5

                Testing the Weighted Digraph Class

No. of Vertices: 4
No. of Edges: 7
{0, 1, 2, 3}

Edge (3, 1, 5) was added.

[(0, 1, 2), (0, 2, 2), (1, 2, 1), (1, 3, 1), (2, 0, 1), (2, 3, 2), (3, 3, 2), (3, 1, 5)]
Vertices connected from Vertex 1: : {2, 3}


                Dijkstra's Shortest Path Algorithm


Adjacency Matrix of the Graph:

[[inf, 2, 2, inf], [inf, inf, 1, 1], [1, inf, inf, 2], [inf, inf, inf, 2]]


Is there a Path from Vertex 0 to Vertex 3? : True

Distance from Vertex 0 to Vertex 3:  3

Paths to other vertices from Vertex 0:

Shortest Distance from 0 to 0 is 0
Shortest Distance from 0 to 1 is 2
Shortest Distance from 0 to 2 is 2
Shortest Distance from 0 to 3 is 3

"""