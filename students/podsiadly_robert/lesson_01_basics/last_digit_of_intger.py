#!/usr/bin/env python3


def main():
    print('Enter integer value')
    int_value = int(input())
    print('Last digit is ' + str(last_digit(int_value)))


def last_digit(int_value: int):
    return int_value % 10


if __name__ == '__main__':
    main()
