#O(log n)

def binary_search(lst, x):
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == x:
            return middle
        elif lst[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return -1