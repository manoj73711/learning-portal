from collections import deque

class Solution:

    #This is my solution
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

        count = 0
        while len(que) > 0:
            index = que.popleft()
            print(index)
            containing_vertices.append(index)
            for i in adj[index]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)
            count +=1
        return count!=V
        # Code here

    # This is geeks solution
    def topologicalSort(self,V,graph):

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0] * (V)

        # Traverse adjacency lists to fill indegrees of
        # vertices.  This step takes O(V + E) time
        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
            print
            "There exists a cycle in the graph"
        else:
            # Print topological order
            print
            top_order