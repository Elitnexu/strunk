import unittest
import file_setup
import lib.file_parser.file_parser as file_parser
#import os

class RuleApplierTest(unittest.TestCase):
    #Setup and destroy
    #>>whatever values required
    #global ruleset
    #global testfile
    parser = file_parser.file_parser(None)
    data = file_setup.generate_file_data()
    file_setup.setup_test_file("tests/test.txt", data)
    testfile = open("tests/test.txt", "r")
    #Replace with function that fills in data
    #testfile = open("tests/tests.strunk", "r")

    def test_open_file(self):
        #Valid mode given
        try:
            file = parser.open_file("test.file", "w+")
            file.close()
        except Exception:
            #self.fail("Function raised Exception unexpectedly!")
            print("Function raised Exception unexpectedly!")

        #Invalid mode specified
        self.assertRaises(
        IOError, lambda: self.parser.open_file("test.file", "qwerty")
        )

    def test_another_test(self):



if __name__ == '__main__':
    unittest.main()
