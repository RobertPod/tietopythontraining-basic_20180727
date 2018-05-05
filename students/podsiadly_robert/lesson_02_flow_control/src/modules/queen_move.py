#!/usr/bin/env python3
from math import fabs


class QueentMove(object):
    def is_queen_move(self, start_column: int, start_row: int, dest_column: int, dest_row: int) -> bool:
        if fabs(start_column - dest_column) > 2 or fabs(start_row - dest_row) > 2:
            return False
        elif fabs(start_column - dest_column) == 2 and fabs(start_row - dest_row) == 1:
            return True
        elif fabs(start_column - dest_column) == 1 and fabs(start_row - dest_row) == 2:
            return True
        else:
            return False


def main():
    print('Enter start_column (1-8)')
    start_column = int(input())
    print('Enter start_row (1-8)')
    start_row = int(input())
    print('Enter dest_column (1-8)')
    dest_column = int(input())
    print('Enter dest_row (1-8)')
    dest_row = int(input())

    km = QueentMove()
    if km.is_knight_move(start_column, start_row, dest_column, dest_row):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
