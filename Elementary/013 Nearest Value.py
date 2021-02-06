"""
Find the nearest value to the given one.

You are given a list of values as set form and a value for which you need to find the nearest one.

For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17,
and we need to find the nearest value to the number 9.
If we sort this set in the ascending order,
then to the left of number 9 will be number 7
and to the right - will be number 10.
But 10 is closer than 7, which means that the correct answer is 10.

A few clarifications:

If 2 numbers are at the same distance, you need to choose the smallest one;
The set of numbers is always non-empty, i.e. the size is >=1;
The given value can be in this set, which means that it’s the answer;
The set can contain both positive and negative numbers, but they are always integers;
The set isn’t sorted and consists of unique numbers.
Input: Two arguments. A list of values in the set form. The sought value is an int.

Output: Int.

Example:

nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
"""


def nearest_value(values: set, one: int) -> int:
    # your code here

    if one in values:
        # print('one in values\nnearest_value:', one)
        return one
    else:

        list_from_set = list(values)
        list_from_set.append(one)
        list_from_set.sort()

        # print("\nvalues:", values, 'one:', one, '\n       ', list_from_set)

        one_index = list_from_set.index(one)
        new_list = []

        if one_index != 0:
            left_one_is_None = False
            new_list.append(list_from_set[one_index - 1])
            # print('left_one:', new_list[0])
            new_list.append(one)
            # print('left_one + one:', new_list)
        else:
            new_list.append(one)
            left_one_is_None = True
            # print('left_one is None')

        if one_index != (len(list_from_set) - 1):
            right_one_is_None = False
            # print('right_one:', list_from_set[one_index + 1])
            new_list.append(list_from_set[one_index + 1])
            # print('left_one + one + right_one:', new_list)
        else:
            right_one_is_None = True
            # print('right_one is None')

        if left_one_is_None:
            nearest_value = new_list[1]
        elif right_one_is_None:
            nearest_value = new_list[0]
        elif len(new_list) == 3:
            d_left = new_list[1] - new_list[0]
            d_right = new_list[2] - new_list[1]
            if d_left < d_right:
                nearest_value = new_list[0]
            elif d_left > d_right:
                nearest_value = new_list[2]
            elif d_left == d_right:
                nearest_value = new_list[0]

        # print('\nANSWER:', new_list, '\nnearest_value:', nearest_value, '\n\n')

        return nearest_value


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
