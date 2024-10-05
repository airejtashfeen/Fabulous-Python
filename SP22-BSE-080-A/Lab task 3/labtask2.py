maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', '#', 'S', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', 'G', '#']
]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_position(maze, symbol):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == symbol:
                return (row, col)
    return None

def bfs(maze):
    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        current = queue.pop(0)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] != '#' and neighbor not in visited):
                queue.append(neighbor)
                visited.append(neighbor)
                parent[neighbor] = current

    return None

path = bfs(maze)

if path:
    print("Path from Start to Goal:")
    for step in path:
        print(step)
else:
    print("No path found.")
