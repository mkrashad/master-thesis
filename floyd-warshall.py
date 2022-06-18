from datetime import datetime

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



def printGraph(solution):
  print("Following matrix shows the shortest distances between every pair of vertices \n")
  for i in range(len(solution)):
    for j in range(len(solution)):
      if solution[i][j] != float('inf'):
        print('\t', int(solution[i][j]), end=' ')
      else:
        print('\t', solution[i][j], end=' ')
    print('\n')


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
  solution = floydWarshall(dist)
  printGraph(solution)


  # start_time = datetime.now()
  # print(f"Time taken: {datetime.now() - start_time}")



if __name__ == "__main__":
    main()