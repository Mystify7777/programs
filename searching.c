#include <stdio.h>

void selection_sort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int binary_search(int arr[], int target, int n) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1; 
}

int linear_search(int arr[], int target, int n) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target)
            return i;
    }
    return -1; 
}

int main() {
    int arr[] = {3, 6, 8, 2, 5, 1, 4, 9, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 5;

    selection_sort(arr, n);

    int binary_index = binary_search(arr, target, n);
    if (binary_index != -1)
        printf("Binary search: Target %d found at index %d\n", target, binary_index);
    else
        printf("Binary search: Target %d not found\n", target);

    int linear_index = linear_search(arr, target, n);
    if (linear_index != -1)
        printf("Linear search: Target %d found at index %d\n", target, linear_index);
    else
        printf("Linear search: Target %d not found\n", target);

    return 0;
}
