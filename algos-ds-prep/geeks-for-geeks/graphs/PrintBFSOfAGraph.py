from collections import deque
class Solution:

    #Problem 1 - print bfs of an undirected graph from a given source s
    def printGraphBFS1(self, adj:[[]], s):

        visitedArray = [False for i in range(len(adj))]
        que = deque()
        que.append(s)

        while len(que)!=0:
            v = que.popleft()
            print(v)
            adj_vertices = adj[v]
            for i in range(len(adj_vertices)):
                if adj_vertices[i] not in visitedArray:
                    que.append(adj_vertices[i])
                    visitedArray[adj_vertices[i]] = True

    #Print bfs of a disconnected graph
    def printGraphBFS2(self, adj:[[]]):

        visitedArray = [False for i in range(len(adj))]
        for i in range(len(adj)):
            if i not in visitedArray:
                self.printGraphBFS(adj,visitedArray, i)
    def printGraphBFS2(self, adj:[[]], s):

        visitedArray = [False for i in range(len(adj))]
        que = deque()
        que.append(s)

        while len(que)!=0:
            v = que.popleft()
            print(v)
            adj_vertices = adj[v]
            for i in range(len(adj_vertices)):
                if adj_vertices[i] not in visitedArray:
                    que.append(adj_vertices[i])
                    visitedArray[adj_vertices[i]] = True



