'''
Every true traveler must know how to do 3 things:
fix the fire, find the water and extract useful information from the nature around him.

Programming won't help you with the fire and water,
but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day.

Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".

example

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Example:

sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"

How it is used: One day it can save your life, if you'll be lost far away from civilization.

Precondition:
00:00 <= time <= 23:59
'''


def sun_angle(time):
    # replace this for solution
    print('\ntime:', time)
    # print('time[:2]:', time[:2])
    # print('time[2:]:', time[3:])
    hour = int(time[:2])
    minuts = int(time[3:])
    time_in_minut = hour * 60 + minuts
    print('hour:', hour)
    print('minuts:', minuts)
    print('time_in_minut:', time_in_minut)

    if time_in_minut >= 6 * 60 and time_in_minut <= 18 * 60:
        angle = (180 / (12 * 60)) * (time_in_minut - 6 * 60)
        print('angle:', angle)
    else:
        angle = "I don't see the sun!"
        print('angle:', angle)

    return angle


def sun_angle(time):
    if (6 <= (int(time[:2]) + int(time[3:]) / 60) <= 18):
        return (180 / 12) * (int(time[:2]) + (int(time[3:]) / 60) - 6)
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
