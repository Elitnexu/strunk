#Takes text and ruleset, outputs results to file
import rule_parser
import file_parser

#Read in config file
#Prepare text file
#For each line of file, check for instance of keyword
#If found, process based on behaviour
#Upon completion, write each suggestion to file

def strunk(args):
    #Read config file from either config folder or args
    #if args is file, process, if args is ruleform, use.
    #else reject

    #Get dictionary of ruleset (if we make it that far)
    contents = rule_parser.rule_parser(args)
    rules = contents.get_ruleset()
    print rules

    #Get input file of text (if we make it that far)



if __name__ == '__main__':
    strunk(None)
