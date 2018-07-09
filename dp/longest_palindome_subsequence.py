'''
Q: Find the longest subsequence of a given string which is a palindrome.

   For example, a longest palindrome subsequence of adbbcebebca is abbebba.
   Another valid choice would be abbcbba. aceca is also a palindrome
   subsequence, but it is not the longest.

A: Given an input `s` of length n, we can use the following recursive relation
   to solve this problem using dynamic programming:

       lps(s[i..j]) = {
           2 + lps(s[i+1..j-1]) if s[i] == s[j],
           max(lps(s[i+1..j]), lps(s[i..j-1])) otherwise
           }

   Note that the recursive relation can involve increasing one index while
   decreasing another. This leads to an interesting way in which we must
   build our dp table.

'''

def longest_palindrome_subsequence(s):
    '''
    Returns the longest subsequence of `s` that is also a palindrome.

    >>> longest_palindrome_subsequence('adbbebebca')
    'abbebba'

    >>> longest_palindrome_subsequence('abc')
    'a'

    '''
    # Let dp[i][j] be the longest palindrome subsequence contained within
    # s[i..j]
    dp = [[None for _ in range(len(s))] for _ in range(len(s))]

    # Fill in the dp table bottom up:
    #
    # The trick here is we need to iterate over the values in the table in such
    # a way that we will have the answer to a subproblem when we need it
    #
    # Notice here we require solutions to the "inner" subproblems (when we
    # recurse, we increase the left pointer and decrease the right pointer)
    # As such, we need to first populate the diagonal (lps of length 1), and
    # gradually fill out the table outward from the diagonal

    # Consider all valid sequence lengths
    for char_len in range(1, len(s)+1):
        # The left index can range between these values
        for i in range(0, len(s)-char_len+1):
            # The right index for this iteration
            j = i + char_len - 1
            if i == j:
                # Base case: one character palindrome
                dp[i][j] = 1
            elif s[i] == s[j] and j == i+1:
                # Edge case: 2 character palindrome
                dp[i][j] = 2 if s[i] == s[j] else 1
            elif s[i] == s[j] and j > i+1:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # work backwards to find the lps
    # can do this iteratively, but this recursive approach is elegant if you
    # forgive the many list concatenations
    def _lps_from_table(i, j):
        if i == j:
            return list(s[i])
        elif j == i+1 and s[i] == s[j]:
            return [s[i], s[j]]
        elif j > i+1 and s[i] == s[j]:
            return list(s[i]) + _lps_from_table(i+1, j-1) + list(s[j])
        else:
            i, j = (i+1, j) if dp[i+1][j] > dp[i][j-1] else (i, j-1)
            return _lps_from_table(i, j)

    lps = _lps_from_table(0, len(s)-1)
    # return a string
    return "".join(lps)


def main():
    seqs = 'adbbebebca', "hello", "a", "12321", "byebye"
    for seq in seqs:
        print "lps({}): {}".format(seq, longest_palindrome_subsequence(seq))


if __name__ == '__main__':
    main()
