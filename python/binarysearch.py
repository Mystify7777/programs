def binary_search_recursive(arr, target, left, right):
    """
    Perform binary search to find the index of 'target' in 'arr'.
    
    Args:
    arr: List of elements to search within.
    target: The value to search for.
    left: The left boundary of the search interval.
    right: The right boundary of the search interval.
    
    Returns:
    The index of 'target' if found, otherwise -1.
    """
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Target {target} found at index {result}")
