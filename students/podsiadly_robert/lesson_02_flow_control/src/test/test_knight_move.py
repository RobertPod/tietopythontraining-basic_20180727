import unittest

from lesson_02_flow_control.src.modules.knight_move import KnightMove


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.km = KnightMove()

    def test_something(self):
        self.assertEqual(self.km.is_knight_move(1, 1, 1, 4), False)
        self.assertEqual(self.km.is_knight_move(1, 1, 8, 8), False)
        self.assertEqual(self.km.is_knight_move(2, 4, 3, 2), True)
        self.assertEqual(self.km.is_knight_move(5, 2, 4, 4), True)
        self.assertEqual(self.km.is_knight_move(2, 8, 3, 7), False)
        self.assertEqual(self.km.is_knight_move(2, 8, 3, 5), False)
        self.assertEqual(self.km.is_knight_move(5, 5, 3, 7), False)
        self.assertEqual(self.km.is_knight_move(2, 4, 2, 5), False)
        self.assertEqual(self.km.is_knight_move(4, 7, 6, 6), True)
        self.assertEqual(self.km.is_knight_move(4, 5, 2, 4), True)
        self.assertEqual(self.km.is_knight_move(2, 3, 3, 2), False)
        self.assertEqual(self.km.is_knight_move(5, 1, 4, 3), True)
        self.assertEqual(self.km.is_knight_move(6, 2, 8, 3), True)


if __name__ == '__main__':
    unittest.main()
