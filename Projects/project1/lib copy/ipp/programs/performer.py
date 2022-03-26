# Accepts movie-cast filename (str) and delimiter (str) as command-line arguments; creates the
# associated performer-performer graph; and writes to standard output the number of vertices,
# the number of edges, the average degree, the average path length, and the clustering
# coefficient of the graph.

from graph import Graph
from instream import InStream
import smallworld
import stdio
import sys


# Entry point.
def main():
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    graph = Graph()
    inStream = InStream(filename)
    while inStream.hasNextLine():
        line = inStream.readLine()
        names = line.split(delimiter)
        for i in range(1, len(names)):
            for j in range(i + 1, len(names)):
                graph.addEdge(names[i], names[j])
    stdio.writef('Number of vertices     = %7d\n', graph.countV())
    stdio.writef('Number of edges        = %7d\n', graph.countE())
    stdio.writef('Average degree         = %7.3f\n', smallworld.averageDegree(graph))
    stdio.writef('Average path length    = %7.3f\n', smallworld.averagePathLength(graph))
    stdio.writef('Clustering coefficient = %7.3f\n', smallworld.clusteringCoefficient(graph))


if __name__ == '__main__':
    main()
