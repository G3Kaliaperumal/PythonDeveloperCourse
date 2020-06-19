import unittest
from main import add


class TestMain(unittest.TestCase):
    def test_add(self):
        param1 = 5
        param2 = 10
        result = add(param1, param2)
        self.assertEqual(result, 15)

    def test_add2(self):
        param1 = 'ABC'
        param2 = 5
        result = add(param1, param2)
        self.assertIsInstance(result, TypeError)

    def test_add3(self):
        param1 = None
        param2 = 5
        result = add(param1, param2)
        self.assertIsInstance(result, TypeError)

    def test_add4(self):
        param1 = 5
        result = add(param1)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
