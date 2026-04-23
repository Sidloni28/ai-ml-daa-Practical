class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def bound(u, n, W, items):
    # If weight exceeds capacity → no profit
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    # Add full items
    while j < n and total_weight + items[j].weight <= W:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # Add fraction of next item
    if j < n:
        profit_bound += (W - total_weight) * (items[j].value / items[j].weight)

    return profit_bound


def knapsack_branch_bound(W, items, n):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)

    class Node:
        def __init__(self, level, profit, weight):
            self.level = level
            self.profit = profit
            self.weight = weight

    Q = []
    max_profit = 0

    v = Node(-1, 0, 0)
    Q.append(v)

    while Q:
        v = Q.pop(0)

        if v.level == n - 1:
            continue

        # Next level
        u = Node(v.level + 1,
                 v.profit + items[v.level + 1].value,
                 v.weight + items[v.level + 1].weight)

        # Case 1: Include item
        if u.weight <= W and u.profit > max_profit:
            max_profit = u.profit

        if bound(u, n, W, items) > max_profit:
            Q.append(u)

        # Case 2: Exclude item
        u = Node(v.level + 1, v.profit, v.weight)

        if bound(u, n, W, items) > max_profit:
            Q.append(u)

    return max_profit


# Input
n = int(input("Enter number of items: "))

values = list(map(int, input("Enter values: ").split()))
weights = list(map(int, input("Enter weights: ").split()))

W = int(input("Enter capacity: "))

items = [Item(values[i], weights[i]) for i in range(n)]

print("Maximum Profit:", knapsack_branch_bound(W, items, n))