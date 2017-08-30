#!/usr/bin/env python3
#Takes text and ruleset, outputs results to file
import lib.rule_parser.rule_parser as rule_parser
import lib.file_parser.file_parser as file_parser
import lib.rule_applier.rule_applier as rule_applier
import lib.rule_parser.rule as rule
import sys

#Read in config file
#Prepare text file
#For each line of file, check for instance of keyword
#If found, process based on behaviour
#Upon completion, write each suggestion to file
def strunk(progname, textfile, rulefile):
    #Read config file from either config folder or args
    #if args is file, process, if args is ruleform, use.
    #else reject

    #Get dictionary of ruleset (if we make it that far)
    ruleset = rule_parser.rule_parser(rulefile)
    ruleset.import_ruleset()
    rules = ruleset.get_ruleset()

    #Get input file of text (if we make it that far)
    parser = file_parser.file_parser(textfile)
    parser.set_ruleset(rules)

    parser.set_file(parser.open_file(parser.filepath, "r"))
    parser.set_file_to_sentences()

    applier = rule_applier.rule_applier(rules, parser)
    applier.apply()
    #TODO Abstract this out
    #TODO Write edited rules to file, check that editor actually writes changes

if __name__ == '__main__':
    #Testing
    args = ("strunk", "gatsby.txt", "demonstrate/demonstrate")
    strunk(*args)
    #if len(sys.argv) == 2:
    #    sys.argv.append(None)
    #    strunk(*sys.argv)
    #elif len(sys.argv) == 3:
    #    strunk(*sys.argv)
    #else:
    #    raise ValueError("Invalid argument syntax. Check usage for info.")
