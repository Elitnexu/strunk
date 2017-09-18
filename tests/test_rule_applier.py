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


    def test_open_file(self):
        applier = rule_applier.rule_applier(self.rules, self.parser)
        #Valid mode given
        try:
            file = applier.open_file("test.file", "w+")
            file.close()
        except Exception:
            self.fail("Function raised Exception unexpectedly!")

        #Invalid mode specified
        self.assertRaises(
            IOError, lambda: applier.open_file("test.file", "qwerty")
        )
        #TODO: Add shutdown hook for this in filesetup destroy
        os.remove("test.file")

    def test_write_new_file(self):
        applier = rule_applier.rule_applier(self.rules, self.parser)
        self.parser.set_file(self.parser.open_file("tests/test.txt", "r"))
        self.parser.set_file_to_sentences()
        self.parser.set_file_path("test.txt")
        #Applier's parser now has sentences from test.txt in it?

        try:
            applier.write_new_file(self.parser.get_file_path())
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
    
        applier = rule_applier.rule_applier(self.rules, self.parser)
        #Check file is written as is properly
        contents = applier.parser.get_sentences()
        contents[0] = 'this will appear in failed test'

        #Patch environment call, editor method call
        with patch.dict(os.environ, {'EDITOR' : 'vi'}):
            with patch.object(applier, 'open_editor', lambda x,y: None):
                applier.edit_sentence('temp.strunk', 'this is a test', 0)
                #Change contents to updated sentences, assert whether update worked
                contents = applier.parser.get_sentences()
                self.assertEqual(contents[0], 'this is a test')


    def test_handle_rule_match(self):

        applier = rule_applier.rule_applier(self.rules, self.parser)
        #Hack for extracting single rule
        for rule in self.rules:
            rule = self.rules[rule]
            break

        #Check Skip is called
        with patch.object(applier, 'get_input', lambda x: 's'):
            self.assertEqual(applier.handle_rule_match(rule, "test", 0), 'skip')

        #Check Skip All is called
        with patch.object(applier, 'get_input', lambda x: 'a'):
            self.assertEqual(applier.handle_rule_match(rule, "test", 0), 'skip_all')

        #Check Ignore is called
        with patch.object(applier, 'get_input', lambda x: 'i'):
            self.assertEqual(applier.handle_rule_match(rule, "test", 0), "default")

        #Check Edit is called
        with patch.object(applier, 'get_input', lambda x: 'e'):
            with patch.object(applier, 'edit_sentence', lambda x,y,z: None):
                self.assertEqual(applier.handle_rule_match(rule, "test", 0), 'default')
        
    def test_apply_ruleset(self):

        applier = rule_applier.rule_applier(self.rules, self.parser)
        #Setup ruleset appropriately
        #Patch the call to handle rule match
        #Assert each outcome
        with patch.object(applier, 'handle_rule_match', lambda x,y,z: 'skip'):
            self.assertEquals(applier.apply_ruleset(self.rules), None)

        with patch.object(applier, 'handle_rule_match', lambda x,y,z: 'skip_all'):
            self.assertRaises(StopIteration, applier.apply_ruleset(self.rules))

    def test_display_help(self):
        applier = rule_applier.rule_applier(self.rules, self.parser)
        contents = "\n".join([
        "==HELP==\n",
        "[E]dit: Edit the sentence(s) displayed in a text editor\n",
        "[I]gnore: Ignore applying the current rule to the sentence displayed\n",
        "[S]kip: Skip the current rule and start applying next rule\n",
        "Skip [A]ll: Skip all future rules and start writing to file\n",
        "[M]ore Information: Display more information on the current rule\n",
        "[H]elp: Display the Help prompt"])

        self.assertEquals(applier.display_help(), contents)

if __name__ == '__main__':
    unittest.main()
