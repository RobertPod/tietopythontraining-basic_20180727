#!/usr/bin/env python3
import math


def main():
    print('Enter the number minutes')
    minutes = int(input())
    print(str((minutes // 60) % 24) + ' ' + str(minutes % 60))


if __name__ == '__main__':
    main()
