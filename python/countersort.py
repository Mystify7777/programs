def counting_sort(arr):
    """
    Sorts an array using counting sort algorithm.
    
    Args:
    arr: List of integers to be sorted.
    
    Returns:
    The sorted array.
    """
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    
    # Update the count array to store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create the output array
    output = [0] * len(arr)
    
    # Place each element in its correct position in the output array
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
