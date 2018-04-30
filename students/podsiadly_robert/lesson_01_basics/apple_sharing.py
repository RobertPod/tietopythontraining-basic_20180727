#!/usr/bin/env python3


def main():
    print('Enter the number of students')
    students = int(input())
    print('Enter the number of apple')
    apple = int(input())
    print('Each student get ' + str(how_many_apple_student_get(apple, students)) + ' apple')
    print('In basket remain ' + str(how_many_apple_remain(apple, students)) + ' apple')


def how_many_apple_student_get(apple: int, students: int):
    return apple // students


def how_many_apple_remain(apple: int, students: int):
    return apple % students


if __name__ == '__main__':
    main()
