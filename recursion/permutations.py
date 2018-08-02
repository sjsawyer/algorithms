def permuations(s):
    '''
    Recursively generate all permutations of a string s by, for all letters in
    s, choosing a letter l, finding all permutations of s with l removed, and
    then appending l to the beginning of each of these permutations.

    e.g. for the string "abc", we first take out "a", find all permutations of
    the string "bc", which are ["bc", "cb"], and then appending "a" to the
    beginning of these to get ["abc", "acb"]. Repeating with "b" and "c" gives
    us all of the permutations ["abc", "acb", "bac", "bca", "cab", "cba"]
    '''
    if len(s) <= 1:
        # Base case, single letter or empty string
        return [s]
    all_permuations = []
    for i in range(len(s)):
        # generate all permuationsuations not starting with s
        rest = s[:i] + s[i+1:]
        permutations_of_rest = permuations(rest)
        # add s[i] to the start of these permuationss
        for p in permutations_of_rest:
            all_permuations.append(s[i] + p)
    return all_permuations


def main():
    print permuations("1234")


if __name__ == '__main__':
    main()
