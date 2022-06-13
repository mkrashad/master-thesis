graph = []
dist = []

def createGraph(n):
  for i in range(n):
    graph.append([])
    for j in range(n):
      if i != j:
        cost = float(input(f"Enter the path cost for node {i} -> {j}: "))
      else:
        cost = 0
      graph[i].append(cost)

def shortDist(graph):
  for i in range(len(graph)):
    dist.append([])
    for j in range(len(graph)):
      dist[i].append(graph[i][j])


def floydWarshall(dist):
  for k in range(len(dist)):
    for i in range(len(dist)):
      for j in range(len(dist)):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]


def main():
  nodes = int(input("Enter the number of nodes from 3 to 10: "))
  createGraph(nodes)
  shortDist(graph)
  floydWarshall(dist)
  print(dist)




if __name__ == "__main__":
    main()
