"""Check if a given string has all symbols in upper case.
If the string is empty or doesn't have any letter in it -
function should return True.

Input: A string.

Output: a boolean.

Example:

is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == True
1
2
3
4
Precondition: a-z, A-Z, 1-9 and spaces"""


def is_all_upper(text: str) -> bool:
    # your code here
    # print('\ntext: ', text)
    my_bool = False
    my_text_length = len(text)
    my_space_count = text.count(' ')
    if text.isupper():
        my_bool = True
    elif text == '':
        my_bool = True
    elif my_text_length == my_space_count:
        my_bool = True
    elif text.isdigit():
        my_bool = True
    else:
        my_bool = False
    return my_bool


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('132hjg1232') == False
    assert is_all_upper('   ') == True
    assert is_all_upper('123') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
