from collections import deque

class Solution:

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):

        que = deque()
        visited = [False] * V
        for i in range(V):
            if visited[i] == False:
                if self.isCycleRec(adj, i, visited, -1) == True:
                    return True

        return False

    def isCycleRec(self, adj, source, visited_set, parent):
        visited_set[source] = True
        for vertex in adj[source]:
            if visited_set[vertex] == False:
                if self.isCycleRec(adj, vertex, visited_set, source):
                    return True
            elif vertex != parent:
                return True
        return False
