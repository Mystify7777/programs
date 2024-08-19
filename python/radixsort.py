def counting_sort(arr, exp):
    """
    Performs counting sort on the array based on the specified exponent.
    
    Args:
    arr: The array to be sorted.
    exp: The exponent (1, 10, 100, ...) to be used for sorting.
    
    Returns:
    The sorted array.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Modify count[] to store the position of each element in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the sorted elements into the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Sorts an array using the radix sort algorithm.
    
    Args:
    arr: The array to be sorted.
    
    Returns:
    The sorted array.
    """
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    
    # Perform counting sort for every digit, starting from the least significant digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    
    return arr

# Example usage:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(f"Sorted array: {sorted_arr}")
