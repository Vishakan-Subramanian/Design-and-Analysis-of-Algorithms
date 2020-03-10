class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    
    def addEdge(self, u, v, w): #adding an edge in the form of u<->v with weight w (undirected graph)
        self.graph.append([u, v, w])
    
    def find(self, parent, i):  #find algorithm that finds parent of i
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):    #combining the disjoint sets x and y
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
    
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
        
    def kruskalMST(self):   #running Kruskal's algorithm on the graph
        result = []
        parent = []
        rank = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key = lambda item: item[2]) #sorting the graph in non-decreasing order

        for vertex in range(self.vertices): #adding all vertices to to the arrays
            parent.append(vertex)
            rank.append(0)
        
        while e < self.vertices - 1:    #running union-find based Kruskal's algorithm to find the MST
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:  #if the parent of u and v aren't the same, i.e. there is no cycle.
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        print("\nThe following edges are present in the MST by Kruskal's Algorithm: ")
        for u, v, w in result:
            print("%d --- %d, W : %d" %(u, v, w))
        

if __name__ == "__main__":
    graph = Graph(4)
    graph.addEdge(0, 1, 10)
    graph.addEdge(0, 2, 6)
    graph.addEdge(0, 3, 5)
    graph.addEdge(1, 3, 15)
    graph.addEdge(2, 3, 4)
    
    graph.kruskalMST()


"""
OUTPUT:

PS D:\College Material\Second Year\4th Semester\DAA Lab\Ex7> python Kruskal.py

The following edges are present in the MST by Kruskal's Algorithm:
2 --- 3, W : 4
0 --- 3, W : 5
0 --- 1, W : 10

"""