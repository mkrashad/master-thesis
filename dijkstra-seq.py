import timeit

# Global variables
infinity = 999999


def convertTextToArray():
    graph = []
    with open('examples/graph-100.txt', 'r') as file:
        for line in file:
            graph.append([int(i) for i in line.split()])
    return graph


def findMinDistance(distance, visitedVertex):
    minDistance = infinity
    minDistanceVertex = -1
    for i in range(len(distance)):
        if visitedVertex[i] is False and distance[i] < minDistance:
            minDistance = distance[i]
            minDistanceVertex = i
    return minDistanceVertex


def dijkstra(graph, source):
    out_file = open('results/dijkstra-seq-result.txt', 'w')
    graphLength = len(graph)
    visitedVertex = [bool(i) for i in range(graphLength)]
    distance = [int(i) for i in range(graphLength)]
    for i in range(graphLength):
        visitedVertex[i] = False
        distance[i] = infinity

    distance[source] = 0
    for i in range(graphLength):
        u = findMinDistance(distance, visitedVertex)
        visitedVertex[u] = True
        for v in range(graphLength):
            if visitedVertex[v] is False and graph[u][v] != 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]
    for i in range(len(distance)):
        print(
            f'Distance from source {source} to node {i} equals {distance[i]}', file=out_file)
    print(
        f'Distance from source {source} to destination node {i} equals {distance[graphLength-1]}')


def main():
    matrix = convertTextToArray()
    start_time = timeit.default_timer()
    dijkstra(matrix, 0)
    stop_time = timeit.default_timer()
    print(f'Total time takes: {stop_time - start_time}')


if __name__ == "__main__":
    main()
