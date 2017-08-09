#Takes text and ruleset, outputs results to file
import rule_parser
import file_parser

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

    parser.open_file()
    parser.preprocess_file()

    parser.apply_ruleset()
    parser.write_new_file()

    #TODO Write edited rules to file, check that editor actually writes changes

if __name__ == '__main__':
    args = ("strunk", "gatsby.txt", None)
    strunk(*args)
