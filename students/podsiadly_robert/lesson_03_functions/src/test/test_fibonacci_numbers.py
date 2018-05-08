import unittest

from ..modules.fibonacci_numbers import FibonacciNumbers, FibonacciNumbersException


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fn = FibonacciNumbers()

    def test_input_less_then_zero(self):
        self.assertRaises(FibonacciNumbersException, self.fn.fibonacci_numbers_exception, -1)

    def test_input_not_integer(self):
        self.assertRaises(FibonacciNumbersException, self.fn.fibonacci_numbers_exception, 1.5)

    def test_fibonacci(self):
        self.assertEqual(1, self.fn.fibonacci_numbers_exception(0))
        self.assertEqual(1, self.fn.fibonacci_numbers_exception(1))
        self.assertEqual(2, self.fn.fibonacci_numbers_exception(2))
        self.assertEqual(21, self.fn.fibonacci_numbers_exception(7))
        self.assertEqual(5702887, self.fn.fibonacci_numbers_exception(33))


if __name__ == '__main__':
    unittest.main()
