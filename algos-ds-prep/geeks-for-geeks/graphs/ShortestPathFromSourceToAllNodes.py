from collections import deque

class Solution:

    def findShortestPathFromSourceToAllNodes(self, adj_graph:[[]], source):

        visited = [False for i in range(len(adj_graph))]
        visited[0] = True
        shortest_path = [0 for i in range(len(adj_graph))]
        que = deque()
        que.append(adj_graph[source])
        shortest_path[0] = 1

        while len(que)>0:
            vertex = que.popleft()
            for adj_vertext in vertex:
                if visited[adj_vertext] == False:
                    que.append(adj_vertext)
                    shortest_path[adj_vertext] = shortest_path[vertex] + 1
                    visited[adj_vertext] = True
        return shortest_path

