def binary_search_iterative(arr, target):
    """
    Perform binary search to find the index of 'target' in 'arr'.
    
    Args:
    arr: List of elements to search within.
    target: The value to search for.
    
    Returns:
    The index of 'target' if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search_iterative(arr, target)
print(f"Target {target} found at index {result}")
