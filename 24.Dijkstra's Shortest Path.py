import sys 
  
class Graph():  
    def __init__(self, vertices): 
        self.V = vertices 
        # initialising a graph with 0 values
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
  
    def printPath(self, parent, j):      
        if parent[j] == -1 :  
            print (j)
            return
        self.printPath(parent , parent[j]) 
        print (j)
    
    def printTree(self, dist, parent):
        src = 0
        print ("Vertex \t\tDistance")
        for node in range(self.V): 
            print ("\n %d --> %d \t %d" % (src, node, dist[node] ))
            print("Path")
            self.printPath(parent,node)
  
# finding vertex with minimum distance value, from the set of vertices  
# not yet included in shortest path 
    def minDistance(self, dist, Set):  
        min = sys.maxsize #setting min value as infinity
        for v in range(self.V): 
            if dist[v] < min and Set[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index 
  
# Dijkstra's shortest path algorithm 
    def dijkstra(self, src): 
        dist = [sys.maxsize] * self.V # creating lists
        dist[src] = 0
        parent = [-1] * self.V
        Set = [False] * self.V 
        for i in range(self.V): 
            u = self.minDistance(dist, Set) 
            Set[u] = True
  
# Updating distance of the adjacent vertices of the vertex if the current  
# distance is greater than new distance and the vertex in not in the shortest path
            for v in range(self.V): 
                if self.graph[u][v] > 0 and Set[v] == False and dist[v] > dist[u] \
                                                                         + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
                        parent[v] = u
  
        self.printTree(dist, parent) 
  
# Driver program 
Dijkstra = Graph(5) 
Dijkstra.graph = [[0, 2, 7, 0, 0], 
                  [0, 0, 3, 8, 5], 
                  [0, 0, 0, 1, 0], 
                  [0, 0, 0, 0, 4], 
                  [0, 0, 0, 5, 0]]; 
  
Dijkstra.dijkstra(0); 