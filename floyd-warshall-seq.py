import timeit


def convertTextToArray():
    graph = []
    with open('examples/graph-4.txt', 'r') as file:
        for line in file:
            graph.append([int(i) for i in line.split()])
    return graph


def floydWarshall(dist):
    graphLength = len(dist)
    out_file = open('results/floyd-seq-result.txt', 'w')
    for k in range(graphLength):
        for i in range(graphLength):
            for j in range(graphLength):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    print(dist)
    print(dist, file=out_file)


def main():
    matrix = convertTextToArray()
    start_time = timeit.default_timer()
    floydWarshall(matrix)
    stop_time = timeit.default_timer()
    print(f'Total time takes: {stop_time - start_time}')


if __name__ == "__main__":
    main()
