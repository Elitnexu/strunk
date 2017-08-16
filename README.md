# Strunk

Strunk is a command-line tool for parsing text documents written in Python.

It takes in a user-defined regular expression ruleset in the form of a
.strunk file and checks a given text document for matches with the rules
provided. For each match found, the user is given the choice to edit the
matching sentence in the text and save any changes made.

Strunk is named after [William Strunk](https://en.wikipedia.org/wiki/William_Strunk_Jr.),
author of [The Elements of Style](https://en.wikipedia.org/wiki/The_Elements_of_Style).

## Getting Started

TODO

### Prerequisites

TODO

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

# Usage
## Running
In the root directory of Strunk, enter `python strunk.py example.txt example.strunk`
at the command line in order to run the ruleset file `example.strunk` on the text document `example.txt`.

## Syntax
Strunk uses the custom file format `.strunk` to designate as the collection of
regular expressions to apply to a document. `.strunk` files have the following syntax:

\#COMMENT  
REGULAR EXPRESSION  
ACTION    
SUBJECT  
MORE INFORMATION LINE#1  
MORE INFORMATION LINE#2  
MORE INFORMATION LINE#3  


REGULAR EXPRESSION  
ACTION  
...  
...  
...  
END  


A template file is included in the root directory under `template.strunk` as a
guide.

Comments are denoted with `#` as the first character of a given line. Every comment
line must _start_ with `#` to be considered a comment, i.e "ACTION \#some action" is
invalid.

The Regular Expression line contains the regular expression Strunk will evaluate.

The Action line contains the specified action for Strunk to perform. As of the
latest commit, this feature is unimplemented and defaults to the 'WARNING' action.

The Subject line should contain a single, concise sentence that specifies why a match
is made for the given expression. For instance, an appropriate subject line for the
expression `\butilise*\b` is "Unnecessary: replace with 'use'". The goal of the subject
line is to inform the user at a glance, and so should not exceed 72 characters if
possible.

The Information lines are displayed when a match is made by Strunk and a user asks
for more information, at which point these lines are displayed. These lines are
optional and can fill as many rows as desired.

Between each rule, include two spaces in order to delineate the end of the previous
rules' "More Information" lines.

The final line of a Strunk file should be "END". Any lines after this are ignored.

## Testing

Explain how to run the automated tests for this system
