#Takes text and ruleset, outputs results to file
import lib.rule_parser.rule_parser as rule_parser
import lib.rule_parser.rule as rule
import lib.file_parser.file_parser as file_parser
#import file_parser
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

    parser.file = parser.open_file(parser.filepath, "r")
    parser.preprocess_file()

    parser.apply_ruleset()
    parser.write_new_file()

    #TODO Write edited rules to file, check that editor actually writes changes

if __name__ == '__main__':
    #Testing
    args = ("strunk", "gatsby.txt", None)
    strunk(*args)
    #if len(sys.argv) == 2:
    #    sys.argv.append(None)
    #    strunk(*sys.argv)
    #elif len(sys.argv) == 3:
    #    strunk(*sys.argv)
    #else:
    #    raise ValueError("Invalid argument syntax. Check usage for info.")
