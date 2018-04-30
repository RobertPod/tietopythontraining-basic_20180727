#!/usr/bin/env python3


def main():
    print('Enter the integer')
    i = int(input())
    print('The next number for the number ' + str(i) + ' is ' + str(next(i)))
    print('The previous number for the number ' + str(i) + ' is ' + str(previous(i)))


def next(i: int):
    return i + 1


def previous(i: int):
    return i - 1


if __name__ == '__main__':
    main()
