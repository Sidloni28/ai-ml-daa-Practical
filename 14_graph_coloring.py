# Number of vertices
V = 4

# Adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Number of colors
m = 3

# Function to check if it's safe to assign color c to vertex v
def is_safe(v, color, c):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


# Backtracking function
def graph_coloring(color, v):
    # If all vertices are colored
    if v == V:
        return True

    # Try all colors
    for c in range(1, m + 1):

        if is_safe(v, color, c):
            color[v] = c   # Assign color

            if graph_coloring(color, v + 1):
                return True

            color[v] = 0   # Backtrack

    return False


# Initialize color array
color = [0] * V

if graph_coloring(color, 0):
    print("Solution exists:")
    for i in range(V):
        print(f"Vertex {i} -> Color {color[i]}")
else:
    print("No solution exists")