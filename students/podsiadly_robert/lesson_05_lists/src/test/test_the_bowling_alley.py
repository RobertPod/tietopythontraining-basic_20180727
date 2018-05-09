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

    def test_one_roll_game(self):
        # given
        pins = 2
        balls = 1

        # when
        rollings = [[1, 1]]

        # then
        game_solution = ['.', 'I']
        self.assertEqual(game_solution, self.tba.bilard_track(pins, balls, rollings))

    def test_games(self):
        # given
        pins = 10
        balls = 3
        # when
        rollings = [[8, 10], [2, 5], [3, 6]]
        # then
        game_solution = ['I', '.', '.', '.', '.', '.', 'I', '.', '.', '.']
        self.assertEqual(game_solution, self.tba.bilard_track(pins, balls, rollings))

        # given
        pins = 5
        balls = 2
        # when
        rollings = [[1, 2], [4, 4], [3, 6]]
        # then
        game_solution = ['.', '.', 'I', '.', 'I']
        self.assertEqual(game_solution, self.tba.bilard_track(pins, balls, rollings))

        # given
        pins = 20
        balls = 1
        # when
        rollings = [[1, 20]]
        # then
        game_solution = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                         '.']
        self.assertEqual(game_solution, self.tba.bilard_track(pins, balls, rollings))

        # given
        pins = 20
        balls = 3
        # when
        rollings = [[3, 8], [13, 17], [6, 9]]
        # then
        game_solution = ['I', 'I', '.', '.', '.', '.', '.', '.', '.', 'I', 'I', 'I', '.', '.', '.', '.', '.', 'I', 'I',
                         'I']
        self.assertEqual(game_solution, self.tba.bilard_track(pins, balls, rollings))


if __name__ == '__main__':
    unittest.main()
