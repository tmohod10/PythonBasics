import unittest
import main_prog


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
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


# to run all the test cases
if __name__ == '__main__':
    unittest.main()
