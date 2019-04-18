def combinations_of_length(arr, k):
    '''
    Find all combinations of elements of length k in arr
    '''
    all_combinations = []
    def _combinations(sofar, remaining):
        if len(sofar) == k:
            # Ensure we copy the list to avoid mutation
            all_combinations.append(sofar[:])
            return
        if len(remaining) == 0:
            return
        # all combinations using the last letter of `remaining`
        sofar.append(remaining.pop())
        _combinations(sofar, remaining)
        # all combinations without the last letter of `remaining`
        last_element = sofar.pop()
        _combinations(sofar, remaining)
        # backtrack by putting back to initial state
        remaining.append(last_element)

    _combinations([], arr)
    return all_combinations


def main():
    print combinations_of_length([1, 2, 3, 4], 2)    


if __name__ == '__main__':
    main()
