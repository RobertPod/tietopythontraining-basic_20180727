import unittest

from lesson_02_flow_control.src.modules.queen_move import QueentMove


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.qm = QueentMove()

    def test_something(self):
        self.assertEqual(self.qm.is_queen_move(1, 1, 2, 2), True)
        self.assertEqual(self.qm.is_queen_move(1, 1, 2, 3), False)
        self.assertEqual(self.qm.is_queen_move(5, 6, 3, 3), False)
        self.assertEqual(self.qm.is_queen_move(3, 3, 1, 1), True)
        self.assertEqual(self.qm.is_queen_move(6, 5, 2, 5), True)

        self.assertEqual(self.qm.is_queen_move(7, 6, 5, 2), False)
        self.assertEqual(self.qm.is_queen_move(2, 7, 6, 7), True)
        self.assertEqual(self.qm.is_queen_move(2, 7, 4, 6), False)
        self.assertEqual(self.qm.is_queen_move(7, 4, 2, 5), False)
        self.assertEqual(self.qm.is_queen_move(7, 5, 1, 1), False)

        self.assertEqual(self.qm.is_queen_move(2, 4, 5, 7), True)
        self.assertEqual(self.qm.is_queen_move(3, 5, 7, 1), True)
        self.assertEqual(self.qm.is_queen_move(5, 2, 5, 8), True)
        self.assertEqual(self.qm.is_queen_move(1, 2, 3, 1), False)
        self.assertEqual(self.qm.is_queen_move(2, 1, 1, 3), False)


if __name__ == '__main__':
    unittest.main()
