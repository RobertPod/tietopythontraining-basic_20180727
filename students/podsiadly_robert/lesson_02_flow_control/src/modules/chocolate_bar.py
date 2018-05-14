#!/usr/bin/env python3


class ChocolateBar(object):

    @staticmethod
    def possible(x_size: int, y_size: int, pieces: int):
        if (pieces % x_size) and (pieces % y_size):
            return False
        elif not (pieces % x_size) and y_size > pieces / x_size:
            return True
        elif not (pieces % y_size) and x_size > pieces / y_size:
            return True
        else:
            return False


def main():
    print('Enter x sixe')
    x_size = int(input())
    print('Enter y sixe')
    y_size = int(input())
    print('Enter the expected number of pieces')
    pieces = int(input())

    cb = ChocolateBar()
    print(dir(cb))
    print(__name__)
    if cb.possible(x_size, y_size, pieces):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
