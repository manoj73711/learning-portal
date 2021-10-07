class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        recTree = [False] * V
        visited = [False] * V
        for i in range(V):

            if self.isCyclicRec(adj, i, visited, recTree):
                return True
        return False

    def isCyclicRec(self, adj, source, visited, recTree):

        visited[source] = True
        recTree[source] = True

        for i in adj[source]:

            if visited[i] == False and self.isCyclicRec(adj, i, visited, recTree):
                return True
            elif recTree[i] == True:
                return True

        recTree[source] = False
        return False

