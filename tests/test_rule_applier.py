import unittest
import file_setup
import lib.file_parser.file_parser as file_parser
import lib.rule_parser.rule_parser as rule_parser
import lib.rule_applier.rule_applier as rule_applier
#import os

class RuleApplierTest(unittest.TestCase):
    #Setup and destroy
    #>>whatever values required
    #global ruleset
    #global testfile
    parser = file_parser.file_parser(None)
    data = file_setup.generate_file_data()
    file_setup.setup_test_file("tests/test.txt", data)
    parser.set_file(parser.open_file("tests/test.txt", "r"))
    parser.set_file_to_sentences()

    ruleset = rule_parser.rule_parser(None)
    data = file_setup.generate_strunk_data()
    file_setup.setup_test_file("tests/tests.strunk", data)
    #TODO Come back here when fixing rule parser get strunk path
    ruleset.args = "tests/tests"
    ruleset.import_ruleset()
    rules = ruleset.get_ruleset()

    #applier = rule_applier.rule_applier(rules, parser)

    def test_open_file(self):
        #Valid mode given
        try:
            file = rule_applier.open_file("test.file", "w+")
            file.close()
        except Exception:
            self.fail("Function raised Exception unexpectedly!")
            #print("Function raised Exception unexpectedly!")

        #Invalid mode specified
        self.assertRaises(
        IOError, lambda: rule_applier.open_file("test.file", "qwerty")
        )

    def test_apply_ruleset(self):
        pass

    def test_handle_rule_match(self):
        pass

    def test_edit_sentence(self):
        pass

    def test_write_new_file(self):
        pass

if __name__ == '__main__':
    unittest.main()
