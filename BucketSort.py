#O(n): if uniform distribution of elements into the buckets
#O(n^2): if non-uniform

def bucket_sort(arr):
    # create an empty list of buckets
    buckets = [[] for _ in range(len(arr))]

    # distribute the elements of arr into the buckets
    for element in arr:
        buckets[int(element * len(buckets))].append(element)

    # sort the elements in each bucket using insertion sort
    # ***you can use any sorting algorithm you want instead of insertion sort
    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    # concatenate the sorted buckets to get the final output
    output = []
    for i in range(len(buckets)):
        output.extend(buckets[i])
    return output