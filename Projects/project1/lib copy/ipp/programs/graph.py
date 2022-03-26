# A data type to represent an undirected symbol graph.

from instream import InStream
from symboltable import SymbolTable
import stdio
import sys


class Graph:
    # Constructs an empty graph, or one from the given file using the specified delimiter.
    def __init__(self, filename=None, delimiter=None):
        self.adj = SymbolTable()  # maps each vertex to its neighbors
        self.e = 0  # number of edges in graph
        if filename:
            inStream = InStream(filename)
            while inStream.hasNextLine():
                line = inStream.readLine()
                names = line.split(delimiter)
                for i in range(1, len(names)):
                    self.addEdge(names[0], names[i])

    # Adds an undirected edge between vertices v and w in this graph.
    def addEdge(self, v, w):
        if not self.hasVertex(v):
            self.adj[v] = set()
        if not self.hasVertex(w):
            self.adj[w] = set()
        if not self.hasEdge(v, w):
            self.adj[v].add(w)
            self.adj[w].add(v)
            self.e += 1

    # Returns True if v is a vertex in this graph, and False otherwise.
    def hasVertex(self, v):
        return v in self.adj

    # Returns True if v-w is an edge in this graph, and False otherwise.
    def hasEdge(self, v, w):
        return v in self.adj and w in self.adj[v]

    # Returns the number of vertices in this graph.
    def countV(self):
        return len(self.adj)

    # Returns the number of edges in this graph.
    def countE(self):
        return self.e

    # Returns the degree of vertex v in this graph.
    def degree(self, v):
        return len(self.adj[v])

    # Returns the vertices adjacent to vertex v in this graph, as an iterable object.
    def adjacentTo(self, v):
        return iter(self.adj[v])

    # Returns all the vertices in this graph, as an iterable object.
    def vertices(self):
        return self.adj.keys()

    # Returns a string representation of this graph.
    def __str__(self):
        s = ''
        for v in self.vertices():
            s += v + ': '
            for w in self.adjacentTo(v):
                s += w + ' '
            s += '\n'
        return s


# Unit tests the data type.
def _main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph(filename, delimiter)
    stdio.writeln(graph)


if __name__ == '__main__':
    _main()
