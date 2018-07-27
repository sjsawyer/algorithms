'''
Counting sort is an ideal choice for sorting when the range of values in the
array to be sorted is small compared to the number of elements. It works
essentially by counting how many of each element is in the array, and then
performing basic arithmetic to determine where in the final sorted array each
element will be. In addition, it is a stable sort, meaning that if two items
have the same key, then their relative order will be unchanged in the final
array, making counting sort an ideal subroutine of radix sort.

If there are n items in the array, the range of keys is k, then

    Time complexity:  O(n+k) Space complexity: O(n+k)

'''

def counting_sort(a, min_element=m, max_element=n):
    '''
    Sort the integers in the array `a` where the minimum element in the array
    is `min_element` and the maximum element is `max_element`
    '''
    counts = [0 for _ in range(m, n+1)]
    # count the number of occurences of each element
    for i in range(len(a)):
        counts(a[i]-min_element) += 1
    # calculate the starting index of each element in the sorted array
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    # Create the sorted array
    s = [None for _ in range(len(a))]
    for i in range(len(a)):
        counts[a[i]]

a:     3, 2, 2, 4, 0, 2, 0

k:     0 1 2 3 4
count: 2 0 3 1 1

count: 2 2 5 6 7
       2 2 5 7 7

[_ _ _ _ _ 3 _]

0 0 2 2 2 3 4



