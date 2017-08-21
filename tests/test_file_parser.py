import unittest
import file_setup
import lib.file_parser.file_parser as file_parser
#import os

class FileParserTest(unittest.TestCase):
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

    def test_process_line(self):
        #Setup for process line
        #parser.set_file(testfile)
        index = 4
        #Current processed sentence
        sentence = "george ate dinner at"
        delim_exp = r'.+[!?.].*'

        #A line is equivalent to no character (after strip)
        line = "\n"
        self.assertEqual(
        "george ate dinner at", \
        self.parser.process_line(index, line, sentence, delim_exp)
        )
        #A line is a delimited sentences (first index)
        sentence = "george ate dinner at"
        line = " the restaurant."
        self.assertEqual(
        "george ate dinner at the restaurant.", \
        self.parser.process_line(index, line, sentence, delim_exp)
        )
        #A line is a delimited sentence (not first index)
        line = "george ate dinner at the restaurant. It was delicious. Even though "
        self.assertEqual(
        "Even though ", \
        self.parser.process_line(index, line, sentence, delim_exp)
        )
        #A line is a delimited sentence (multiple on this line)

        #A line is not a delimited sentence

        #A line is
        #Test each type of expected return



if __name__ == '__main__':
    unittest.main()
