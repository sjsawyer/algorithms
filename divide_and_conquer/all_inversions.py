def find_all_inversions(l):
    '''
    Find all inversions in the list `l`, where an inversion in the list is defined
    as two elements l[i], l[j] satisfying i < j and l[i] > l[j]

    Returns a list of all inversion pairs

    >>> find_all_inversions([4, 6, 2, 7, 3])
    [(4, 2), (6, 2), (7, 3), (4, 3), (6, 3)]


    --- Implementation details ---
    The naive approach of comparing all possible pairs is O(n^2). We can use a divide
    and conquer approach:
        1. Divide: Break problem into subproblems of the same type
        2. Recursively solve the subproblems
        3. Combine the solutions of the subproblems in a clever way

    In this case, we can repeatedly divide the list in half and solve each half
    recursively. For instance, for list `l`, we will "magically" have the solution
    to l1=l[:len(l)/2] and l2=l[len(l)/2:], which is the number of inversion pairs
    in the first half of the list and the number of inversion pairs in the second
    half of the list. We thus need to additionally find the number of inversion pairs
    between the lists, which we hope is a simpler problem. We can do this by sorting
    each half of the list O(n*log(n)) and using a two pointer method to find the
    number of inversion pairs between the sorted lists (O(n)).

    The total runtime is thus log(n) * n*log(n) = n*log^2(n)
                             (divide)  (combine)
    '''
    # store our inversion pairs here
    inversion_pairs = []
    # check for empty list
    if not l:
        return inversion_pairs

    def _find_all_inversions(i, j):
        '''
        Find all inversions from indices `i` to `j` in `l`
        Returns: None
        Note: appends inversion pairs to `inversion_pairs`
        '''
        if i == j:
            # nothing to do
            return
        m = (i + j)/2
        # find inversions in the left half of the left
        _find_all_inversions(i, m)
        # find inversions in the right half of the list
        _find_all_inversions(m+1, j)
        # find all inversion pairs between the two halfs
        # note: left half includes middle element
        lh = sorted(l[i:m+1])
        rh = sorted(l[m+1:j+1])
        s, t = 0, 0
        while s < len(lh) and t < len(rh):
            if lh[s] > rh[t]:
                # because lh and rh are sorted, we know that lh[v],rh[t]
                # for s <= v < len(lh) are all inversion pairs
                for v in xrange(s, len(lh)):
                    inversion_pairs.append((lh[v], rh[t]))
                t += 1
            else:
                s += 1
    # populate `inversion_pairs` with all inversion pairs from beginning
    # index 0 to last index `len(l)-1` of l
    _find_all_inversions(0, len(l)-1)

    return inversion_pairs



def main():
    l = [4, 6, 2, 7, 3]
    print "List:       {}".format(l)
    print "Inversions: {}".format(find_all_inversions(l))


if __name__ == '__main__':
    main()
