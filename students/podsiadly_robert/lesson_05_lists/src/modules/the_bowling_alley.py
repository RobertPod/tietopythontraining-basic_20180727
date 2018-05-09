#!/usr/bin/env python3


class TheBowlingAlley(object):
    def bilard_track(self, pins, rolls, rolls_description) -> []:

        if type(pins) != int or pins < 1:
            raise BowlingException('ERROR: the variable pins must be a positive natural number')
        if type(rolls) != int or rolls < 0:
            raise BowlingException('ERROR: the rolls variable must be a nonnegative natural number')

        output_tab = ['I' for i in range(pins)]
        if len(rolls_description) < rolls:
            raise BowlingException(
                'ERROR: wrong roll description, there are %s rols instead %s' % (len(rolls_description), rolls))

        for i in range(rolls):
            if len(rolls_description[i]) < 2:
                raise BowlingException('ERROR: wrong roll description')
            if rolls_description[i][0] <= 0 or rolls_description[i][0] > pins:
                raise BowlingException('ERROR: wrong roll description')
            if rolls_description[i][1] <= 0 or rolls_description[i][1] > pins:
                raise BowlingException('ERROR: wrong roll description')

            for j in range(rolls_description[i][0] - 1, rolls_description[i][1]):
                output_tab[j] = '.'

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
