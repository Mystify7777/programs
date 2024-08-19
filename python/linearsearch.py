def linear_search(arr, target):
    """
    Perform linear search to find the index of 'target' in 'arr'.
    
    Args:
    arr: List of elements to search within.
    target: The value to search for.
    
    Returns:
    The index of 'target' if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50, 60]
target = 40
result = linear_search(arr, target)
print(f"Target {target} found at index {result}")

# If the target is not in the list
target = 70
result = linear_search(arr, target)
print(f"Target {target} found at index {result}")
