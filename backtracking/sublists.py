def get_sublists(l):
    '''
    Generate all possible sublists of the list `l`

    >>> sublists([1, 2, 3])
    [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

    '''
    # List to store all sublists
    all_sublists = []

    def _get_sublists(sublist, i):
        '''
        Generate all sublists of `l` that begin with a fixed sublist of
        l[0,..,i-1] fixed in `sublist`.

        '''
        if i == len(l):
            # No elements of `l` left to use
            # Note we must make a copy of our sublist else each
            # sublist in `all_sublists` will be the same object
            sublist_copy = list(sublist)
            all_sublists.append(sublist_copy)
        else:
            # We either use the item at `l[i]` or we don't
            sublist.append(l[i])
            _get_sublists(sublist, i+1)
            sublist.pop()
            _get_sublists(sublist, i+1)

    # Populate all_sublists
    _get_sublists([], 0)

    return all_sublists
            

def main():
    l = [1, 2, 3]
    sublists = get_sublists(l)
    for sublist in sublists:
        print sublist
    

if __name__ == '__main__':
    main()
