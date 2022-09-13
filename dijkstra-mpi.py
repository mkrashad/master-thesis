from asyncio import gather
from mpi4py import MPI

# Global variables
infinity = 999999
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


graph = [
    [0, 4, 1, 3],
    [999999,  0,  999999,  999999],
    [999999, 2, 0, 1],
    [999999, 999999, 999999, 0],
]


def findMinDistance(val):
    new_dict = {key: val for key,
                val in val.items() if val != 0}

    temp = min(new_dict.values())

    res = {key: val for key,
           val in val.items() if val == temp}

    return res


def main():
    graphLength = len(graph)
    rowsPerThread = graphLength / size
    startRow = int(rowsPerThread * rank)
    endRow = int(rowsPerThread * (rank + 1))
    part = []
    distance = []
    # nodes = ['a', 'b', 'c', 'd']
    nodes = [0, 1, 2, 3]
    d = []
    for i in range(graphLength):
        d.append(dict(zip(nodes, graph[i])))

    for i in range(graphLength):
        part.append(dict(list(d[i].items())[startRow:endRow]))
        a = findMinDistance(part[0])

    b = comm.allgather(a)

    for i in range(len(b)):
        temp = min(b[i].values())
        res = {key: val for key,
               val in b[i].items() if val == temp}

    g = list(res.keys())[0]
    k = list(res.values())[0]
    n = part[g]

    print(f'First: {n}\nSecond: {part}')


if __name__ == "__main__":
    main()
