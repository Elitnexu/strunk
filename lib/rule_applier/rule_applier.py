from __future__ import print_function
#Applies ruleset to text file. Abstracted behaviour out of
#File_Parser.py
from builtins import input
import os
import re
import subprocess

class rule_applier(object):

    def __init__(self, ruleset, parser):

        self.ruleset = ruleset
        self.parser = parser
        self.sentences = parser.get_sentences()

    def apply(self):
        self.apply_ruleset(self.ruleset)
        filepath = self.parser.get_file_path()
        self.write_new_file(filepath)

    def apply_ruleset(self, ruleset):
        #For the given ruleset, apply the rules.
        #Compile ruleset
        action = "default"

        try:
            for rule in ruleset:
                #Making code more readable
                rule = ruleset[rule]

                for index, line in enumerate(self.sentences):
                    if re.search(rule.get_expression(), line) is not None:
                        print("\n")
                        print("Match found for " + rule.get_expression() + " : " + line)
                        #Print context, give options
                        action = self.handle_rule_match(self.sentences, rule, line, index)
                        if action == "skip": #Skip current rule
                            action = "default"
                            break
                        if action == "skip_all": #Skip all rules
                            raise StopIteration("Skipping all rules...")

        #This exception is deliberately invoked when skipping all rules,
        #to prematurely end processing
        except StopIteration:
            pass

        print("Done!")
        return self.sentences

    def handle_rule_match(self, sentences, rule, line, index):

        SENTENCE_PATH = "temp.strunk"
        #Takes a rule, prints match, etc. and gives options.
        print("Expression: " + rule.get_expression())
        print("Action: " + rule.get_action())
        print("Subject:" + rule.get_subject())
        print("--OPTIONS--")
        #Due to action only being WARNING for now, this is static.
        print("[E]dit, [I]gnore, [S]kip, Skip [A]ll, [M]ore, [H]elp")
        while True:
            try:
                response = (input("Reply: "))
                if response.lower() == 'e':
                    print("Editing file...")
                    #Edit file with index
                    self.edit_sentence(SENTENCE_PATH, line, index)
                    print("Edit complete!")
                    break
                elif response.lower() == 'i':
                    print("Ignored match. Finding next...")
                    #Skip to next line
                    break
                elif response.lower() == "s":
                    #Skip current rule
                    return "skip"
                    break
                elif response.lower() == "a":
                    #Skip entire prompt
                    return "skip_all"
                    break
                elif response.lower() == 'm':
                    #Display more info
                    info = rule.get_info()
                    for contents in info:
                        print(contents)
                elif response.lower() == 'h':
                    #Display help module
                    self.display_help()
                else:
                    #Invalid input
                    print("Please enter a valid option.")
                    continue
            except ValueError:
                print("Please enter a valid option.")
                continue

        print("Completed rule application!")
        return "default"

    def display_help(self):
        print("\n")
        print("==HELP==")
        print("[E]dit: Edit the sentence(s) displayed in a text editor")
        print("[I]gnore: Ignore applying the current rule to the sentence displayed")
        print("[S]kip: Skip the current rule and start applying next rule")
        print("Skip [A]ll: Skip all future rules and start writing to file")
        print("[M]ore Information: Display more information on the current rule")
        print("[H]elp: Display the Help prompt")

    def edit_sentence(self, filepath, line, index):
        #write temp file with sentence as only contents
        #open with default editor
        #take file changes and save as new sentence index
        line = line.strip()
        file = self.open_file(filepath, "w+")
        file.write(line)
        file.close()

        #Attempt to find default editor, set to vi if none found
        try:
            editor = os.environ['EDITOR']
        except KeyError:
            print("Default editor not found. Setting to 'vi'...")
            editor = 'vi'

        #Attempt to open editor and wait until its closed to continue
        try:
            subprocess.Popen([editor, filepath]).wait()
            #When done, open and write new sentence to file
        except:
            raise IOError("No valid editor found.")

        #Attempt to open sentence file to read edited line
        file = self.open_file(filepath, "r+")

        #Read contents, delete contents when done
        lines = file.read()
        self.parser.set_sentence(index, lines)
        #sentences[index] = line
        file.truncate(0)
        file.close()
        os.remove(filepath)

    #Takes the sentence array and writes it to new file
    def write_new_file(self, filepath):

        file = self.open_file("strunked_" + filepath, "w+")
        print("Writing Strunked file to " + "strunked_" + filepath + "...")
        #TODO Change behaviour based on config file
        #Change to process all at once? Might fix the sentence fragmentation
        sentences = self.parser.get_sentences()
        for line in sentences:
            file.write(line)
        file.close()

        print("Done!")

    def open_file(self, filepath, mode):
        #Take the filepath specified
        #Attempt to open
        try:
            return open(filepath, mode)
        except:
            raise IOError("Text file at " + filepath
                        + " in mode " + mode
                        + " failed to open.")
