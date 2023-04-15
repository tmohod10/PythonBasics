import unittest
import guessing_game_for_testing as g


class GuessingGameTest(unittest.TestCase):
    def test_for_correct_input(self):
        first_num = 1
        last_num = 2
        guess = 2
        result = g.run_guess(first_num, last_num, guess, 2)
        self.assertTrue(result)

    def test_for_wrong_input2(self):
        first_num = 1
        last_num = 2
        guess = 2
        result = g.run_guess(first_num, last_num, guess, 0)
        self.assertFalse(result)

    def test_for_incorrect_range_guess(self):
        first_num = 1
        last_num = 2
        guess = 20
        result = g.run_guess(first_num, last_num, guess, 2)
        self.assertFalse(result)

    def test_for_incorrect_input(self):
        first_num = 1
        last_num = 2
        guess = 20
        result = g.run_guess(first_num, last_num, guess, '2')
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
