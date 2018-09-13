"""
DFS for a graph

"""

from collections import defaultdict  # importing defaultdict to construct adjacencylist


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, x, y):

        """
        :param x:
        :param y:
        :return: adjacency list for the give edge
        """

        self.graph[x].append(y)

    def dfs_helper(self, s, visited, dft_arr):

        visited[s] = True

        dft_arr.append(s)

        for i in self.graph[s]:
            if not visited[i]:
                self.dfs_helper(i, visited, dft_arr)

        return dft_arr

    def dfs(self, s):
        visited = [False] * len(self.graph)
        dft_arr = []

        return self.dfs_helper(s, visited, dft_arr)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Depth First Traversal"
      " (starting from vertex 2)")
print(g.dfs(3))
