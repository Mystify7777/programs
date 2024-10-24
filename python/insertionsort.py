def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.
    
    Args:
    arr: List of elements to be sorted.
    
    Returns:
    The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print(f"Sorted array: {sorted_arr}")
