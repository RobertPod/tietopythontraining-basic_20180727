#!/usr/bin/env python3


class FibonacciNumbers(object):
    def fibonacci_numbers_exception(self, n: int) -> int:
        if n < 0:
            raise FibonacciNumbersException('Input value have to be greater than zero')
        elif n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.fibonacci_numbers_exception(n - 2) + self.fibonacci_numbers_exception(n - 1)


class FibonacciNumbersException(Exception):
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return self.wartosc


def main():
    print('Enter number')
    n = int(input())

    fn = FibonacciNumbers()
    print(fn.fibonacci_numbers_exception(n - 1))


if __name__ == '__main__':
    main()
