# To run all the testcases in a folder: python -m unittest
# With verbose: python -m unittest -v

import unittest
from main import add


class TestMain(unittest.TestCase):
    def setUp(self):
        print('setUp() function is called before each test method')

    def test_add(self):
        '''
        CHECK 1: Default check with INT paramters
        '''
        param1 = 5
        param2 = 10
        result = add(param1, param2)
        self.assertEqual(result, 15)

    def test_add2(self):
        '''
        CHECK2: STRING type and INT type
        '''
        param1 = 'ABC'
        param2 = 5
        result = add(param1, param2)
        self.assertIsInstance(result, TypeError)

    def test_add3(self):
        '''
        CHECK 3: NONE and INT parameter
        '''
        param1 = None
        param2 = 5
        result = add(param1, param2)
        self.assertIsInstance(result, TypeError)

    def test_add4(self):
        '''
        CHECK 4: INT and no paramter value is passed
        '''
        param1 = 5
        result = add(param1)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('teardown() method is called after every test method')


if __name__ == '__main__':
    unittest.main()
