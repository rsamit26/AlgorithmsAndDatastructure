"""
Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u, v) in the
given graph. Here reachable mean that there is a path from vertex u to v. The reach-ability matrix is called transitive
closure of a graph.
"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.TCM = [[0 for j in range(self.V)] for i in range(self.V)]

    def add_edge(self, x, y):
        self.graph[x].append(y)

    def helper(self, s, v):
        self.TCM[s][v] = 1
        for i in self.graph[v]:
            if self.TCM[s][i] == 0:
                self.helper(s,i)

    def transitive_closure_matrix(self):

        for i in range(self.V):
            self.helper(i,i)

        return self.TCM


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(4, 1)
g.add_edge(6, 4)
g.add_edge(5, 6)
g.add_edge(5, 2)
g.add_edge(6, 0)

print("Transitive closure matrix is")

for i in g.transitive_closure_matrix():
    print(i)
