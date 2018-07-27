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

def counting_sort(a, max_element, min_element=0):
    '''
    Sort the integers in the array `a` where the minimum element in the array
    is `min_element` and the maximum element is `max_element`
    '''
    import pdb; pdb.set_trace()
    counts = [0 for _ in range(max_element-min_element+1)]
    # count the number of occurences of each element
    for i in range(len(a)):
        counts[a[i]-min_element] += 1
    # calculate the starting index of each element in the sorted array by
    # computing an accumulative sum of the `counts` array, and shifting
    # all elements to the right by one, setting the first element to 0
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    for i in reversed(range(1, len(counts))):
        counts[i] = counts[i-1]
    counts[0] = 0
    # Create the sorted array
    s = [None for _ in range(len(a))]
    for i in range(len(a)):
        current_element = a[i]
        index = counts[current_element-min_element]
        s[index] = current_element
        # increase the starting index by 1
        counts[current_element-min_element] += 1
    # return the sorted array
    return s


def main():
    import random
    k_lower, k_upper = 0, 20
    sample = range(k_lower, k_upper+1)
    n = 100000
    a = [random.choice(sample) for _ in range(n)]
    #print a
    import time
    t = time.time()
    counting_sort(a, k_upper, k_lower)
    print "counting sort: {}".format(time.time() - t)
    t2 = time.time()
    sorted(a)
    print "sorted: {}".format(time.time() - t2)


if __name__ == '__main__':
    main()
