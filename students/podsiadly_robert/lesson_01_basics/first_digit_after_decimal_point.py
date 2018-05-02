#!/usr/bin/env python3


def main():
    print('Enter positive real number')
    int_value = float(input())
    print('First digit after decimal point is ' + str(last_digit(int(int_value * 10))))


def last_digit(int_value: int):
    return int_value % 10


if __name__ == '__main__':
    main()
