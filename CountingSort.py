#O(n)

def counting_sort(arr):
    # find the maximum element in arr
    max_element = len(arr)

    # create a counting array with a slot for each element from 0 to max_element
    counting_arr = [0] * (max_element + 1)

    # count the occurrences of each element in arr
    for element in arr:
        counting_arr[element] += 1

    # compute the prefix sum of counting_arr
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]
        
    # create the output array
    output_arr = [0] * len(arr)

    # place each element in its correct position in the output array
    for element in arr:
        counting_arr[element] -= 1
        output_arr[counting_arr[element]] = element
    return output_arr


print(counting_sort([5,2,3,6,1,3,4,7]))