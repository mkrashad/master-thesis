import timeit


def convertTextToArray():
    graph = []
    with open('examples/graph-4.2.txt', 'r') as file:
        for line in file:
            graph.append([int(i) for i in line.split()])
    return graph


def floydWarshall(dist):
    out_file = open('results/result-seq.txt', 'w')
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    matrix_after = dist
    print(matrix_after, file=out_file)


def main():
    matrix = convertTextToArray()
    start_time = timeit.default_timer()
    floydWarshall(matrix)
    stop_time = timeit.default_timer()
    print(f'Total time takes: {stop_time - start_time}')


if __name__ == "__main__":
    main()
