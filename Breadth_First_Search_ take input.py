n = int(input("How many Nodes do you have: "))
graph = {}
for i in range(n):
    name = input("Enter the parent node:  ")
    salary = input("Enter the children nodes : ").split()

    graph[name] = salary
    
    
s = list(graph.keys())[0]
visited = [] 
queue = []     

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


print("Following is the Breadth-First Search")
bfs(visited, graph, s)    