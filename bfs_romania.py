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

def bfs(visited, graph, startNode, targetNode):
    queue = [startNode]
    visited.append(startNode)

    while queue:
        node = queue.pop(0) 
        print(node, end=" ")

        if node == targetNode:
            print("\nTarget Found")
            return True
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return False

visited = []
startNode = 'A'
goalNode = 'B'
print("BFS Path from A to B:")
if not bfs(visited, graph, startNode, goalNode):
    print("\nTarget not found.")
