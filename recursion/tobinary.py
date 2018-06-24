def tobinary(n):
    '''
    Return the binary representation of the nonnegative integer `n` as a
    string.

    >>> tobinary(43)
    '101011'

    '''
    # Store the binary digits here
    digits = []

    def _tobinary(n):
        if n < 0:
            digits.append('-')
            _tobinary(-n)
        elif n < 2:
            digits.append(str(n))
        else:
            _tobinary(n/2)
            digits.append(str(n % 2))

    # Populate `digits`
    _tobinary(n)
    # Return as a string
    return "".join(digits)


def main():
    n1 = 43
    n2 = -127
    print "{}: {}".format(n1, tobinary(n1))
    print "{}: {}".format(n2, tobinary(n2))


if __name__ == '__main__':
    main()
