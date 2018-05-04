import unittest
from app.chocolate_bar import ChocolateBar


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cb = ChocolateBar()

    def test_something(self):
        result = self.cb.possible(4, 2, 6)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
