from mpi4py import MPI
import timeit

# Global variables
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


def convertTextToArray():
    graph = []
    with open('examples/graph-4.2.txt', 'r') as file:
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
    matrix_after = floydWarshallMPI(matrix_before)
    stop_time = timeit.default_timer()
    out_file = open('results/result-mpi.txt', 'w')
    print(matrix_after, file=out_file)
    print(f'Thread {rank}\nTime takes: {stop_time - start_time}\n')


if __name__ == "__main__":
    main()
