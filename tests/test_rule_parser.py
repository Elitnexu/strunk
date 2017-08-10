import unittest
import rule_parser
#import os

class RuleParserTest(unittest.TestCase):
    #Setup and destroy
    #>>whatever values required
    global ruleset
    global testfile
    ruleset = rule_parser.rule_parser(None)
    #Replace with function that fills in data
    testfile = open("tests/tests.strunk", "r")

    def test_get_file_type(self):
        #No argument given, so return the default file
        ruleset.args = None
        self.assertEqual(
        ruleset.get_file_type(), ".strunk"
        )

        #Argument is custom filename
        ruleset.args = "tests/tests"
        self.assertEqual(
        ruleset.get_file_type(), "tests/tests.strunk"
        )

        #Argument is invalid file
        ruleset.args = "tests/noexist"
        self.assertRaises(
        ValueError, lambda: ruleset.get_file_type()
        )

    def test_process_ruleset(self):
        #Preparation for tests
        ruleset.args = "tests/tests"
        filepath = ruleset.get_file_type()

        #Ruleset is parsed successfully
        ruleset.process_ruleset(filepath)

        #Ruleset syntax is invalid
        ruleset.args = "tests/failed_test"
        filepath = ruleset.get_file_type()

        self.assertRaises(
        SyntaxError, lambda: ruleset.process_ruleset(filepath)
        )

        #Ruleset file specified not found
        self.assertRaises(
        IOError, lambda: ruleset.process_ruleset(filepath + ".shouldnotexist")
        )

if __name__ == '__main__':
    unittest.main()
