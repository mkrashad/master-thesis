def copyGraph(graph):
  new_graph = []
  for i in range(len(graph)):
    new_graph.append([])
    for j in range(len(graph)):
      new_graph[i].append(graph[i][j])
  return new_graph


def floydWarshall(dist):
  for k in range(len(dist)):
    for i in range(len(dist)):
      for j in range(len(dist)):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
  return dist


def main():
  graph = []
  nodes = int(input("Enter the number of nodes from 3 to 10: "))
  for i in range(nodes):
    graph.append([])
    for j in range(nodes):
      if i != j:
        cost = float(input(f"Enter the path cost for node {i} -> {j}: "))
      else:
        print(f"The path from node {i} -> {j} is always 0")
        cost = 0
      graph[i].append(cost)
  dist = copyGraph(graph)
  print(floydWarshall(dist))


if __name__ == "__main__":
    main()
