class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsack_greedy(weights, values, capacity):
    items = [Item(weights[i], values[i]) for i in range(len(weights))]
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0
    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break

    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in Knapsack (Greedy):", knapsack_greedy(weights, values, capacity))
