#!/usr/bin/env python3
import math


def main():
    print('Enter positive real number')
    real_value = float(input())
    print('Fractional part is ' + str(fractional_part(real_value)))


def fractional_part(real_value: float):
    frac, whole = math.modf(real_value)
    return frac


if __name__ == '__main__':
    main()
