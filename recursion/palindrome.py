def is_palindrome(s):
    '''
    Returns a bool indicating whether or not the string `s` is a palindrome

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("notapalindrome")
    False

    '''
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


def main():
    s1 = "racecar"
    s2 = "123321"
    s3 = "byebye"
    s4 = ""
    s5 = "h"
    for s in (s1, s2, s3, s4, s5):
        print '"{}": {}'.format(s, is_palindrome(s))


if __name__ == '__main__':
    main()
