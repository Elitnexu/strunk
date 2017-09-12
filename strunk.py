#!/usr/bin/env python3
#==Strunk==
#Author: Marc Hanley
#Commenced: 27/07/2017
#Last modified: 12/09/2017
#
#Description:
#Strunk is a regular expression parser and validator for text files.
#Regular expressions in PCRE format are evaluated against the text file provided
#and for every match found the user is prompted to either edit the file or skip
#the rule.
#Refer to the README for more detailed information.
import sys
import lib.rule_parser.rule as rule
import lib.rule_parser.rule_parser as rule_parser
import lib.file_parser.file_parser as file_parser
import lib.rule_applier.rule_applier as rule_applier

#Read config file from either config folder or args
#if args is file, process, if args is ruleform, use.
#else reject
def strunk(progname, textfile, rulefile):

    #Get dictionary of ruleset
    ruleset = rule_parser.rule_parser(rulefile)
    ruleset.import_ruleset()
    rules = ruleset.get_ruleset()

    #Get input file of text, set up the parser
    parser = file_parser.file_parser(textfile)
    parser.set_ruleset(rules)

    parser.set_file(parser.open_file(parser.filepath, "r"))
    parser.set_file_to_sentences()

    #Apply the rules to the text
    applier = rule_applier.rule_applier(rules, parser)
    applier.apply()

if __name__ == '__main__':
    #Testing
    #args = ("strunk", "gatsby.txt", "")
    #strunk(*args)
    if len(sys.argv) == 2:
        sys.argv.append(None)
    elif len(sys.argv) == 3:
        pass
    else:
        raise ValueError("Invalid argument syntax. Check usage for info.")

    strunk(*sys.argv)
