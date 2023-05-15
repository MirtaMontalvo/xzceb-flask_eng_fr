import unittest
from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(english_to_french(''), '')  # test when empty string is given as input the output is an empty string

class Test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(french_to_english(''), '')  # test when empty string is given as input the output is an empty string

unittest.main()
