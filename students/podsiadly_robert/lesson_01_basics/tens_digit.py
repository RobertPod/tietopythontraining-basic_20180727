#!/usr/bin/env python3


def main():
    print('Enter integer value')
    int_value = int(input())
    print('Tens digit is ' + str(tens_digit(int_value)))


def tens_digit(int_value: int):
    return (int_value % 100 - int_value % 10) // 10


if __name__ == '__main__':
    main()
