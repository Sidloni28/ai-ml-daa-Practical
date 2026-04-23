# Fractional Knapsack using Greedy Method

n = int(input("Enter number of items: "))

values = []
weights = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = float(input("Enter capacity of knapsack: "))

items = []
for i in range(n):
    ratio = values[i] / weights[i]
    items.append((ratio, values[i], weights[i]))

# Sort by ratio (descending)
items.sort(reverse=True)

total_value = 0

for ratio, value, weight in items:
    if capacity >= weight:
        capacity -= weight
        total_value += value
    else:
        fraction = capacity / weight
        total_value += value * fraction
        break

print("Maximum value in knapsack =", total_value)