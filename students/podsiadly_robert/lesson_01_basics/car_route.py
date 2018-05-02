#!/usr/bin/env python3
import math


def main():
    print('Enter the distance covered by day')
    day_distance = int(input())
    print('Enter the route length')
    distance = int(input())
    print('Car need ' + str(count_days(day_distance, distance)) + ' days')


def count_days(day_distance: int, distance: int):
    return math.ceil(distance / day_distance)


if __name__ == '__main__':
    main()
