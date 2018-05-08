#!/usr/bin/env python3


class CommaCode(object):
    def list2formatted_string(self, input_list: []) -> str:
        output_str = ''
        input_list_len = len(input_list)
        if input_list_len < 1:
            pass
        elif input_list_len == 1:
            output_str = input_list[0]
        else:
            for i in range(input_list_len):
                output_str += input_list[i]
                if i == input_list_len - 2:
                    output_str += ' and '
                elif i < input_list_len - 2:
                    output_str += ', '
        return output_str


def main():
    input_list = ['ola']
    cc = CommaCode()
    print(cc.list2formatted_string(input_list))


if __name__ == '__main__':
    main()
