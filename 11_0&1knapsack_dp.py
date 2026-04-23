n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

W = int(input("Enter capacity of knapsack: "))

# DP table
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

# Build table
for i in range(1, n + 1):
    for w in range(W + 1):
        
        if weights[i-1] <= w:
            dp[i][w] = max(
                values[i-1] + dp[i-1][w - weights[i-1]],
                dp[i-1][w]
            )
        else:
            dp[i][w] = dp[i-1][w]

print("Maximum Profit:", dp[n][W])