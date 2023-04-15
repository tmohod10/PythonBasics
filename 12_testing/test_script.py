# to run the unit test using command line
# the file name should start with "test"

# command to run the unittest using command line
# python3 -m unittest -v

import unittest
import main_prog


class TestMain(unittest.TestCase):
    def setUp(self):
        print("This is invoked before every test case")

    def test_do_stuff1(self):
        """Hii there"""
        test_param = 10
        result = main_prog.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "abcd"
        result = main_prog.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = 20.5
        result = main_prog.do_stuff(test_param)
        self.assertEqual(result, 25)

    def test_do_stuff4(self):
        test_param = None
        result = main_prog.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def test_do_stuff5(self):
        test_param = ''
        result = main_prog.do_stuff(test_param)
        self.assertEqual(result, "Please enter a number")

    def tearDown(self):
        print("This is invoked after every test case")


# to run all the test cases
if __name__ == '__main__':
    unittest.main()
