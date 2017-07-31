#File Parser handles the text file side of strunk, opening and
#processing text files based on the ruleset given to it.

import re

class file_parser:

    def __init__(self, filepath):
        #Instance variables
        self.file = None
        self.filepath = filepath
        self.ACTIONS = {
        "add", "delete", "replace %s", "flag"
        }
        self.ruleset = None
        self.DELIMITERS = {
        ".!?"
        }
        self.sentences = []

    def open_file(self):
        #Take the filepath specified
        #Attempt to open
        #If works, we ready for main show
        try:
            file = open(self.filepath, "r")
        except:
            raise IOError("Textfile failed to open")

        self.file = file

    def preprocess_file(self):
        #read in file contents
        i = 0
        sentence = ""

        for line in self.file:
            #Remove leading/trailing whitespace and newlines
            line = line.strip()
            if line == '':
                continue
            if re.match(r'.+[!?.].*', line) is not None:
                line = re.split('[!?.]', line)

                #Append second half of sentence to previous sentence
                line[0] = sentence + " " + line[0]
                self.sentences.append(line[0])
                if len(line) > 1:
                    #Process all sentences and append to list
                    for w in line:
                        if w == line[0]: #already did this
                            continue
                        elif w == line[len(line) - 1]:
                            #New uncomplete sentence for final list item
                            sentence = w
                        else:
                            self.sentences.append(w)
            else:
                sentence += line
            i = i + 1

        return self.sentences

    #Set ruleset dictionary
    def set_ruleset(self, ruleset):
        self.ruleset = ruleset

    def set_file_path(self, filepath):
        self.filepath = filepath
