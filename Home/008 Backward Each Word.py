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


def backward_string_by_word(text: str) -> str:
    # your code here
    if text != '':
        word_ = text.split()
        print(word_)
        backward = text
        for w in word_:
            print('w=', w)
            backward = text.partition(w)  # append(w[::-1])
            print(list(backward))

    else:
        return ''
    return ' '#.join(backward)


print("'':", backward_string_by_word(''))
print("'world':", backward_string_by_word('world'))
print("'hello world':", backward_string_by_word('hello world'))
print("'hello   world':", backward_string_by_word('hello   world'))
print("'welcome to a game':", backward_string_by_word('welcome to a game'))

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
