import unittest

from lesson_02_flow_control.src.modules.lost_card import LostCard


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.lc = LostCard()

    def test_get_lost_card_number_1(self):
        number_of_cards = 5
        table_of_cards = [1, 2, 3, 4]
        self.assertEqual(5, self.lc.get_lost_card_number(number_of_cards, table_of_cards))

    def test_get_lost_card_number_2(self):
        number_of_cards = 5
        table_of_cards = [3, 5, 2, 1]
        self.assertEqual(4, self.lc.get_lost_card_number(number_of_cards, table_of_cards))

    def test_get_lost_card_number_7(self):
        number_of_cards = 1
        table_of_cards = []
        self.assertEqual(1, self.lc.get_lost_card_number(number_of_cards, table_of_cards))

    def test_get_lost_card_number_8(self):
        number_of_cards = 10
        table_of_cards = [4, 1, 7, 8, 3, 5, 9, 10, 6]
        self.assertEqual(2, self.lc.get_lost_card_number(number_of_cards, table_of_cards))


if __name__ == '__main__':
    unittest.main()
