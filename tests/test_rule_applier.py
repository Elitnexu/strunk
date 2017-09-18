import os
import unittest
import subprocess
from mock import patch, PropertyMock #Python 2.7 Compatibility
import tests.file_setup as file_setup
import strunk.file_parser.file_parser as file_parser
import strunk.rule_parser.rule_parser as rule_parser
import strunk.rule_applier.rule_applier as rule_applier

class RuleApplierTest(unittest.TestCase):
    #Setup and destroy
    #>>whatever values required
    #global ruleset
    #global testfile
    parser = file_parser.file_parser("tests/test.txt")
    data = file_setup.generate_file_data()
    file_setup.setup_test_file("tests/test.txt", data)
    parser.set_file(parser.open_file("tests/test.txt", "r"))
    parser.set_file_to_sentences()

    ruleset = rule_parser.rule_parser(None)
    data = file_setup.generate_strunk_data()
    file_setup.setup_test_file("tests/tests.strunk", data)
    #TODO Come back here when fixing rule parser get strunk path
    ruleset.args = "tests/tests.strunk"
    ruleset.import_ruleset()
    rules = ruleset.get_ruleset()

    applier = rule_applier.rule_applier(rules, parser)

    def test_open_file(self):
        #Valid mode given
        try:
            file = self.applier.open_file("test.file", "w+")
            file.close()
        except Exception:
            self.fail("Function raised Exception unexpectedly!")

        #Invalid mode specified
        self.assertRaises(
            IOError, lambda: self.applier.open_file("test.file", "qwerty")
        )
        #TODO: Add shutdown hook for this in filesetup destroy
        os.remove("test.file")

    def test_write_new_file(self):
        self.parser.set_file(self.parser.open_file("tests/test.txt", "r"))
        self.parser.set_file_to_sentences()
        self.parser.set_file_path("test.txt")
        #Applier's parser now has sentences from test.txt in it?

        try:
            self.applier.write_new_file(self.parser.get_file_path())
        except Exception:
            self.fail("Applier failed to write new file!")

        #Open newly Strunked text file
        file = ""
        try:
            file = self.parser.open_file("strunked_test.txt", "r")
        except Exception:
            self.fail("Strunked Text File failed to open!")

        test_sentences = self.parser.get_sentences()
        self.parser.set_file(file)
        self.parser.set_file_to_sentences()

        #Strunked File should equal pre-write file
        self.assertEqual(test_sentences, self.parser.get_sentences())

    def test_edit_sentence(self):
    #Check file is written as is properly
        contents = self.applier.parser.get_sentences()
        contents[0] = 'this will appear in failed test'

        #Patch environment call, editor method call
        with patch.dict(os.environ, {'EDITOR' : 'vi'}):
            with patch.object(self.applier, 'open_editor', lambda x,y: None):
                self.applier.edit_sentence('temp.strunk', 'this is a test', 0)
                contents = self.applier.parser.get_sentences()
                self.assertEqual(contents[0], 'this is a test')


    def test_handle_rule_match(self):
        #Hack for extracting single rule
        for rule in self.rules:
            rule = self.rules[rule]
            break

        #Check Skip is called
        with patch.object(self.applier, 'get_input', lambda x: 's'):
            self.assertEqual(self.applier.handle_rule_match(rule, "test", 0), 'skip')

        #Check Skip All is called
        with patch.object(self.applier, 'get_input', lambda x: 'a'):
            self.assertEqual(self.applier.handle_rule_match(rule, "test", 0), 'skip_all')
        
        #Check Edit is called
        with patch.object(self.applier, 'get_input', lambda x: 'e'):
            with patch.object(self.applier, 'edit_sentence', lambda x,y,z: None):
                self.assertEqual(self.applier.handle_rule_match(rule, "test", 0), 'default')
    
    

if __name__ == '__main__':
    unittest.main()
