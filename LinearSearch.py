#O(n)

def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1