import timeit


def convertTextToArray():
    graph = []
    with open('./graph.txt', 'r') as file:
        for line in file:
            graph.append([int(i) for i in line.split()])
    return graph


def floydWarshall(dist):
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def main():
    matrix_before = convertTextToArray()
    start_time = timeit.default_timer()
    # print(
    #     f'Matrix before Floyd Warshall algorithm\n {matrix_before}\n\n')
    matrix_after = matrix_before
    matrix_after = floydWarshall(matrix_before)
    # print(
    #     f'Following matrix shows the shortest distances between every pair of vertices:\n\n {matrix_after}')
    stop_time = timeit.default_timer()
    out_file = open('results.txt', 'w')
    print(matrix_after, file=out_file)
    print(f'Time takes: {stop_time - start_time}')


if __name__ == "__main__":
    main()
