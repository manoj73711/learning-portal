
#Kosarajus algorithm in 3 steps 
class Solution:
    def printStronglyConnectedComponents(self,adj:[[]], V):
        seen_set = [False]*V
        stack = []

        #Step 1
        for i in range(V):
            if seen_set[i] is False:
                self.dfsOrderHelper(adj,V,seen_set,stack)
        #Step 2
        transpose = self.getTranspose(adj, V)

        #Step 3
        seen_set = [False] * V
        while len(stack)>0:
            source =stack.pop()
            for vertex in source:
                if seen_set[source] is False:
                    self.dfsUtil(transpose,V,seen_set)
            print("\n")

    def dfsUtil(self, adj:[[]], source, seen_set):
        vertecies = adj[source]
        seen_set[source] = True
        print(source, end="")
        for vertex in vertecies:
            if seen_set[vertex] is False:
                self.dfsUtil(adj,vertex,seen_set)

    def getTranspose(self, adj:[[]], V):

        transpose = [[] for i in range(V)]
        for i in range(V):
            for j in len(adj[i]):
                self.doTranspose(transpose,adj[i][j],j)
        return transpose

    def doTranspose(transpose:[[]], source, dest):
        transpose[source].append(dest)



    def dfsOrderHelper(self, adj:[[]], s, seen_set, stack):

        vertices = adj[s]
        for vertex in vertices:
            if seen_set[vertex] is False:
                self.dfsOrderHelper(adj, vertex, seen_set, stack)
        stack.append(s)




