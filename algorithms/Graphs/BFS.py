"""
BFS for a graph

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

    def bfs(self, s):

        """
        :param s: Source Vertex for BFS
        :return: BFS for the given graph
        """

        # initiating all the vertex as not visiting

        visited = [False] * len(self.graph)

        # Queue array for level of traversal

        queue = [s]

        visited[s] = True  # source vertex as visited

        bft_array = []

        while queue:
            s = queue.pop(0)
            bft_array.append(s)

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return bft_array

    def level_vertex_in_bfs(self, s):

        item = self.bfs(s)
        print("\n")
        for i in range(len(item)):
            print("Level of vertex ", item[i] , " is ", i)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
print(g.bfs(2))
g.level_vertex_in_bfs(2)
