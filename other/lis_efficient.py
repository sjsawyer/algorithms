def binary_search_and_replace(l, s, i):
    '''
    Set `l[k] = i`, where `s[l[k]]` is the smallest number in `s` that is
    greater than `s[i]`

    Note that `l` itself is not sorted, but the result of evaluating `s` at each
    `i`th index of `l` is sorted, allowing us to perform binary search.

    Returns the updated `l`, along with the index `old_idx` that `l[k]` was
    previously set to, in order to update the parent array

    '''
    b, e = 0, len(l)-1
    m = (b + e)/2
    while b < e:
        if s[l[m]] > s[i]:
            e = m - 1
        else:
            b = m + 1
        m = (b + e)/2

    # now if s[l[m]] > s[i], replace l[m] = i
    # otherwise, replace l[m+1] = i
    if s[l[m]] > s[i]:
        replace_idx = m
    else:
        replace_idx = m+1

    # update l
    prev_idx = l[replace_idx]
    l[replace_idx] = i

    return l, prev_idx


def get_current_lis(l, s, parent):
    '''
    Return the current LIS using the original sequence `s`, the auxiliary
    sequence `l` where `l[i]` keeps track of the (index in s of the ...)
    smallest ending value of the current LIS of length `i`, and `parent[i]`
    keeps track of the (index in s of the ...) element preceding `s[i]` in
    the LIS.
    '''
    last = l[-1]
    lis = []  # we know lis will be of length `l`
    while last != -1:
        lis.append(s[last])
        last = parent[last]
    lis.reverse()
    return lis


def longest_increasing_subsequence(s):
    '''
    A more efficient approach to the LIS problem, which is typically
    done with a DP approach, resulting in a suboptimal O(n**2) solution.

    The below approach reduces the run time to O(n*log(n))

    Effectively, we iterate through the array from left to right and keep track
    of the last elements of the LIS of each size (when we encounter an element
    larger than that of what we've yet seen, we obtain a new LIS of larger
    size)

    '''
    # use an array `l` to keep track of the last element of LIS at various
    # sizes, where s[l[i]] is the last element of the LIS of `s` of size `i`,
    # such that the last element of this LIS is the smallest possible of all
    # other LIS of size i

    # we use an auxiliary array `parent`, where `parent[i]` keeps track of the
    # index of the prior element to `s[i]` in the LIS
    l = [0]
    parent = [-1 for _ in range(len(s))]  # `p[i]=-1` signifies that nothing
                                          # comes before `s[i]` in the LIS

    for i in range(1, len(s)):
        if s[i] > s[l[-1]]:
            l.append(i)
            # new last element points to the previous last element
            parent[i] = l[-2]
        else:
            # replace an element in `l` with `i`
            l, prev_idx = binary_search_and_replace(l, s, i)
            parent[i] = parent[prev_idx]
        # Print info for current iteration
        current_lis = get_current_lis(l, s, parent)
        print "Current s[i]: {}".format(s[i])
        print "New s[l]:     {}".format([s[l_i] for l_i in l])
        print "Current LIS:  {}".format(current_lis)
        print ""

    return current_lis


def main():
    lis = longest_increasing_subsequence([2, 6, 3, 4, 1, 2, 9, 5, 8])
    print "LIS: {}".format(lis)


if __name__ == '__main__':
    main()
