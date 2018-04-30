#!/usr/bin/env python3


def main():
    print('Enter the length of the triangle base')
    base = int(input())
    print('Enter the height of the triangle')
    height = int(input())
    print('Area of tringle is ' + str(area_of_right_angled_triangle(base, height)))


def area_of_right_angled_triangle(base: int, height: int):
    return (base * height) / 2


if __name__ == '__main__':
    main()
