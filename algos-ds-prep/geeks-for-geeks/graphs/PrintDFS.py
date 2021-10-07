
class Solution:

    def printDfs(self,adj:[[]]):

        visited_set = [False for i in range(len(adj))]
        self.printDfsHelper(adj,visited_set,0)


    def printDfsHelper(self, adj:[[]], visited_set, s):

        vertices = adj[s]
        print("vertex: "+s)
        visited_set[s] = True

        for vertex in vertices:
            if visited_set[vertex] == False:
                self.printDfsHelper(adj,visited_set,vertex)


    def printDfsForDisconnectedGraph(self,adj_graph:[[]]):

        visited_set = [False for i in range(len(adj_graph))]

        for vertex in adj_graph:
            if visited_set[vertex] != False:
                self.printDfsForDisconnectedGraphHelper(adj_graph, visited_set,vertex)



    def printDfsForDisconnectedGraphHelper(self, adj:[[]], visited_set, s):

        vertices = adj[s]
        print("vertex: "+s)
        visited_set[s] = True

        for vertex in vertices:
            if visited_set[vertex] == False:
                self.printDfsForDisconnectedGraphHelper(adj,visited_set,vertex)





