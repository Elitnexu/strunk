#File Parser handles the text file side of strunk, opening and
#processing text files based on the ruleset given to it.

import re
import subprocess
import os

class file_parser:

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

    def open_file(self):
        #Take the filepath specified
        #Attempt to open
        #If works, we ready for main show
        try:
            file = open(self.filepath, "r")
        except:
            raise IOError("Textfile failed to open")

        self.file = file


    def apply_ruleset(self):
        #For the given ruleset, apply the rules.
        #Compile ruleset
        for rule in self.ruleset:
            #Making code more readable
            rule = self.ruleset[rule]
            #print "Expression: " + rule.get_expression()
            #print "Senteces length: " + str(len(self.sentences))
            for index, line in enumerate(self.sentences):
                if re.search(rule.get_expression(), line) is not None:
                    print "\n"
                    print "Match found for " + rule.get_expression() + " : " + line
                    #Print context, give options
                    self.handle_rule_match(rule, line, index)


    def handle_rule_match(self, rule, line, index):
        #Takes a rule, prints match, etc. and gives options.
        print "Expression: " + rule.get_expression()
        print "Action: " + rule.get_action()
        print "Subject:" + rule.get_subject()
        print "--OPTIONS--"
        #Due to action only being WARNING for now, this is static.
        print "[E]dit line, [S]kip, More [I]nformation"
        while True:
            try:
                #print "--OPTIONS--"
                #Due to action only being WARNING for now, this is static.
                #print "[E]dit line, [S]kip, More [I]nformation"
                response = raw_input("Reply: ")
                if response.lower() == 'e':
                    print "Editing file..."
                    #Edit file with index
                    oldLine = line
                    self.edit_sentence(line, index)
                    print "Edited! oldLine = " + oldLine
                    print "New line = " + self.sentences[index]
                    break
                elif response.lower() == 's':
                    print "Skipping..."
                    #Skip to next line
                    break
                elif response.lower() == 'i':
                    #Display more info
                    info = rule.get_info()
                    for contents in info:
                        print contents
                else:
                    #Invalid input
                    print "Please enter a valid option."
                    continue
            except ValueError:
                print "Please enter a valid option."
                continue

        print "Completed rule application!"

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
                line[0] = sentence + "\n" + line[0]
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
            else: #full line, add to previous sentence
                #sentence += line
                sentence = sentence + "\n" + line
            i = i + 1
        #DEBUG
        #for line in self.sentences:
        #    print " Line: " + line
        return self.sentences

    def edit_sentence(self, line, index):
        #write temp file with sentence as only contents
        #open with default editor
        #take file changes and save as new sentence index
        line = line.strip()
        try:
            file = open(self.SENTENCE_PATH, "w+")
        except:
            raise IOError("Sentence file failed to open")

        file.write(line)
        file.close()

        #Attempt to find default editor, set to vi if none found
        try:
            editor = os.environ['EDITOR']
        except KeyError:
            print "Default editor not found. Setting to 'vi'..."
            editor = 'vi'

        #Attempt to open editor and wait until its closed to continue
        try:
            subprocess.Popen([editor, self.SENTENCE_PATH]).wait()
            #When done, open and write new sentence to file
        except:
            raise IOError("No editor found.")

        #Attempt to open sentence file to read edited line
        try:
            file = open(self.SENTENCE_PATH, "r+")
        except:
            raise IOError("Sentence file failed to open.")

        #Read contents, delete contents when done
        line = file.read()
        self.sentences[index] = line
        file.truncate(0)
        file.close()

    #Takes the sentence array and writes it to new file
    def write_new_file(self):
        try:
            file = open("strunked_" + self.filepath, "w+")
        except:
            raise IOError("Strunked file failed to open")

        print "Writing Strunked file to " + "strunked_" + self.filepath + "..."
        #TODO Change behaviour based on config file
        #Change to process all at once? Might fix the sentence fragmentation
        for line in self.sentences:
            file.write(line)

        file.close()
        print "Done!"

    #Set ruleset dictionary
    def set_ruleset(self, ruleset):
        self.ruleset = ruleset

    def set_file_path(self, filepath):
        self.filepath = filepath
