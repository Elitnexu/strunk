import unittest
import tests.file_setup as file_setup
import strunk.rule_parser.rule_parser as rule_parser
#import os

class RuleParserTest(unittest.TestCase):
    #Setup and destroy
    #>>whatever values required
    global ruleset
    global testfile
    ruleset = rule_parser.rule_parser(None)
    #Replace with function that fills in data
    data = file_setup.generate_strunk_data()
    file_setup.setup_test_file("tests/tests.strunk", data)
    testfile = open("tests/tests.strunk", "r")

    def test_get_strunk_path(self):
        #No argument given, so return the default file
        ruleset.args = None
        self.assertEqual(
        ruleset.get_strunk_path(), ".strunk"
        )

        #Argument is custom filename
        ruleset.args = "tests/tests.strunk"
        self.assertEqual(
        ruleset.get_strunk_path(), "tests/tests.strunk"
        )

        #Argument is invalid file
        ruleset.args = "tests/noexist.strunk"
        self.assertRaises(
        ValueError, lambda: ruleset.get_strunk_path()
        )

    def test_process_ruleset(self):
        #Preparation for tests
        ruleset.args = "tests/tests.strunk"
        filepath = ruleset.get_strunk_path()

        #Ruleset is parsed successfully
        ruleset.process_ruleset(filepath)

        #Ruleset syntax is invalid
        ruleset.args = "tests/failed_test.strunk"
        filepath = ruleset.get_strunk_path()

        self.assertRaises(
        SyntaxError, lambda: ruleset.process_ruleset(filepath)
        )

        #Ruleset file specified not found
        self.assertRaises(
        IOError, lambda: ruleset.process_ruleset(filepath + ".shouldnotexist")
        )

if __name__ == '__main__':
    unittest.main()
