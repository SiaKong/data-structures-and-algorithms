#O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted partition
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with the first element in the unsorted partition
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr