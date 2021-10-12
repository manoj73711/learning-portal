class Solution:

    def shortestPath(self, adj:[[]], V:int, source:int) -> int:

        dist = [float('inf')]*V
        dist[0] = 0
        seen_set = [False]*V
        for count in range(V-1):

            u = -1
            for i in range(V):
                if i not in seen_set and u==-1 or dist[i]<dist[u]:
                    u = i
            seen_set[u] = True
            for v in range(V):

                if v not in seen_set and adj[u][v]!=0:
                    dist[v] = min(dist[v], dist[u]+adj[u][v])
        return dist



