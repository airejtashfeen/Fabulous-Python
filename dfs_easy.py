graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

visited= []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
        
print("The DFS is:")
dfs(visited, graph, '1')
    