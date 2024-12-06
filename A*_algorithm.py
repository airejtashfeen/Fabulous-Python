import heapq

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0  # Cost from start node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(tree, heuristic, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    start_node.h = heuristic[start]
    start_node.f = start_node.g + start_node.h
    heapq.heappush(open_list, start_node)

    while open_list:
        # 1. Node Expansion: Select the node with the lowest f(n)
        current_node = heapq.heappop(open_list)

        # 2. Goal Test: Check if the goal has been reached
        if current_node.name == goal:
            return reconstruct_path(current_node)

        closed_list.add(current_node.name)

        # Explore neighbors
        for neighbor, cost in tree.get(current_node.name, []):
            if neighbor in closed_list:
                continue  # Skip already visited nodes

            # Calculate costs
            neighbor_node = Node(neighbor, current_node)
            neighbor_node.g = current_node.g + cost
            neighbor_node.h = heuristic[neighbor]
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Check if this node is already in the open list
            if any(neighbor_node.name == node.name and neighbor_node.g >= node.g for node in open_list):
                continue  # Skip this neighbor if a better path already exists

            heapq.heappush(open_list, neighbor_node)

    return None  # No path found

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Return reversed path

# Example tree structure
tree = {
    'S': [['A', 1], ['B', 5], ['C', 8]],
    'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
    'B': [['S', 5], ['G', 4]],
    'C': [['S', 8], ['G', 5]],
    'D': [['A', 3]],
    'E': [['A', 7]]
}

# Heuristic values for each node
heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}

start_node = 'S'
goal_node = 'G'

# Run A* algorithm
path = astar(tree, heuristic, start_node, goal_node)

if path:
    print("Optimal path from", start_node, "to", goal_node, ":", " -> ".join(path))
else:
    print("No path found from", start_node, "to", goal_node)
