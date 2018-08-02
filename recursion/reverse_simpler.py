def rev(s):
    '''
    Reverse the string s
    '''
    if s == "":
        return s
    return s[-1] + rev(s[:-1])


def main():
    print rev("hello")


if __name__ == '__main__':
    main()
