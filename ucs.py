import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue= [(0, start)]

    visited= {start: (0, None)}

    while priority_queue:
        current_cost, current_node= heapq.heappop(priority_queue)

        if current_node== goal:
            return current_cost, reconstruct_path(visited, start, goal)
        
        for neighbor, cost in graph[current_node]:
            total_cost= current_cost + cost

            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor]= (total_cost, current_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))
    
    return None

def reconstruct_path(visited, start, goal):
    path=[]

    current= goal

    while current is not None:
        path.append(current)
        current= visited[current][1]

    path.reverse()
    return path


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Example usage of the UCS function
start_node = 'A'
goal_node = 'G'
result = uniform_cost_search(graph, start_node, goal_node)

if result:
    total_cost, path = result
    print(f"Least cost path from {start_node} to {goal_node}: {' -> '.join(path)} with total cost {total_cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")