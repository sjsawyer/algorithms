'''
Find all combinations of elements of an array using recursion.  Note that if an
array has n elements, then the number of combinations is 2**n (since we can
represent each choice as a binary string, with 1's to indicate which elements
are chosen and 0 for those that are not).

The recursive relation is similar to Pascal's Identity,

n C k = (n-1) C (k-1) + (n-1) C k

where we can say the combinations of an array consist of those that contain the
first element of the array, and those that do not, and the combinations
containing the first element can be found by first finding those that do not
contain the first element, and then adding the first element back in.

'''

def combinations(arr):
    '''
    Recursively generate all combinations of the elements in arr.
    '''
    if len(arr) == 0:
        # Base case
        return [[]]
    all_combinations = []
    # all combinations are a combination of those that contain the first
    # element and those that do not
    f = arr[0]
    combinations_without_f = combinations(arr[1:])
    for combo in combinations_without_f:
        all_combinations.append(combo)
        all_combinations.append([f] + combo)
    return all_combinations


def main():
    print combinations([1, 2, 3])


if __name__ == '__main__':
    main()
