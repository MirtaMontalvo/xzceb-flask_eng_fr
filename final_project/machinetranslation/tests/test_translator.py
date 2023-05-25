"""
Unit tests for translator module.
"""

import unittest
from .translator import english_to_french, french_to_english
class TestTranslatorModule(unittest.TestCase):
    """
    Test case class for testing functions, english_to_french and french_to_english.
    """
    def test_english_to_french(self):
        """
        Test cases for the english_to_french function.
        """
        # Test when one-word input is 'Hello' the translated text is 'Bonjour'.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

        # Test when input is 'Where is the theater?' the expected text is 'Où est le théâtre?'.
        self.assertEqual(english_to_french('Where is the theater?'), 'Où est le théâtre?')

        # Test input for null which returns None
        self.assertNotEqual(self, english_to_french(None))

    def test_french_to_english(self):
        """
        Test cases for the french_to_english function.
        """
        # Test when input is 'Bonjour' the translated text is 'Hello'.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

        # Test when input is 'Où est le théâtre?' the expected text is 'Where is the theater?'
        self.assertEqual(french_to_english('Où est le théâtre?'), 'Where is the theater?')

        # Test input for null which returns None
        self.assertNotEqual(self, french_to_english(None))

if __name__ == '__main__':
    unittest.main()
