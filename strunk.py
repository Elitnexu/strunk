#Takes text and ruleset, outputs results to file
import rule_parser
import file_parser
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
    rules = []
    new_rules = ruleset.get_ruleset()
    for w in new_rules:
        rules.append(w)

    for w in rules:
        print w.get_action()
        #print get_action()
        #print get_subject()
        #print get_info()

    #Get input file of text (if we make it that far)
    parser = file_parser.file_parser(textfile)
    parser.set_ruleset(rules)
    parser.open_file()
    print parser.preprocess_file()

    #TODO Process text file with ruleset (pass two args)
    #new file_parser
    pass


if __name__ == '__main__':
    args = ("strunk", "gatsby.txt", None)
    strunk(*args)
