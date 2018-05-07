#!/usr/bin/env python3
from math import fabs


class ReplaceWithinTheFragment(object):
    def replace_within_the_fragment(self, input_string: str) -> str:
        len_input_string = len(input_string)
        count_h = input_string.count('h')
        if count_h < 3:
            return input_string

        changed_h = 0
        output_string: str = ''
        for i in range(len_input_string):
            if input_string[i] == 'h':
                changed_h += 1
                if changed_h == 1 or changed_h == count_h:
                    output_string += input_string[i]
                else:
                    output_string += 'H'
            else:
                output_string += input_string[i]

        return output_string


def main():
    print('Enter string')
    input_string = input()
    rwtf = ReplaceWithinTheFragment()
    print(rwtf.replace_within_the_fragment(input_string))


if __name__ == '__main__':
    main()
