#!/usr/bin/env python3
#==Strunk==
#Author: Marc Hanley
#Commenced: 27/07/2017
#Last modified: 15/09/2017
#
#Description:
#Strunk is a regular expression parser and validator for text files.
#Regular expressions in PCRE format are evaluated against the text file provided
#and for every match found the user is prompted to either edit the file or skip
#the rule.
#Refer to the README for more detailed information.
import sys
import lib.rule_parser.rule_parser as rule_parser
import lib.file_parser.file_parser as file_parser
import lib.rule_applier.rule_applier as rule_applier

#Main program function
def strunk(progname, textfile, rulefile):

    #Get dictionary of ruleset
    ruleset = rule_parser.rule_parser(rulefile)
    ruleset.import_ruleset()
    rules = ruleset.get_ruleset()

    #Instantiate parser, set ruleset specified
    parser = file_parser.file_parser(textfile)
    parser.set_ruleset(rules)

    #Open specified text file and load contents
    parser.set_file(parser.open_file(parser.filepath, "r"))
    parser.set_file_to_sentences()

    #Apply the rules to the text
    applier = rule_applier.rule_applier(rules, parser)
    applier.apply()

if __name__ == '__main__':

    #TODO: Come back here
    if len(sys.argv) == 2:
        sys.argv.append(None)
    elif len(sys.argv) == 3:
        pass
    else:
        print("Invalid argument syntax. Format is: strunk <text file> <strunk file>")
        sys.exit()

    strunk(*sys.argv)
