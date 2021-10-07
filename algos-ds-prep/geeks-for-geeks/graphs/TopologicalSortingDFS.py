class Solution:

    # #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj: [[]]):

        stack = []
        seen = [False] * V
        for i in range(V):
            if seen[i] == False:
                self.topoSortHelper(i, adj, seen, stack)

        return stack

    def topoSortHelper(self, source, adj, seen, stack):

        seen[source] = True

        for i in adj[source]:
            if seen[i] == False:
                self.topoSortHelper(i, adj, seen)

        stack.append(source)
