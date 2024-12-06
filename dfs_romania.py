graph = {
    "A": ["S","Z","T"],
    "S": ["F","R"],
    "Z": ["O"],
    "O": ["S"],
    "T": ["L"],
    "L": ["M"],
    "M": ["D"],
    "D": ["C"],
    "C": ["P", "R"],
    "R": ["P","C","S"],
    "F": ["B"],
    "B": ["G","U"],
    "U": ["H","V"],
    "V": ["L"],
    "L": ["N"],
    "H": ["E"],
    "E": [],
    "L":[]

}

visited= []

def dfs(visited, graph, node, targetNode):
    if node not in visited:
        visited.append(node)
        print(node, end= " ")
        
    if node== targetNode:
        print("\nTarget Found")
        return True
        
    for neighbor in graph[node]:
       if(dfs(visited, graph, neighbor, targetNode)):
           return True

    return False
        
startNode= 'A'
goalNode= 'B'
print("DFS Path from A to B:")
if not dfs(visited,graph, startNode, goalNode):
    print("\nTarget not found.")
    