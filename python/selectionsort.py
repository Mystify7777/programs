def selection_sort(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm.
    
    Args:
    arr: List of elements to be sorted.
    
    Returns:
    The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(f"Sorted array: {sorted_arr}")
