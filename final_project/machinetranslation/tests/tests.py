import unittest
from translator import englishToFrench, frenchToEnglish

class Test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(englishToFrench(''), '')  # test when empty string is given as input the output is an empty string

class Test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(frenchToEnglish(''), '')  # test when empty string is given as input the output is an empty string

unittest.main()
