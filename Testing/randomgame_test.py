import unittest
from randomgame import is_the_guess_correct


class TestRandomGame(unittest.TestCase):
    def test_input_equal(self):
        result = is_the_guess_correct(2, 2, 1, 2)
        self.assertTrue(result)

    def test_input_not_equal(self):
        result = is_the_guess_correct(1, 2, 1, 2)
        self.assertFalse(result)

    def test_input_wrong_guess(self):
        result = is_the_guess_correct(3, 2, 1, 2)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
