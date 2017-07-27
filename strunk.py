#Takes text and ruleset, outputs results to file
import config

#Read in config file
#Prepare text file
#For each line of file, check for instance of keyword
#If found, process based on behaviour
#Upon completion, write each suggestion to file

#Put into functions?
#Takes file with keyword, action, comment
#Outputs Dictionary of keywords and behaviour
def process_file(filename):
    #Read file
    pass



def strunk(args):
    #Read config file from either config folder or args
    #if args is file, process, if args is ruleform, use.
    #else reject
    filename = config.read_config(args)
    process_file(filename)


if __name__ == '__main__':
    #Test when argument is rule
    #tyler_parser("(they're),(replace with my),(I'm selfish)")

    #Test when no arg i.e. default rulefile
    #tyler_parser(None)

    #Test when custom rulefile piped in
    #tyler_parser("custom.csv")
