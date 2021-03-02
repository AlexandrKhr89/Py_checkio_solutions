'''
Elementary+

Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

example

Input: Date and time as a string

Output: The same date and time, but in a more readable format

Example:

date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases it should be used "hours" and "minutes".

How it is used: To improve the understanding between computers and humans.

Precondition:
0 < date <= 31
0 < month <= 12
0 < year <= 3000
0 < hours < 24
0 < minutes < 60
'''


def date_time(time: str) -> str:
    # replace this for solution

    day = int(time[:2])
    month = int(time[3:5])
    year = int(time[6:10])
    hour = int(time[11:13])
    minute = int(time[14:])

    # print('\nday:', day)
    # print('month:', month)
    # print('year:', year)
    # print('hours:', hour)
    # print('minute:', minute)

    hour_word = ''
    minute_word = ''

    if hour == 1:
        hour_word = 'hour'
    elif hour != 1 and hour <= 24:
        hour_word = 'hours'

    if minute == 1:
        minute_word = 'minute'
    elif minute != 1 and minute < 60:
        minute_word = 'minutes'

    print('\nhour_word:', hour_word)
    print('minute_word:', minute_word)

    monthes = {1: 'January',
               2: 'February',
               3: 'March',
               4: 'April',
               5: 'May',
               6: 'June',
               7: 'July',
               8: 'August',
               9: 'September',
               10: 'October',
               11: 'November',
               12: 'December'}
    if hour_word != '' and minute_word != '':
        print('Yes !!!')
        time_list = [day, monthes.get(month), year, 'year', hour, hour_word, minute, minute_word]
        time_list = [str(tl) for tl in time_list]
        print('time_list:', time_list)
        time_str = ' '.join(time_list)
    print('time_str:', time_str)

    return time_str


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    print(date_time("11.04.1812 01:01"))
