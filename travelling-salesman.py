import math
import sys

def solve_tsp_true_bb_simplified(graph):
    n = len(graph)
    best_cost = float('inf')
    best_path = []
    
    # Pre-calculate the shortest edges
    shortest_edges = []
    for i in range(n):
        edges = sorted([weight for j, weight in enumerate(graph[i]) if i != j])
        # If a city has fewer than 2 connections, the graph is invalid
        if len(edges) < 2:
            return None, float('inf') 
        shortest_edges.append((edges[0], edges[1]))


    def search(current_city, level, current_weight, current_bound, current_path, visited):
        nonlocal best_cost, best_path

        # Base case: All cities have been visited
        if level == n:
            return_cost = graph[current_city][current_path[0]]
            if return_cost > 0:
                total_cost = current_weight + return_cost
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = current_path + [current_path[0]]
            return

        # Branching
        for next_city in range(n):
            if not visited[next_city] and graph[current_city][next_city] > 0:
                
                temp_bound = current_bound
                
                if level == 1:
                    current_bound -= (shortest_edges[current_city][0] + shortest_edges[next_city][0]) / 2
                else:
                    current_bound -= (shortest_edges[current_city][1] + shortest_edges[next_city][0]) / 2

                new_weight = current_weight + graph[current_city][next_city]
                
                # Pruning
                if current_bound + new_weight < best_cost:
                    visited[next_city] = True
                    search(next_city, level + 1, new_weight, current_bound, current_path + [next_city], visited)
                    visited[next_city] = False 

                current_bound = temp_bound

    # INITIALIZATION
    initial_bound = math.ceil(sum([min1 + min2 for min1, min2 in shortest_edges]) / 2)

    visited = [False] * n
    visited[0] = True
    
    search(0, 1, 0, initial_bound, [0], visited)

    return best_path, best_cost

# --- User Input  ---
if __name__ == '__main__':
    try:
        # Get the number of cities
        print("=== Traveling Salesperson Problem (Branch & Bound) ===")
        n = int(input("Enter the total number of cities: "))
        
        if n < 2:
            print("Error: You need at least 2 cities to form a route.")
            sys.exit()

        print(f"\nYou will now enter the distances for a {n}x{n} matrix.")
        print("Type the distances for each row separated by spaces.")
        print("Note: Use 0 for the distance from a city to itself.\n")

        adjacency_matrix = []
        
        # Get the matrix rows from the user
        for i in range(n):
            while True:
                user_input = input(f"Enter distances from City {i} to all other cities: ")
                row = list(map(int, user_input.strip().split()))
                
                # Validate the row length
                if len(row) == n:
                    adjacency_matrix.append(row)
                    break
                else:
                    print(f"-> Error: You must enter exactly {n} numbers. Please try again.")

        print("\nCalculating the optimal route...")
        optimal_path, min_cost = solve_tsp_true_bb_simplified(adjacency_matrix)
        if not optimal_path:
            print("\nResult: No valid complete path exists for this graph.")
        else:
            path_str = " -> ".join(map(str, optimal_path))
            print(f"\nMinimum Cost: {min_cost}")
            print(f"Optimal Path: {path_str}")

    except ValueError:
        print("\nError: Invalid input. Please only use whole numbers.")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")