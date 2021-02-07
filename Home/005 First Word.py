'''
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.

Example:

first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"

How it is used: the first word is a command in a command line

Precondition: the text can contain a-z A-Z , . '
'''


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    print()
    print(text)
    text = text.replace(',', ' ')
    # print('text_coma:', text)
    text = text.replace('.', ' ')
    # print('text_dot:', text)
    text_list = text.split()
    # print(text_list)
    print(text_list[0])

    return text_list[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
