graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

visited= []
queue= []

def bfs(visited, graph, startNode):
    visited.append(startNode)
    queue.append(startNode)
    
    while queue:
        m= queue.pop(0)
        print(m, end=" ")
        
        for node in graph[m]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
        
print("The BFS is:")
bfs(visited, graph, '1')
    