'''
Max Digit
 Elementary
English RU
You have a number and you need to determine which digit in this number is the biggest.

Input: A positive int.

Output: An Int (0-9).

Example:

max_digit(0) == 0
max_digit(52) == 5
max_digit(634) == 6
max_digit(1) == 1
max_digit(10000) == 1
'''
#######################################################################
import math

def max_digit(number: int) -> int:
    # your code here
    if number != None:
        number = str(number)
        my_max_digit = 0
        for digit in number:
            digit = int(digit)
            if digit > my_max_digit:
                my_max_digit = digit
    return my_max_digit


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))
    print(max_digit(52))
    print(max_digit(634))
    print(max_digit(1))
    print(max_digit(10000))
    # '''
    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
    # '''
