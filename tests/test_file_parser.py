import unittest
import os
import file_setup
import strunk.file_parser.file_parser as file_parser
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
            file = self.parser.open_file("test.file", "w+")
            file.truncate(0)
            file.close()
        except Exception:
            self.fail("Function raised Exception unexpectedly!")

        #Invalid mode specified
        self.assertRaises(
        IOError, lambda: self.parser.open_file("test.file", "qwerty")
        )
        #Cleanup
        os.remove("test.file")

    def test_set_file_to_sentences(self):
        #Set file to some set of sentences
        #Run test case
        #Assert sentences returned equal to original file contents
        test_contents = "This is a test sentence.\n" \
                        + "It will have three lines!\n" \
                        + "This is the third? I'd say so."
        self.parser.set_file(test_contents)

        #File contents is read correctly into sentences list
        self.parser.set_file_to_sentences()
        self.assertEqual("".join(self.parser.get_sentences()), test_contents)

if __name__ == '__main__':
    unittest.main()
