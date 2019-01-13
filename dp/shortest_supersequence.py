'''
Q: Given two input strings, find the shortest string which contains both input
   strings as subsequences (there can be multiple such supersequences).  For
   instance, a supersequence of the strings "hello" and "chilled" would be
   "chielloed", which has length 9.

A: As with most shortest sequence problems, we are optimizing on the length
   of the final supersequence. If we let `s1` and `s2` be the inputs, and
   `opt(i1, i2)` be the length of the shortest supersequence of `s1[0..i1]`
   and `s2[0..i2]`, then we have the recursive relation

   opt(i1, i2) = { opt(i1-1, i2-1) + 1                      if s1[i1] == s2[i2]
                 { min( opt(i1-1, i2), opt(i1, i2-1) ) + 1  otherwise

'''


def shortest_supersequence(s1, s2):
    '''
    Find the shortest sequence that contains both `s1` and `s2` as subsequences

    >>> shortest_supersequence("avocado", "volcano")
    "avolcando"

    '''
    # Let dp[i1][i2] be the length of the shortest supersequence of s1[0..i1-1]
    # and s2[0..i2-1]
    dp = [[None for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    # Base case: s2 is empty string (i2 = 0)
    for i1 in range(len(s1)+1):
        dp[i1][0] = i1
    # Base case: s1 is empty string (i1 = 0)
    for i2 in range(len(s2)+1):
        dp[0][i2] = i2
    # Build up dp table bottom up
    for i1 in range(1, len(s1)+1):
        for i2 in range(1, len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                # Next letter matches
                dp[i1][i2] = dp[i1-1][i2-1] + 1
            else:
                dp[i1][i2] = min(dp[i1-1][i2], dp[i1][i2-1]) + 1
    # Retrieve the sequence
    i1, i2 = len(s1), len(s2)
    seq = []
    # construct the sequence in reverse order
    while dp[i1][i2] != 0:
        if i1 - 1 < 0:
            # we only have letters of s2 left
            seq.append(s2[i2-1])
            i2 -= 1
        elif i2 - 1 < 0:
            # we only have letters of s1 left
            seq.append(s1[i1-1])
            i1 -= 1
        elif s1[i1-1] == s2[i2-1]:
            # we chose s1[i1-1]==s2[i2-1]
            seq.append(s1[i1-1])
            i1 -= 1
            i2 -= 1
        elif dp[i1][i2] == dp[i1-1][i2] + 1:
            # we chose s1[i1-1]
            seq.append(s1[i1-1])
            i1 -= 1
        else:
            # we chose s2[i2-1]
            seq.append(s2[i2-1])
            i2 -= 1
    seq.reverse()
    return "".join(seq)


def main():
    print shortest_supersequence("avocado", "volcano")
    print shortest_supersequence("av", "")
    print shortest_supersequence("123", "321")


if __name__ == '__main__':
    main()
