"""Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0"""


def end_zeros(num: int) -> int:
    # your code here
    count_zero = 0
    if num == 0:
        count_zero = 1
        return count_zero

    elif 0 < num < 9:
        count_zero = 0

    elif num > 9:
        while num % 10 == 0:
            num //= 10
            count_zero += 1

    return count_zero


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
    print(end_zeros(1))
    print(end_zeros(10))
    print(end_zeros(101))
    print(end_zeros(245))
    print(end_zeros(10100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
