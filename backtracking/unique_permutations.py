from collections import deque


def unique_permutations(s):
    '''
    Return all unique permutations of the string `s`
    E.g., for `s="abbc"`, "babc" and "babc" are both permutations, but are not
    unique, so we should only return one of them.

    '''
    all_unique_permutations = []

    def _unique_permutations(sofar, rest):
        '''
        Find all unique permutations that begin with `sofar` and end with
        permutations of `rest`
        '''
        if len(rest) == 0:
            all_unique_permutations.append("".join(sofar))
            return
        # keep track of which letter we have used to avoid duplicates
        chosen = set()
        for _ in range(len(rest)):
            letter = rest.popleft()
            if letter in chosen:
                # We have already used this letter, put it back and continue
                rest.append(letter)
                continue
            chosen.add(letter)
            sofar.append(letter)
            _unique_permutations(sofar, rest)
            # backtrack
            rest.append(sofar.pop())

    # populate `all_unique_permuations`
    _unique_permutations([], deque(s))
    return all_unique_permutations


def main():
    print unique_permutations("feet")


if __name__ == '__main__':
    main()
