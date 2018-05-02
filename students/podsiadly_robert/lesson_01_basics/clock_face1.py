#!/usr/bin/env python3


HOUR_ANGLE = 360 / 12
MINUTE_ANGLE = 360 / (12 * 60)
SECOND_ANGLE = 360 / (12 * 60 * 60)


def main():
    print('Enter hours')
    hours = int(input())
    print('Enter minutes')
    minutes = int(input())
    print('Enter seconds')
    seconds = int(input())

    angle = hours * HOUR_ANGLE + minutes * MINUTE_ANGLE + seconds * SECOND_ANGLE
    print(str(angle))


if __name__ == '__main__':
    main()
