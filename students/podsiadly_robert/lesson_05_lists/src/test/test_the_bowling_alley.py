import unittest

from ..modules.the_bowling_alley import TheBowlingAlley


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tba = TheBowlingAlley()

    def test_no_roll_game(self):
        # given
        pins = 1
        balls = 0

        # when
        rollings = []

        # then
        game_solution = ['I' for i in range(pins)]
        self.assertEqual(game_solution, self.tba.bilard_track(pins, balls, rollings))


if __name__ == '__main__':
    unittest.main()
