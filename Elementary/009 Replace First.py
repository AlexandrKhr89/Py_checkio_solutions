'''
Replace First
In a given list the first element should become the last one.
An empty list or list with only one element should stay the same.

example

Input: List.

Output: Iterable.

Example:

replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
'''
#######################################################################

from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    print('1. items', items)
    # items[0], items[-1] = items[-1], items[0]
    if items != []:
        items.append(items.pop(0))
    print('2. items', items)
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

#######################################################################
import this
