#!/usr/bin/env python3
from math import fabs


class DeleteEveryThirdCharacter(object):
    def delete_every_third_character(self, input_string: str) -> str:
        len_input_string = len(input_string)
        output_string : str = ''
        for i in range(len_input_string):
            if i % 3 != 0:
                output_string += input_string[i]
        return output_string


def main():
    print('Enter string')
    input_string = input()
    deth = DeleteEveryThirdCharacter()
    print(deth.delete_every_third_character(input_string))


if __name__ == '__main__':
    main()
