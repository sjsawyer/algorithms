def reverse_text(text):
    '''
    Reverse some text using recursion

    >>> reverse_text("no tears left to cry")
    'yrc ot tfel sraet on'

    '''

    def _reverse_text(reversed_text, text_remaining):
        '''
        Reverse the text in `text_remaining` and add it to the text that
        has already been reversed in `reverse_text`

        '''
        if text_remaining:
            reversed_text.append(text_remaining.pop())
            return _reverse_text(reversed_text, text_remaining)
        else:
            return reversed_text

    text_list = list(text)
    reversed_text = _reverse_text([], list(text_list))
    # Return the reversed text as a string
    return "".join(reversed_text)


def main():
    text = "no tears left to cry"
    print reverse_text(text)


if __name__ == '__main__':
    main()
