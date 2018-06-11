def swap(x, y):
    '''
    Swap x and y without creating a temporary variable
    (Besides the obvious x, y = y, x pythonic approach)

    Solution:
    ---------
    Let ' denote the first update to a variable and
    let '' be a second update to the same variable

    # first, update x
    x' = x + y

    # second, update y
    y' = x'    - y
       = x + y - y
       = x
    # third, update x again
    x'' = x'    - y'
        = x + y - x
        = y
    
    Can also accomplish with * and /, or repetitive applications of 
    XOR (x=x^y, y=x^y, x=x^y). This fails if x and y are pointing to
    the same variable, which can be checked in advance.

    '''
    x = x + y
    y = x - y
    x = x - y
    return x, y


def main():
    x, y = -4, 12
    print "Before swap: x = {}  y = {}".format(x, y)
    x, y = swap(x, y)
    print "After swap:  x = {}  y = {}".format(x, y)


if __name__ == '__main__':
    main()
