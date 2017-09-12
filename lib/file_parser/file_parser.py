from builtins import object
import re
import subprocess
import os

#File Parser handles text file importing
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
        try:
            print(filepath)
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

    #Takes all contents of current file and appends to sentences list
    #Returns the newly appended sentences list
    def set_file_to_sentences(self):

        for line in self.get_file():
            self.sentences.append(line)

    #Set ruleset dictionary
    def set_ruleset(self, ruleset):
        self.ruleset = ruleset

    def set_file_path(self, filepath):
        self.filepath = filepath

    def get_file_path(self):
        return self.filepath
