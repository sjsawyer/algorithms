'''
Q: Find the minimum number of operations to convert one string of characters to
   another, where the allowable operations of Insert, Remove, and Replace are
   all of equivalent cost.

   E.g. the minimum edit distance of "flour" and "flower" would be 2, because
   we can replace "u" with "w", and insert an "e".

'''

def minimum_edit_distance(s1, s2):
    '''
    Returns the minimum edit distance of strings `s1` and `s2`
    '''
    l1 = len(s1)
    l2 = len(s2)

    # Let D[m][n] be the minimum edit distance of s1[0..m-1] and s2[0..n-1]
    D = [[None for n in range(l2+1)] for m in range(l1+1)]

    # Minimum edit distance of a string and an empty string  is the length of
    # the string
    for m in range(l1+1):
        D[m][0] = m
    for n in range(l2+1):
        D[0][n] = n

    # Populate the rest of the table
    for m in range(1, l1+1):
        for n in range(1, l2+1):
            if s1[m-1] == s2[n-1]:
                D[m][n] = D[m-1][n-1]
            else:
                D[m][n] = 1 + min(
                    D[m-1][n],    # remove
                    D[m][n-1],    # insert
                    D[m-1][n-1])  # replace

    return D[l1][l2]


def main():
    s1 = "flower"
    s2 = "flour"
    med = minimum_edit_distance(s1, s2)
    print "MED of {} and {}: {}".format(s1, s2, med)


if __name__ == '__main__':
    main()
