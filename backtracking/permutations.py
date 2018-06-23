from collections import deque


def permute(s):
    '''
    Generate all permutations of a given string `s`

    >>> permute("abc")
    ["abc", "acb", "bca", "bac", "cab", "cba"]

    '''
    permutations = []

    def _permute(chosen, remaining):
        '''
        Generate all permutations of `s` starting with the characters in
        `chosen` by considering permutations of `remaining`

        Args:
            chosen: a stack (list) of characters (a subset of `s`)
            remaining: a queue of characters (`s` \ `chosen`)

        Returns:
            None

        Note: appends to `permutations`

        '''
        if not remaining:
            permutation = "".join(chosen)
            permutations.append(permutation)
        # We have characters remaining. Choose each one
        for _ in range(len(remaining)):
            # Choose a character from `remaining` to add to `chosen`
            char = remaining.popleft()
            chosen.append(char)
            # Recurse
            _permute(chosen, remaining)
            # Put the chosen character at the back of the `remaining` queue
            remaining.append(char)
            chosen.pop()

    # Populate `permutations` recursively
    _permute([], deque(s))

    return permutations


def main():
    s = "abc"
    permutations = permute(s)
    for p in permutations:
        print p


if __name__ == '__main__':
    main()
