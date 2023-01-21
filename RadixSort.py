#O(nk) where n is the number of elements, k isthe number of digits in the elements

#Integers
def radix_sort(arr):
    # determine the maximum number of digits
    max_digits = len(str(max(arr)))

    # perform radix sort for each digit
    for digit in range(max_digits):

        #perform counting sort in this for loop

        # create the buckets for each digit
        buckets = [[] for _ in range(10)]

        # distribute the elements of arr into the buckets
        for element in arr:
            digit_value = (element // 10**digit) % 10
            buckets[digit_value].append(element)

        # concatenate the buckets to get the sorted output
        arr = [element for bucket in buckets for element in bucket]
    return arr

#Strings
def radix_sort_string(arr,string_len):
    for i in range(string_len-1,-1,-1):
        s=[[] for x in range(27)]
        for word in arr:
            if i>len(word)-1:
                s[0].append(word)
            else:
                index= ord(word[i])-ord('a')+1
                s[index].append(word)
        arr=[]
        for k in s:
            for w in k:
                arr.append(w)
    return arr