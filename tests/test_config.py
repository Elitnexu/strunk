import unittest
from config import *

class ConfigTest(unittest.TestCase):
    def test_read_config(self):
        #Argument given is an explicit rule
        self.assertEqual(
        read_config("(they're),(replace with my),(I'm selfish)"), "Explicit regex"
        )

        #Argument given is a custom ruleset
        self.assertEqual(
        read_config("custom"), "rules/custom.strunk"
        )

        #Argument given is None, meaning go with default ruleset
        self.assertEqual(
        read_config(None), DEFAULT_RULE_FILE
        )

        #Argument doesn't match format
        self.assertRaises(
        ValueError, lambda: read_config("(I'm invalid)(syntax))")
        )

if __name__ == '__main__':
    unittest.main()
