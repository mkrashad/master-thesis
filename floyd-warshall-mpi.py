from mpi4py import MPI
import timeit

# Global variables
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


def convertTextToArray():
    graph = []
    with open('./graph.txt', 'r') as file:
        for line in file:
            graph.append([int(i) for i in line.split()])
    return graph


def floydWarshallMPI(dist):
    rowsPerThread = len(dist) / size
    threadsPerRow = size / len(dist)

    startRow = int(rowsPerThread * rank)
    endRow = int(rowsPerThread * (rank + 1))
    for k in range(len(dist)):
        owner = threadsPerRow*k
        dist[k] = comm.bcast(dist[k], root=owner)
        for i in range(startRow, endRow):
            for j in range(len(dist)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    if rank == 0:
        for k in range(endRow, len(dist)):
            owner = int(threadsPerRow*k)
            dist[k] = comm.recv(source=owner, tag=k)
    else:
        for k in range(startRow, endRow):
            comm.send(dist[k], dest=0, tag=k)

    return dist


def main():
    matrix_before = convertTextToArray()
    start_time = timeit.default_timer()
    # print(
    #     f'Matrix before Floyd Warshall algorithm\n {matrix_before}\n\n')
    matrix_after = matrix_before
    matrix_after = floydWarshallMPI(matrix_before)
    # print(
    #     f'Following matrix shows the shortest distances between every pair of vertices:\n\n {matrix_after}')
    stop_time = timeit.default_timer()

    out_file = open('result.txt', 'w')
    print(matrix_after, file=out_file)
    print(f'Thread {rank}\nTime takes: {stop_time - start_time}\n')


if __name__ == "__main__":
    main()
