def quick_sort(l):
    '''
    Works by selecting an element `p` from `l` to be the "pivot". The list is
    then partioned into elements in `l` less than `p` and elements in `l`
    greater than `p`. These two partions are then sorted recursively, and
    are finally joined with the pivot element to created the sorted list

    Everything is done in place, with O(n*log(n)) runtime
    '''
    def _quick_sort(i, j):
        '''
        Sort the elements in `l` starting from index `i` and ending at
        index `j`
        '''
        # Base case
        if i >= j:
            return
        # Index of pivot element, arbitrarily chosen to be the first element
        p = i
        # Partion the array so that elements less than p are on the left and
        # elements greater than p are on the right
        # The following does so in place:
        swap_idx = i+1
        # Leave the pivot element where it is
        for k in range(i+1, j+1):
            if l[k] < l[p]:
                l[k], l[swap_idx] = l[swap_idx], l[k]
                swap_idx += 1
        # Move pivot to its new position
        new_pivot = swap_idx - 1
        l[p], l[new_pivot] = l[new_pivot], l[p]
        # Now recurse on both sides of the pivot point
        _quick_sort(i, new_pivot-1)
        _quick_sort(new_pivot+1, j)

    # sort l, in place
    _quick_sort(0, len(l)-1)
    return l


def main():
    l = [3, 1, 4, 1, 5, 9, 2, 6]
    print "Before:     {}".format(l)
    quick_sort(l)
    print "After sort: {}".format(l)


if __name__ == '__main__':
    main()
