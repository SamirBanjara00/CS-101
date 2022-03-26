# A data type to represent paths within an undirected symbol graph from a fixed source vertex.

from arrayqueue import ArrayQueue
from arraystack import ArrayStack
from graph import Graph
from symboltable import SymbolTable
import stdio
import sys


class PathFinder:
    # Constructs a path finder given the graph and source vertex.
    def __init__(self, graph, s):
        self.graph = graph  # the graph
        self.s = s  # the source vertex
        self.distTo = SymbolTable()  # maps a vertex to its distance from source
        self.edgeTo = SymbolTable()  # maps a vertex to previous vertex on path
        queue = ArrayQueue()
        queue.enqueue(s)
        self.distTo[s] = 0
        self.edgeTo[s] = None
        while not queue.isEmpty():
            v = queue.dequeue()
            for w in graph.adjacentTo(v):
                if w not in self.distTo:
                    queue.enqueue(w)
                    self.distTo[w] = 1 + self.distTo[v]
                    self.edgeTo[w] = v

    # Returns the distance of vertex v from the source vertex.
    def distanceTo(self, v):
        return self.distTo[v]

    # Returns True if there is a path to vertex v from the source vertex, and False otherwise.
    def hasPathTo(self, v):
        return v in self.distTo

    # Returns the path to vertex v from the source vertex.
    def pathTo(self, v):
        path = ArrayStack()
        while v is not None:
            path.push(v)
            v = self.edgeTo[v]
        return path

    # Returns a string representation of this object.
    def __str__(self):
        s = ''
        for t in self.graph.vertices():
            if self.hasPathTo(t):
                s += self.s + ' -> ' + t + ': '
                for v in self.pathTo(t):
                    s += v + ' '
                s += '(' + str(self.distanceTo(t)) + ')\n'
        return s.strip()


# Unit tests the data type.
def _main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    s = sys.argv[3]
    graph = Graph(filename, delimiter)
    pf = PathFinder(graph, s)
    stdio.writeln(pf)


if __name__ == '__main__':
    _main()
