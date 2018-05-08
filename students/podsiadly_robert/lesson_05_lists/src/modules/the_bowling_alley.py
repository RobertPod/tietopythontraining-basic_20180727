#!/usr/bin/env python3


class TheBowlingAlley(object):
    def bilard_track(self, pins, rolls, rolls_description) -> []:

        if type(pins) != int or pins < 1:
            raise BowlingException('ERROR: the variable pins must be a positive natural number')
        if type(rolls) != int or rolls < 0:
            raise BowlingException('ERROR: the rolls variable must be a nonnegative natural number')

        output_tab = ['I' for i in range(pins)]

        return output_tab


class BowlingException(Exception):
    def __init__(self, wartosc):
        self.wartosc = wartosc

    def __str__(self):
        return self.wartosc


def main():
    tba = TheBowlingAlley()
    print(tba.bilard_track(6, 1, [[2, 3], [3, 4]]))


if __name__ == '__main__':
    main()
