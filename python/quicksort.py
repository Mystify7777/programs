def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose a pivot element (middle element in this case)
    left = [x for x in arr if x < pivot]      # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to the pivot
    right = [x for x in arr if x > pivot]     # Elements greater than the pivot
    return quicksort(left) + middle + quicksort(right)  # Recursively sort the sublists

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
