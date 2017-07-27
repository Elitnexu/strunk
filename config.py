#Ruleset (to be replaced with some other file format)
import os.path
import re

#Instance variables
DEFAULT_RULE_FILE = "rules.csv"
ACTIONS = {
    "delete", "replace with %s", "flag"
}

#Checks if rules file exists.
#Returns true, false
def rules_exists(filename):
    return os.path.isfile(filename)

def read_config(args):
    if args is None:
        #Check for config file
        print "Default rule file specified."
        if(rules_exists(DEFAULT_RULE_FILE)):
            print "Default rule file found."
            return DEFAULT_RULE_FILE
        else:
            #Raise error? Create default?
            raise IOError("Default rule file " + DEFAULT_RULE_FILE + " not found")

    #Check if args matches ruleform (regxp)
    elif re.match(r"\(.*\),\(.*\),\(.*\)", args) is not None:
        print "RegEx matches "
        #Maybe change to specify whether regex, filename?
        return args
    else:
        raise ValueError("No valid rules found.")
