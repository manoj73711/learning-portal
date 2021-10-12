class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj: [[]]):

        result = 0
        key = [float('inf') for i in range(V)]
        key[0] = 0
        mst = [False] * V
        for count in range(V):
            u = -1
            for i in range(V):
                if not mst[i] and u == -1 or key[i] < key[u]:
                    u = i
            mst[u] = True
            result = result + u
            for v in range(V):
                if mst[v] is False and adj[u][v] != 0:
                    key[v] = min(adj[u][v], key[v])
        return result

