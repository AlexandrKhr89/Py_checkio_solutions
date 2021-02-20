'''
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string.

Example:

backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition: The line consists only from alphabetical symbols and spaces.
'''


def backward_string_by_word(text: str):
    print('text:', text, '(len(text):', len(text), ')')
    wl = []
    w = ''
    bwl = []
    for i, s in enumerate(text):
        #		print(i,'s=',s)
        if s == ' ':
            #			wl.append(w)
            w = ''
            wl.append(s)
        elif s != ' ':
            w += s
            if i != len(text) - 1:
                if text[i + 1] == ' ':
                    wl.append(w)
                    w = ''
            elif i == len(text) - 1:
                wl.append(w)
    for w in wl:
        #		print(w[::-1])
        bwl.append(w[::-1])
    # print(wl)

    new_text = ''.join(bwl)
    print(new_text)
    return new_text


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
