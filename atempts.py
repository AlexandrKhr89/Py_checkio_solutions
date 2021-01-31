def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # return text.split()[0]
    return text.split()

# if __name__ == '__main__':
#     print("Example:")
#     print(first_word("Hello world"))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert first_word("Hello world") == "Hello"
#     assert first_word("a word") == "a"
#     assert first_word("hi") == "hi"
#     print("Coding complete? Click 'Check' to earn cool rewards!")
print()
print(first_word("returns the first word in a given text."))


import math

def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1

print('number_length = ', number_length(99))


def number_length_1(number: int) -> int:
    base, result = 10, 1
    while base <= number:
        base = (base << 3) + (base << 1)
        result += 1
    return result


print('number_length_1 = ', number_length_1(1000))


# Clear solution for End Zeros
# BackShow description
# one-liner
#  41 tom-tom[Follow]
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))


# Clear solution for End Zeros
# BackShow description
# 36-liner: 7 easy examples
#  44 przemyslaw.daniel[Follow]
def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))

def end_zeros(number):
    import re
    return len(re.search('0*$', str(number)).group())

def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])

def end_zeros(number):
    if not number:
       return 1
    if not number % 10:
       return 1 + end_zeros(number // 10)
    return 0

def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result

def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')

def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))


################################################################################################################
# Creative solution for End Zeros
# BackShow description
# a bundle of looping
#  29 PythonWithPI[Follow]
def end_zeros_while(num: int) -> int:
    if num == 0:
        return 1
    zeros = 0
    while not num % 10:
        num //= 10
        zeros += 1
    return zeros

#Don't do this
from itertools import takewhile, repeat
def end_zeros_takewhile(num: int) -> int:
    return (
        1
        if (num := num * 10) == 0
        else (
            sum(
                takewhile(
                    lambda x: x and num > 0,
                    (
                        not (num := num // 10) % 10
                        for _ in repeat(1)
                    )
                )
            )
        )
    )

def end_zeros_recursive(num: int) -> int:
    return 1 if num == 0 else (
        0 if num % 10 else (
            1 + end_zeros_recursive(num // 10)
        )
    )

def end_zeros_tail_recursive(num: int, pre_zeros: int=0) -> int:
    return pre_zeros + 1 if num == 0 else (
        pre_zeros if num % 10 else (
            end_zeros_tail_recursive(num // 10, pre_zeros + 1)
        )
    )

def end_zeros_string_strip(num: int) -> int:
    num = str(num)
    return len(num) - len(num.rstrip('0'))

import re
zeros_starting = re.compile('0+').match
def end_zeros_string_re(num: int) -> int:
    num = str(num)[::-1]
    match = zeros_starting(num)
    return len(zeros_starting(num)[0]) if match else 0

from time import perf_counter
def end_zeros(num: int) -> int:
    answer = None
    for name, value in globals().items():
        if name.startswith('end_zeros_'):
            start = perf_counter()
            for i in range(100000):
                if answer is None:
                    answer = value(num)
                else:
                    assert answer == value(num)
            end = perf_counter()
            print(name, end - start, answer)
    return answer

#Speediest varies between recursive, string_strip, and while
if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
    print(end_zeros(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
####################################################################################

def is_all_upper(text: str) -> bool:
    # your code here
    return text.upper() == text


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    #assert is_all_upper('') == False
    assert is_all_upper("") == True
    assert is_all_upper('132hjg1232') == False
    assert is_all_upper('   ') == True
    assert is_all_upper('123') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

####################################################################################
my_list = [1,2,3,4,5]
print('my_list = ', my_list[-1])

# Clear solution for Replace First
# BackShow description
# Three solutions + 1 in comments
#  43 Phil15[Follow]
# # Change items IN-PLACE.
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices
def replace_first(items: list) -> list:
    return items[1:] + items[:1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items