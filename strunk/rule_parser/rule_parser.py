from __future__ import print_function
from __future__ import absolute_import
#Rule Parser handles the ruleset given, opening and extracting from the
#ruleset file or command and placing all valid entries into a dictionary.
#The dictionary is then used as a matcher when compared against the text file
#input.
#Rule Parser takes multiple rulesets? Extension? Consider leaving this
#option open while designing interface
from builtins import object
import sys
import os.path
from . import rule

class rule_parser(object):

    def __init__(self, args):
        self.args = args
        #Instance variables
        self.DEFAULT_RULE_FILE = ".strunk"
        self.ruleset = None

    #Get the ruleset from this event, returns None if unassigned
    #@return The ruleset currently assigned to the parser
    def get_ruleset(self):
        return self.ruleset

    def open_file(self, filepath, mode):
        try:
            return open(filepath, mode)
        except:
            raise IOError("File at " + filepath + " failed to open")

    #Process the ruleset file given and converts to a dictionary
    #for applying to a text file.
    #@filepath: a .strunk filepath
    #@return A dictionary of keywords, behaviour and comments
    def process_ruleset(self, filepath):
        #Open file
        file = self.open_file(filepath, "r")

        next_expected = "EXP"
        rules = {}
        new_rule = None
        spaces = 0
        exp_key = None
        ended = False

        for line in file:
            ended = False
            #Remove leading/trailing whitespace and newlines
            line = line.strip()

            #rules.append(new_rule)
            if line == "END": #EOF, cleanup and continue
                rules[exp_key] = new_rule
                new_rule = None
                next_expected = "EXP"
                spaces = 0
                ended = True
                continue
            #Ignore comments
            if line[:1] == '#':
                continue
            #Handle expression
            if next_expected == "EXP":
                exp_key = line
                new_rule = rule.rule(exp_key)
                next_expected = "ACT"
                continue
            #Handle action type
            if next_expected == "ACT":
                new_rule.set_action(line)
                next_expected = "SUB"
                continue
            #Handle subject type
            if next_expected == "SUB":
                new_rule.set_subject(line)
                next_expected = "INFO"
                continue
            #Handle information
            if next_expected == "INFO":
                #Check if reached the end of INFO lines
                if spaces == 1 and line == "":
                    rules[exp_key] = new_rule
                    new_rule = None
                    next_expected = "EXP"
                    spaces = 0
                    continue
                elif line == "":
                    new_rule.append_info(line)
                    spaces = 1
                    continue
                else:
                    new_rule.append_info(line)
                    spaces = 0
                    continue
                    #Keep going until double space
            #Somehow you got here
            else:
                raise ValueError("Why are you here? Line = " + line)
        if ended:
            return rules
        else:
            raise SyntaxError("Rule file ended unexpectedly. Check .strunk file syntax.")

    #Finds the appropriate response to the type of input expected
    #i.e. given rule, ruleset file, etc. and outputs a filepath
    #@return string containing a filepath
    def get_strunk_path(self):
        if self.args is None:
            #Check for default file
            print("Default rule file specified.")
            if os.path.isfile(self.DEFAULT_RULE_FILE):
                print("Default rule file detected.")
                return self.DEFAULT_RULE_FILE
            else:
                #Raise error? Create default?
                print("Default rule file " + self.DEFAULT_RULE_FILE + " not found")
                sys.exit()

        #Either custom ruleset or syntax error. Check ruleset first.
        else:
            #Check if custom ruleset exists
            print("Custom ruleset specified.")
            custom_ruleset = self.args
            print(custom_ruleset)
            if os.path.isfile(custom_ruleset):
                print("Custom ruleset file detected.")
                return custom_ruleset
            else:
                raise ValueError("No valid rules found. Check your syntax!")

    #Sets ruleset to imported file
    def import_ruleset(self):
        #Get the path to specified (or not) rulefile
        filepath = self.get_strunk_path()
        #Open the file and start reading in data
        contents = self.process_ruleset(filepath)

        self.ruleset = contents
