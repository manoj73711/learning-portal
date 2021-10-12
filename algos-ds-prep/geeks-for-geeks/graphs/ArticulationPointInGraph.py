from collections import defaultdict


# This class represents an undirected graph
# using adjacency list representation
#TC: o(V+E)
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def AP(self):

        disc = [float('inf')]*self.V
        low = [float('inf')]*self.V
        visited = [False]*self.V
        parent = [-1]*self.V
        ap = [False]*self.V

        for i in range(self.V):
            if visited[i] is False:
                self.APUtil(i, visited, parent,low,disc,ap)

        for index, value in enumerate(ap):
            if value == True: print(index)

    def APUtil(self, u, visited, parent,low,disc,ap):

        children = 0
        vertices = self.graph[source]
        visited[u] = True
        for v in vertices:
            if visited[v] is False:
                parent[v] = u
                children +=1
                self.APUtil(v, visited,parent, low,disc)
                low[u] = min(low[u], low[v])

                if parent[u]==-1 and children >0:
                    ap[u] = True

                if parent[u]!=-1 and low[v] >=disc[u]:
                    ap[u] = True

            elif v!=parent[u]:
                low[u] = min(low[u], disc[v])



