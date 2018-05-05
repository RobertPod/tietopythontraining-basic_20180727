import unittest

from lesson_02_flow_control.src.modules.chocolate_bar import ChocolateBar


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = ChocolateBar()

    def test_something(self):
        self.assertEqual(self.cb.possible(4, 2, 6), True)
        self.assertEqual(self.cb.possible(2, 10, 7), False)
        self.assertEqual(self.cb.possible(5, 7, 1), False)
        self.assertEqual(self.cb.possible(7, 4, 21), True)
        self.assertEqual(self.cb.possible(5, 12, 100), False)
        self.assertEqual(self.cb.possible(6, 6, 6), True)
        self.assertEqual(self.cb.possible(6, 6, 35), False)
        self.assertEqual(self.cb.possible(6, 6, 37), False)
        self.assertEqual(self.cb.possible(7, 1, 99), False)
        self.assertEqual(self.cb.possible(300, 100, 3000), True)
        self.assertEqual(self.cb.possible(256, 124, 4069), False)
        self.assertEqual(self.cb.possible(348, 41, 6183), False)
        self.assertEqual(self.cb.possible(387, 13, 2709), True)
        self.assertEqual(self.cb.possible(13, 387, 2709), True)
        self.assertEqual(self.cb.possible(1, 1, 2), False)


if __name__ == '__main__':
    unittest.main()
