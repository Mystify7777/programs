def knapsack_dynamic(weights, values, capacity):
    n = len(values)
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in Knapsack (Dynamic):", knapsack_dynamic(weights, values, capacity))
