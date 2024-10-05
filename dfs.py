graph = {
    "A": ["B", "F"],
    "F": ["G", "H"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["J"],
    "G": ["I"]
}

def dfs(graph, start_node, goal_node):
    stack = [[start_node]]
    visited = set()

    while stack:
        print("Stack:", stack)
        path = stack.pop()
        node = path[-1]
        
        if node == goal_node:
            return print("This is DFS Path:", path)
                
        if node not in visited:
            visited.add(node)
            children = graph.get(node, [])
            
            for child in children:
                newPath = path + [child]
                stack.append(newPath)

dfs(graph, "A", "I")