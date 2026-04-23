import sys

N = 4  # number of cities

# Cost matrix
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False] * N
min_cost = sys.maxsize


def tsp(curr_pos, count, curr_cost):
    global min_cost

    # If all cities visited, return to start
    if count == N and cost[curr_pos][0] > 0:
        total_cost = curr_cost + cost[curr_pos][0]
        min_cost = min(min_cost, total_cost)
        return

    # Branching
    for i in range(N):
        if not visited[i] and cost[curr_pos][i] > 0:

            # Bounding condition
            if curr_cost + cost[curr_pos][i] < min_cost:

                visited[i] = True
                tsp(i, count + 1, curr_cost + cost[curr_pos][i])
                visited[i] = False  # Backtrack


# Start from city 0
visited[0] = True
tsp(0, 1, 0)

print("Minimum travelling cost:", min_cost)