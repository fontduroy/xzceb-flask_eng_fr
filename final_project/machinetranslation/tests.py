import unittest
import translator

class TestTranslations(unittest.TestCase):

    def test_frenchToEnglish_nullInput(self):
        self.assertEqual(translator.french_to_english(""), None)

    def test_englishToFrench_nullInput(self):
        self.assertEqual(translator.english_to_french(""), None)

    def test_frenchToEnglish_bonjour(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")

    def test_englishToFrench_hello(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()

