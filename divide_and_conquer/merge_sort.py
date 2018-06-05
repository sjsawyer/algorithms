def merge_sort(l):
    '''
    Sort the list `l` by dividing the list in half, sorting the two halves of
    the list recursively, and combining the two sorted lists in linear time,
    resulting in an O(n*log(n)) algorithm.
    '''
    # base case
    if len(l) <= 1:
        return l
    # divide the list in half and recurse on each half
    lh = l[:len(l)/2]
    rh = l[len(l)/2:]
    lh_sorted = merge_sort(lh)
    rh_sorted = merge_sort(rh)
    # combine the sorted halves
    l_sorted = []
    j, k = 0, 0
    while j < len(lh) and k < len(rh):
        if lh_sorted[j] < rh_sorted[k]:
            l_sorted.append(lh_sorted[j])
            j += 1
        else:
            l_sorted.append(rh_sorted[k])
            k += 1
    # append remaining elements
    if j == len(lh):
        l_sorted.extend(rh_sorted[k:])
    else:
        l_sorted.extend(lh_sorted[j:])
    # done
    return l_sorted


if __name__ == '__main__':
    l = [6, 1, 4, 2, 9, 4]
    print "{} -> {}".format(l, merge_sort(l))
