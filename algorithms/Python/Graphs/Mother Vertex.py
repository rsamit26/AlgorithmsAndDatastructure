"""
A mother vertex in a graph G = (V,E) is a vertex v such that all other vertices in G can be reached by a path from v.
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, x, y):
        self.graph[x].append(y)

    def helper(self, visited, s):

        visited[s] = True

        for i in self.graph[s]:
            if not visited[i]:
                self.helper(visited, i)

    def find_mother(self):

        visited = [False] * self.V

        v = 0

        for i in range(self.V):
            if not visited[i]:
                self.helper(visited, i)
                v = i

        visited = [False] * self.V

        self.helper(visited, v)

        for i in visited:
            if not i:
                return -1
        return v


"""
Testing code for finding mother
"""

g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(4, 1)
g.add_edge(6, 4)
g.add_edge(5, 6)
g.add_edge(5, 2)
g.add_edge(6, 0)

print("Mother of given graph is")
print(g.find_mother())

