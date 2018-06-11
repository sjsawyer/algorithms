'''
Question: Find the missing number in an array of items from 1 to 100

Also, extend to array containing not only ints, and multiple missing
elements.

'''

def find_missing_int(l):
    '''
    Find the missing integer in l, where l is a list of integers from
    1 to len(l), with one element missing.

    Can use the fact that the sum of numbers from 1 up to n should be
    n(n+1)/2

    '''
    expected_sum = len(l)*(len(l)+1)/2
    actual_sum = sum(l)
    return expected_sum - actual_sum


def find_missing_general(l_complete, l_incomplete):
    '''
    Return the missing elements from an incomplete set of elements
    `l_incomplete` using `l_complete` as a reference for the original items.

    '''
    complete = set(l_complete)
    incomplete = set(l_incomplete)
    missing = list(complete.difference(incomplete))
    return missing


def main():
    import random

    # Example 1
    l = range(100)
    missing_element = random.choice(l)
    del(l[missing_element])
    print "Number removed: {}".format(missing_element)
    print "Number found to be missing: {}".format(find_missing_int(l))

    # Example 2
    l = 'abcdefghijklmnop'
    n_missing_elements = random.choice(range(5))
    missing_elements = random.sample(l, n_missing_elements)
    l_set = set(l)
    for me in missing_elements:
        l_set.remove(me)
    print "Elements removed: {}".format(missing_elements)
    print "Found missing: {}".format(
        find_missing_general(l, l_set))


if __name__ == '__main__':
    main()
