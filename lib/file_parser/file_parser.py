#File Parser handles the text file side of strunk, opening and
#processing text files based on the ruleset given to it.

from builtins import object
import re
import subprocess
import os

class file_parser(object):

    def __init__(self, filepath):
        #Instance variables
        self.file = None
        self.filepath = filepath
        self.SENTENCE_PATH = "temp.strunk"
        self.ruleset = None
        self.DELIMITERS = {
        ".!?"
        }
        self.sentences = []

    def open_file(self, filepath, mode):
        #Take the filepath specified
        #Attempt to open
        #If works, we ready for main show
        try:
            return open(filepath, mode)
        except:
            raise IOError("Text file at " + filepath
                        + " in mode " + mode
                        + " failed to open.")

    def get_file(self):
        return self.file

    def get_sentences(self):
        return self.sentences

    def set_file(self, file):
        self.file = file

    def set_sentence(self, index, line):
        self.sentences[index] = line

    def preprocess_file(self):
        #read in file contents
        index = 0
        sentence = ""
        delim_exp = r'.+[!?.].*'

        #For each line, apply processing to line and
        #add to sentence list
        for line in self.file:
            sentence = self.process_line(index, line, sentence, delim_exp)
            index = index + 1

        return self.sentences

    def process_line(self, index, line, sentence, delim_exp):
        #Remove leading/trailing whitespace and newlines
        line = line.strip()
        if line == '':
            self.sentences.append(line)
            return sentence
        if re.match(delim_exp, line) is not None:
            #line = re.split('[!?.]', line)
            line = re.findall(delim_exp, line, re.DOTALL)

            if index != 0:
                #Append second half of sentence to previous sentence
                line[0] = sentence + "\n" + line[0]
            self.sentences.append(line[0])
            #...why is this if branch in here again?
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
        else: #full line, add to previous sentence
            #sentence += line
            sentence = sentence + "\n" + line
            self.sentences.append(sentence)
            sentence = ""
            return sentence
        return sentence

    #Set ruleset dictionary
    def set_ruleset(self, ruleset):
        self.ruleset = ruleset

    def set_file_path(self, filepath):
        self.filepath = filepath

    def get_file_path(self):
        return self.filepath
