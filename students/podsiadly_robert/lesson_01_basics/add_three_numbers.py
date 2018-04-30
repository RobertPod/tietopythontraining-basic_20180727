#!/usr/bin/env python3

"""The `hello_world.py` approach is good for simple scripts, where the code is
unlikely to be reused.

As soon as you want to import and use your code from other modules, you want
to make sure it runs only when asked to. To do that we check magic variable
__name__, set by the interpreter. If the script has been called directly,
the variable holds '__main__' string.
"""


def main():
    print('Enter first number')
    num1 = int(input())
    print('Enter second number')
    num2 = int(input())
    print('Enter third number')
    num3 = int(input())
    print('Sum of three nubers is ' + str(num1 + num2 + num3))


if __name__ == '__main__':
    main()
