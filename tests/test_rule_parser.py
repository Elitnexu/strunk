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

    def test_import_ruleset(self):
        pass


if __name__ == '__main__':
    unittest.main()
