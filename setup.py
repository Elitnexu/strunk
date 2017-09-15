from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Strunk',
    version='1.0',
    description='Command-line tool for validating and re-writing text files with regular expressions',
    author='Marc Hanley',
    author_email='marcjameshanley@gmail.com',
    licence='MIT',
    keywords='validate text regular expressions',
    long_description=read('README.md'),
    packages=['strunk', 'rulesets', 'strunk/file_parser', 'strunk/rule_parser', 'strunk/rule_applier', 'tests'])
