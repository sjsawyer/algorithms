def tobinary(n):
    '''
    Return the binary representation of the nonnegative integer `n` as a
    string.

    >>> tobinary(43)
    '101011'

    '''
    def _tobinary(digits_so_far, n):
        if n < 0:
            digits_so_far.append('-')
            return _tobinary(digits_so_far, -n)
        elif n < 2:
            digits_so_far.append(str(n))
            return digits_so_far
        else:
            digits_so_far = _tobinary(digits_so_far, n/2)
            digits_so_far.append(str(n % 2))
            return digits_so_far

    digits = _tobinary([], n)
    # Return as a string
    return "".join(digits)


def main():
    n1 = 43
    n2 = -127
    print "{}: {}".format(n1, tobinary(n1))
    print "{}: {}".format(n2, tobinary(n2))


if __name__ == '__main__':
    main()
