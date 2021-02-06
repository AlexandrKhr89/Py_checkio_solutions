"""You are given a string and you have to find its first word.

This is a simplified version of the First Word mission, which can be solved later.

The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
Input: A string.

Output: A string.

Example:

first_word("Hello world") == "Hello"
1
How it is used: The first word is a command in a command line.

Precondition: The text can contain a-z, A-Z and spaces."""
############################################################################################################
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    # print(text.index(" "))
    # print("hi","hi".index(" ")i)
    if " " in text:
        # print(text.index(" "))
        return text[:text.index(" ")]
    elif " " not in text:
        return text[0:]

    # return text.index(" ")


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")


def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text

############################################################################################################
"""
https://py.checkio.org/mission/first-word-simplified/publications/quarkov/python-3/methods-contest/?ordering=most_voted&filtering=all
It's worth to look at the performance of different methods under the same predefined conditions.
Let's check runtime of the 4 methods (10000 executions for each) defined below for the next 4 cases:
-a short str which contains space chars: "asdf we"*10;
-a short str which doesn't contain space chars: "asdfawe"*10;
-a long str which contains space chars: "asdf we"*100000;
-a long str which doesn't contain space chars: "asdf we"*100000."""
############################################################################################################
# from timeit import timeit as t
#
#
# def first_word_1(text):
#     return text.split(" ")[0]
#
# print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~11.7 ms
# print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~6.1 ms
# print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~90928.2 ms
# print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~5562.9 ms
#
#
# def first_word_2(text):
#     index = text.find(" ")
#     return text[:index] if index != -1 else text
#
# print(t('first_word_2(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~6.3 ms
# print(t('first_word_2(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~4.7 ms
# print(t('first_word_2(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~7.0 ms
# print(t('first_word_2(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2108.4 ms
#
#
# def first_word_3(text):
#     try:
#         index = text.index(" ")
#         return text[:index]
#     except ValueError:
#         return text
#
# print(t('first_word_3(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~5.8 ms
# print(t('first_word_3(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~8.5 ms
# print(t('first_word_3(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~5.8 ms
# print(t('first_word_3(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2005.8 ms
#
#
# def first_word_4(text):
#     index = -1
#     for pos, letter in enumerate(text):
#         if letter == " ":
#             index = pos
#             break
#     return text[:index] if index != -1 else text
#
# print(t('first_word_4(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~13.1 ms
# print(t('first_word_4(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~71.1 ms
# print(t('first_word_4(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~13.1 ms
# print(t('first_word_4(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~788793.7 ms
############################################################################################################
"""So what conclusions can be made from all of this?

1.Since every string is an instance of the string class, it's preferred to use its methods rather than implement
a new function which seems to be faster. It won't work faster in most of the cases. Compare first_word_2 and
first_word_4 for example.

2.Despite the fact first_word_1 (which uses .split() method) looks nice and concise it works worse with long strings
than first_word_2 and first_word_3 do(they use .find() and .index() methods respectively). Especially in case there are
lots of spaces in the text.

3.str.index() method works a bit faster than str.find() but only in case there is a space in the text. Otherwise it's
needed to handle an exception which takes some extra time. 

Thus, I'd use str.find() method in such kind of tasks.
"""


import timeit

code_to_test = """
a = range(10000)
b = []
for i in a:
    b.append(i*2)
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
