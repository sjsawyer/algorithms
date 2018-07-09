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

    # The length of a one character palindrome is 1
    for i in range(len(s)):
        dp[i][i] = 1

    # Fill in the dp table bottom up
    # NOTE:
    # The trick here is we need to iterate over the values in the table in such
    # a way that we will have the answer to a subproblem when we need it
    # How to do this?
    # Because we initialize our table on the diagonal (a LPS of length 1), we
    # must extend our solutions out from the diagonal, essentially gradually
    # extending the length of the LPS from 1 to the length of `s`
    for char_len in range(0, len(s)):
        for i in range(0, len(s)):
            j == i + char_len
            # We now iterate out from the diagonal

    for i in range(1, len(s)):
        for j in range(1, len(s)):
            if s[i] == s[j] and i+1<len(s):
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])





