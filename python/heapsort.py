def heapify(arr, n, i):
    """
    Heapifies the subtree rooted at index 'i' in 'arr'.
    
    Args:
    arr: The input array.
    n: Size of the heap.
    i: Index of the root of the subtree to heapify.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Sorts an array using the heap sort algorithm.
    
    Args:
    arr: The input array to be sorted.
    
    Returns:
    The sorted array.
    """
    n = len(arr)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap
        heapify(arr, i, 0)
    
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print(f"Sorted array: {sorted_arr}")
