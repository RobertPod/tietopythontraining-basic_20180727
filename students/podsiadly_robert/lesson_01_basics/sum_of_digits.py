#!/usr/bin/env python3


def main():
    print('Enter three digit integer value')
    int_value = int(input())
    print('Sum of digits is ' + str(last_digit(int_value) + tens_digit(int_value) + hundreds_digit(int_value)))


def last_digit(int_value: int):
    return int_value % 10


def tens_digit(int_value: int):
    return (int_value % 100 - int_value % 10) // 10


def hundreds_digit(int_value: int):
    return (int_value % 1000 - int_value % 100) // 100


if __name__ == '__main__':
    main()
