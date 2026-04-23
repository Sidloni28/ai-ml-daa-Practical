import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    # Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_list = []
    closed_set = set()
    step_count = 0

    start_node = Node(start)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        step_count += 1

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            
            return path[::-1], step_count

        closed_set.add(current_node.position)

        # Possible moves: Right, Down, Left, Up
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]

        for move in neighbors:
            node_pos = (current_node.position[0] + move[0],
                        current_node.position[1] + move[1])

            # Check boundaries
            if (node_pos[0] < 0 or node_pos[0] >= len(grid) or
                node_pos[1] < 0 or node_pos[1] >= len(grid[0])):
                continue

            # Check obstacle
            if grid[node_pos[0]][node_pos[1]] == 1:
                continue

            if node_pos in closed_set:
                continue

            neighbor = Node(node_pos, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(node_pos, goal)
            neighbor.f = neighbor.g + neighbor.h

            heapq.heappush(open_list, neighbor)

    return None, step_count


# 🔹 USER INPUT SECTION

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter the grid row by row (0 = free path, 1 = obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input(f"Row {i}: ").split()))
    grid.append(row)

print("\nEnter start position:")
start = tuple(map(int, input("Format -> row col: ").split()))

print("Enter goal position:")
goal = tuple(map(int, input("Format -> row col: ").split()))

path, steps = astar(grid, start, goal)

if path:
    print("\n✅ Shortest Path:", path)
else:
    print("\n❌ No path found!")

print("Step Count:", steps)
