# graph = [
# [0,3,3,INF], 
# [INF,0,5,8], 
# [INF,5,0,1], 
# [INF,INF,INF,0]
# ]
# INF = float("inf")




def adjacency_matrix(n):
  graph = []
  for i in range(n):
    graph.append([])
    for j in range(n):
      cost = input(f"Enter the path cost for node {i} -> {j}: ")
      graph[i].append(cost)
  print(graph)    




def main():
  nodes = int(input("Enter the number of nodes from 3 to 10: "))
  adjacency_matrix(nodes)


if __name__ == "__main__":
    main()
