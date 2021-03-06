import pprint
from collections import defaultdict

class Graph(object):
    """Graph Data Structure, undirected by default"""

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """Add connections (list of tuple pairs) to graph"""
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """Add Connection between node1 and node2"""
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """Completely remove a node from the graph"""
        for n, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass

        try:
            del self._graph[node]
        except KeyError:
            pass
    
    def is_connected(self, node1, node2):
        """is node1 connected to node2"""
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """Finds a path between node1 and node2"""
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path

        return None

    def find_shortest_path(self, node1, node2, path=[]):
        path = path + [node1]
        

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))