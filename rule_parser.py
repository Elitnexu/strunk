#Rule Parser handles the ruleset given, opening and extracting from the
#ruleset file or command and placing all valid entries into a dictionary.
#The dictionary is then used as a matcher when compared against the text file
#input.

import os.path
import re
import rule

class rule_parser:

    def __init__(self, args):
        self.args = args
        #Instance variables
        self.DEFAULT_RULE_FILE = ".strunk"
        self.ruleset = None
        #self.NEXT_EXPECTED_TYPE = {'EXP', 'ACT', 'SUB', 'INFO'}

    #Get the ruleset from this event, returns None if unassigned
    #@return The ruleset currently assigned to the parser
    def get_ruleset(self):
        return self.ruleset

    #Process the ruleset file given and converts to a dictionary
    #for applying to a text file.
    #@filepath: a .strunk filepath
    #@return A dictionary of keywords, behaviour and comments
    def process_ruleset(self, filepath):

        try:
            file = open(filepath, "r")
        except:
            raise IOError("Rulefile failed to open")

        empty = "".strip()
        next_expected = "EXP"
        rules = []
        new_rule = None
        spaces = 0

        for line in file:
            #Remove leading/trailing whitespace and newlines
            line = line.strip()
            print next_expected
            print line

            rules.append(new_rule)
            if line == "END": #EOF, deal with better TODO
                new_rule = None
                next_expected = "EXP"
                spaces = 0
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
                new_rule.set_action = line
                next_expected = "SUB"
                continue
            #Handle subject type
            if next_expected == "SUB":
                new_rule.set_subject = line
                next_expected = "INFO"
                continue
            #Handle information
            if next_expected == "INFO":
                #Reached the end of info, next rule, fix if statements
                if spaces == 1 and line == "":
                    rules.append(new_rule)
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
                raise Error("Why are you here? Line = " + line)
        return rules


    #Finds the appropriate response to the type of input expected
    #i.e. given rule, ruleset file, etc. and outputs either a filepath
    #or a TODO whatever I end up doing with explicit regex
    #@return string containing a filepath or regex
    def get_file_type(self):
        if self.args is None:
            #Check for config file
            print "Default rule file specified."
            if os.path.isfile(self.DEFAULT_RULE_FILE):
                print "Default rule file detected."
                return self.DEFAULT_RULE_FILE
            else:
                #Raise error? Create default?
                raise IOError("Default rule file " + self.DEFAULT_RULE_FILE + " not found")

        #Either custom ruleset or regex. Check ruleset first.
        else:
            #Check if custom ruleset exists
            print "Custom ruleset specified."
            custom_ruleset = self.args + ".strunk"
            if os.path.isfile(custom_ruleset):
                print "Custom ruleset file detected."
                return custom_ruleset

            #Check if args matches ruleform (regxp)
            if re.match(r"\(.*\),\(.*\),\(.*\)", self.args) is not None:
                print "RegEx matches."
                #Maybe change to specify whether regex, filename?
                return "Explicit regex"
            else:
                raise ValueError("No valid rules found. Check your syntax!")

    #Sets ruleset to imported file
    def import_ruleset(self):
        filepath = self.get_file_type()
        if filepath == "Explicit regex":
            #TODO Handle explicit rule
            contents = "Explicit regex"
        else:
            #Open the file and start reading in data
            contents = self.process_ruleset(filepath)

        self.ruleset = contents
