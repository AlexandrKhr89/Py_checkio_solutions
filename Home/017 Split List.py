'''
Simple
English UK
You have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.

example

Input: Array.

Output: Array or two arrays.

Example:

split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]
'''


def split_list(items: list) -> list:
    # your code here
    i = items
    print('\ni:', i)

    # print('len(i):', len(i))
    # print('len(i)%2:', len(i) % 2)
    # print('3//2=', 3 // 2)
    # if len(i) % 2 == 0:
    #     print('i[:len(i)//2]:', i[:len(i) // 2])
    #     print('i[len(i)//2:]:', i[len(i) // 2:])
    # else:
    #     print('i[:1 + len(i) // 2]:', i[:1 + len(i) // 2])
    #     print('i[len(i) // 2 -1:]:', i[1 + len(i) // 2:])

    return [i[:len(i) // 2], i[len(i) // 2:]] if len(i) % 2 == 0 else [i[:1 + len(i) // 2], i[1 + len(i) // 2:]]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
