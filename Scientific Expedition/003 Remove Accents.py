'''
Elementary+
English
Assuming you are developing a user based system like facebook,
you will want to provide the functionality to search for other members regardless
of the presence of accents in a username.
Without using a 3rd party collation library,
you will need to remove the accents from the username before the comparison.

é - letter with an accent; e - letter without an accent; ̀ and ́ - the stand alone accents;

example

Input: A phrase as a string (unicode).

Output: An accent free Unicode string.

Example:

checkio(u"préfèrent") == u"preferent"
checkio(u"loài trăn lớn") == u"loai tran lon"


How it is used: It might be a part of a username verification process or
a system that proposes the username based on the first and last name of a user.

Precondition: 0≤|input|≤40
'''


def checkio(in_string):
    "remove accents"
    print('in_string:', in_string)

    for s in in_string:
        print(s, ord(s))

    return in_string

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
