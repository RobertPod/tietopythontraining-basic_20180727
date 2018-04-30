#!/usr/bin/env python3


def main():
    print('Enter number of students in first class')
    students1 = int(input())
    print('Enter number of students in second class')
    students2 = int(input())
    print('Enter number of students in third class')
    students3 = int(input())
    print('Minimum number of desks is ' + str(
        minimum_desks(students1) + minimum_desks(students2) + minimum_desks(students3)))


def minimum_desks(students: int):
    return students // 2 + students % 2


if __name__ == '__main__':
    main()
