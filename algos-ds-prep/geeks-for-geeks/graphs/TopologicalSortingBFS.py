# Function to return list containing vertices in Topological order.
class Solution:
    def topoSort(self, V, adj: [[]]):
        indegree = [0] * V
        containing_vertices = []
        for i in range(V):
            for vertex in adj[i]:
                indegree[vertex] += 1
        que = deque()

        for i in range(V):
            if indegree[i] == 0:
                que.append(i)

        while len(que) > 0:
            index = que.popleft()
            print(index)
            containing_vertices.append(index)
            for i in adj[index]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)

        return containing_vertices
        # Code here
