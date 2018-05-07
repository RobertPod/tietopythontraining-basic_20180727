#!/usr/bin/env python3
from math import fabs


class LostCard(object):
    def get_lost_card_number(self, number_of_cards: int, table_of_cards: []) -> int:
        deck = []
        for i in range(number_of_cards + 1):
            deck.append(0)
        for i in range(number_of_cards - 1):
            deck[table_of_cards[i]] = 1
        for i in range(1, number_of_cards + 1):
            if deck[i] == 0:
                return i
        return 0


def main():
    table_of_cards = []
    print('Enter number of cards')
    number_of_cards = int(input())
    for i in range(number_of_cards - 1):
        table_of_cards.append(int(input()))

    lc = LostCard()
    print(lc.get_lost_card_number(number_of_cards, table_of_cards))


if __name__ == '__main__':
    main()
