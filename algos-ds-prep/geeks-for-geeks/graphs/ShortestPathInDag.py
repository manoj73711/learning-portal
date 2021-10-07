class Solution:
    def shortestPath(self, adj: [[]], V, s):

        seen = [False] * V
        stack = []
        dist = [float('inf')] * V
        dist[s] = 0
        for i in range(V):

            if seen[i] == False:
                self.shortestPathUtil(adj, i, seen, stack)

        while len(stack) > 0:
            elem = stack.pop
            if dist[elem] != float('inf'):
                for i in adj[elem]:
                    dist[i] = max(dist[i], dist[elem] + i)
        return dist

    def shortestPathUtil(self, adj, source, seen, stack):

        seen[source] = True

        for i in adj[source]:

            if seen[i] == False:
                self.shortestPathUtil(adj, i, seen, stack)
        stack.append(source)

