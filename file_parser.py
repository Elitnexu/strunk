#Parse a file with a ruleset
#TODO

class file_parser:

    def __init__(self, filepath):
        #Instance variables
        self.filepath = filepath
        self.ACTIONS = {
        "delete", "replace %s", "flag"
        }
        self.ruleset = None

    def preprocess_file(self):
        #Take the filepath specified
        #Attempt to open
        #If works, we ready for main show
        try:
            file = open(self.filepath, "r")
        except:
            raise IOError("Textfile failed to open")

        return "HEAVEN OR HELL LET'S ROCK"

    #Set ruleset dictionary
    def set_ruleset(self, ruleset):
        self.ruleset = ruleset

    def set_file_path(self, filepath):
        self.filepath = filepath
