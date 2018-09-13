"""
Topological Sorting of a given graph

"""

from collections import defaultdict  # importing defaultdict to construct adjacencylist


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, x, y):

        """
        :param x:
        :param y:
        :return: adjacency list for the give edge
        """
        self.graph[x].append(y)

    def topological_helper(self, s, visited, stack):

        visited[s] = True

        for i in self.graph[s]:
            if not visited[i]:
                self.topological_helper(i, visited, stack)

        stack.insert(0, s)

    def topological_sort(self):

        visited = [False] * self.V

        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topological_helper(i, visited, stack)

        print(stack)


"""
Testing Code for Sample Data
"""

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print(
    "Following is a Topological Sort of the given graph",
    g.topological_sort())
