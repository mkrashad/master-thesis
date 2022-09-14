from mpi4py import MPI

# Global variables
infinity = 999999
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


matrix = [
    [0, 4, 1, 3],
    [999999,  0,  999999,  999999],
    [999999, 2, 0, 1],
    [999999, 999999, 999999, 0],
]


def combine_with_nodes(val):
    newArr = []
    nodes = [i for i in range(len(val[0]))]
    for i in range(len(val)):
        newArr.append(dict(zip(nodes, val[i])))
    return newArr


def divide_graph(val, start, end):
    part = []
    for i in range(len(val)):
        part.append(dict(list(val[i].items())[start:end]))
    return part


def find_local_min(graph):
    min_value = None
    remove_zero = {}
    new_arr = {}
    for key, value in graph.items():
        if value != 0:
            remove_zero.update({key: value})
            min_value = min(remove_zero.values())
            if value == min_value:
                new_arr.update({key: value})
    return new_arr


def find_global_min(graph):
    for i in range(len(graph)):
        temp = min(graph[i].values())
        res = {key: value for key,
               value in graph[i].items() if value == temp}
    return res


def dijkstra(graph):
    return graph


def main():
    rows_per_thread = len(matrix) / size
    start_row = int(rows_per_thread * rank)
    end_row = int(rows_per_thread * (rank + 1))

    graph_with_nodes = combine_with_nodes(matrix)
    graph_per_pro = divide_graph(graph_with_nodes, start_row, end_row)

    local_min = find_local_min(graph_per_pro[0])

    combined_graph = comm.allgather(local_min)
    global_min = find_global_min(combined_graph)

    nearest_node = list(global_min.keys())[0]
    distance = list(global_min.values())[0]
    node_and_distance = graph_per_pro[nearest_node]

    result = dijkstra(graph_per_pro)
    print("before", rank, node_and_distance, graph_per_pro)
    dict_left, dicts = node_and_distance, graph_per_pro

    for key in node_and_distance.keys():
        for d in graph_per_pro:
            num = node_and_distance[key] + 1
            if num < d[key]:
                d[key] = num

    print("after", rank, node_and_distance, graph_per_pro)


    # print(rank, nearest_node, distance, node_and_distance)
    # print(f'Rank: {rank}\nFirst: {n}\nSecond: {part}\n')
if __name__ == "__main__":
    main()
