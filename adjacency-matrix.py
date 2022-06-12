graph = []


def createGraph(n):
  for i in range(n):
    graph.append([])
    for j in range(n):
      if i != j:
        cost = float(input(f"Enter the path cost for node {i} -> {j}: "))
      else:
        cost = 0
      graph[i].append(cost)




def main():
  nodes = int(input("Enter the number of nodes from 3 to 10: "))
  createGraph(nodes)
  print(graph)   




if __name__ == "__main__":
    main()
