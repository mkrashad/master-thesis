graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]
         ]
infinity = 999999


def dijkstra(graph, source):
    length = len(graph)
    visitedVertex = [bool(i) for i in range(length)]
    distance = [int(i) for i in range(length)]
    for i in range(length):
        visitedVertex[i] = False
        distance[i] = infinity

    distance[source] = 0
    for i in range(length):
        u = findMinDistance(distance, visitedVertex)
        visitedVertex[u] = True
        for v in range(length):
            if visitedVertex[v] is False and graph[u][v] != 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    for i in range(len(distance)):
        print(f'Distance from, {source}, {i}, {distance[i]}')


def findMinDistance(distance, visitedVertex):
    minDistance = infinity
    minDistanceVertex = -1
    for i in range(len(distance)):
        if visitedVertex[i] is False and distance[i] < minDistance:
            minDistance = distance[i]
            minDistanceVertex = i
    return minDistanceVertex


dijkstra(graph, 0)
