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
        if n < 2:
            digits.append(str(n))
            return
        digits.append(str(n % 2))
        _tobinary(n/2)

    # Populate `digits`
    _tobinary(n)
    # Reverse to get the correct representation
    digits.reverse()
    # Return as a string
    return "".join(digits)


def main():
    n = 43
    print tobinary(n)


if __name__ == '__main__':
    main()
