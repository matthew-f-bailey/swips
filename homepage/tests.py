from django.test import TestCase

from homepage.views import get_words
from homepage.models import Word
# Create your tests here.

class TestGame(TestCase):

    # Load in fixtures
    fixtures = ['word_fixtures']

    def test_get_words(self):
        """Test that we get back 2 Word instance"""
        word1, word2 = get_words()
        self.assertIsInstance(word1, Word)
        self.assertIsInstance(word2, Word)