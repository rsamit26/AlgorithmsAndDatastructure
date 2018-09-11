"""
Graph Data Structure and Algorithms

"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices, is_undirected):
        self.vertices = vertices
        self.is_undirected = is_undirected
        self.graph = defaultdict(list)

    def add_edge(self, x, y):
        self.graph[x].append(y)

        if self.is_undirected:
            self.graph[y].append(x)

    def print(self):
        for i in self.graph:
            print(i, "->", self.graph[i])


"""
Testing Code
"""

G = Graph(6, False)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 2)
G.add_edge(2, 0)
G.add_edge(2, 3)
G.add_edge(3, 3)
print("Adjacency list for Directed graph")
G.print()

