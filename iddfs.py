graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'G': ['H'],
    'F': [],
    'H': [],
}

def dfs(node, goal, graph, depth, path):
    path.append(node)

    if node == goal:
        return True

    if depth == 0:
        path.pop()
        return False
    
    for neighbor in graph[node]:
        if dfs(neighbor, goal, graph, depth - 1, path):
            return True
    
    path.pop()
    return False

def iddfs(start, goal, max_depth, graph):
    for depth in range(max_depth + 1):  
        path = []
        print(f"Searching at depth: {depth}")

        if dfs(start, goal, graph, depth, path):
            print(f"Path found: {path}")
            return True
    
    print("Path does not exist")
    return False


iddfs('A', 'E', 3, graph)
