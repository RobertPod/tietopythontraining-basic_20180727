#!/usr/bin/env python3
def is_leap(year: int):
    if year % 4:
        return False
    elif not (year % 400):
        return True
    elif not (year % 100):
        return False
    else:
        return True


def main():
    print('Enter the year')
    year = int(input())
    if is_leap(year):
        print('LEAP')
    else:
        print('COMMON')


if __name__ == '__main__':
    main()
