# A library of small-world graph functions.

from graph import Graph
from pathfinder import PathFinder
import stdio
import sys


# Returns the average degree of the specified graph.
def averageDegree(graph):
    return 2 * graph.countE() / graph.countV()


# Returns the average path length of the specified graph.
def averagePathLength(graph):
    total = 0
    for v in graph.vertices():
        pf = PathFinder(graph, v)
        for w in graph.vertices():
            if pf.hasPathTo(w):
                total += pf.distanceTo(w)
    return total / (graph.countV() * (graph.countV() - 1))


# Returns the clustering coefficient of the specified graph.
def clusteringCoefficient(graph):
    total = 0
    for v in graph.vertices():
        possible = graph.degree(v) * (graph.degree(v) - 1) / 2
        actual = 0
        for u in graph.adjacentTo(v):
            for w in graph.adjacentTo(v):
                if graph.hasEdge(u, w):
                    actual += 1
        actual /= 2
        if possible > 0:
            total += actual / possible
    return total / graph.countV()


# Unit tests the library.
def _main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph(filename, delimiter)
    stdio.writef('Number of vertices     = %7d\n', graph.countV())
    stdio.writef('Number of edges        = %7d\n', graph.countE())
    stdio.writef('Average degree         = %7.3f\n', averageDegree(graph))
    stdio.writef('average path length    = %7.3f\n', averagePathLength(graph))
    stdio.writef('Clustering coefficient = %7.3f\n', clusteringCoefficient(graph))


if __name__ == '__main__':
    _main()
