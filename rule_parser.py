#Ruleset (to be replaced with some other file format)
import os.path
import re

class rule_parser:

    def __init__(self, args):
        self.args = args
        #Instance variables
        self.DEFAULT_RULE_FILE = ".strunk"
        self.ACTIONS = {
        "delete", "replace with %s", "flag"
        }

    def process_file(self, filepath):

        try:
            file = open(filepath, "r")
        except:
            raise IOError("File failed to open")

        #Bug: need to remove \n error
        d = {}
        i = 0
        for line in file:
            d[i] = line
            i = i + 1

        return d

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

    def get_ruleset(self):
        #Main flow
        filepath = self.get_file_type()
        if filepath == "Explicit regex":
            #TODO Handle explicit rule
            contents = "Explicit regex"
        else:
            #Open the file and start reading in data
            contents = self.process_file(filepath)

        return contents
