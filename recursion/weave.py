'''
Q: "Weave" two lists together `a` and `b` together in all possible ways such that
   in the produced list `l`, we always have that l.index(a[i]) < l.index(a[i+1]).
   In other words, the ordering of the elements in a and b are maintained in the new
   list.

   For instance, weave([1, 2], [3, 4]) produces the following lists:

       [1, 2, 3, 4]
       [1, 3, 2, 4]
       [1, 3, 4, 2]
       [3, 4, 1, 2]
       [3, 1, 2, 4]
       [3, 1, 4, 2]

   Note that this routine can come up as a subroutine in other algorithms. For
   example, when considering all possible ordering of elements that can
   produce a given binary tree.

'''

def weave(a, b):
    '''
    Return all possible "weaves" of the lists `a` and `b`, where a weave is
    defined above
    '''
    all_weaves = []

    def _weave(prefix, a_remaining, b_remaining):
        '''
        Produce all possible weave that begin with the elements in `prefix`,
        with the remaining elements in `a` and `b` given in `a_remaining`
        and `b_remaining`
        '''
        if not a_remaining or not b_remaining:
            all_weaves.append(prefix + a_remaining + b_remaining)
            return
        # recurse by taking the first element from the remainder of a,
        # and then the first element from the remainder of b
        for l in (a_remaining, b_remaining):
            # l is a reference
            prefix.append(l.pop())
            _weave(prefix, a_remaining, b_remaining)
            # backtrack
            l.append(prefix.pop())

    # because we are treating a and b as stacks, we must call our recursive
    # function with a and b reversed so we can pop from the "beginning"
    _weave([], list(reversed(a)), list(reversed(b)))
    return all_weaves


def main():
    a = [1, 2]
    b = [3, 4]
    weaves = weave(a, b)
    for w in weaves:
        print w
    

if __name__ == '__main__':
    main()
