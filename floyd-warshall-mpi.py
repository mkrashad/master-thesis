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
    graphLength = len(dist)
    out_file = open('results/floyd-mpi-result.txt', 'w')
    rowsPerThread = graphLength / size
    threadsPerRow = size / graphLength

    startRow = int(rowsPerThread * rank)
    endRow = int(rowsPerThread * (rank + 1))
    for k in range(graphLength):
        owner = threadsPerRow*k
        dist[k] = comm.bcast(dist[k], root=owner)
        for i in range(startRow, endRow):
            for j in range(graphLength):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    if rank == 0:
        for k in range(endRow, graphLength):
            owner = int(threadsPerRow*k)
            dist[k] = comm.recv(source=owner, tag=k)
        print(dist, file=out_file)
    else:
        for k in range(startRow, endRow):
            comm.send(dist[k], dest=0, tag=k)


def main():
    matrix = convertTextToArray()
    start_time = timeit.default_timer()
    floydWarshallMPI(matrix)
    stop_time = timeit.default_timer()
    time_per_thread = stop_time - start_time
    print(f'Thread {rank}\nTime takes: {time_per_thread}\n')
    totalTime = comm.gather(time_per_thread, root=0)
    if rank == 0:
        print('Maximum time takes: ', max(totalTime))


if __name__ == "__main__":
    main()
