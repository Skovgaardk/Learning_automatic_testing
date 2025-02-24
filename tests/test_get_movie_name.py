import unittest
from unittest.mock import patch, Mock
import json
from main_module import get_movies_by_popularity, get_movie_names
from dotenv import load_dotenv

class TestMovieNamesFunction(unittest.TestCase):
    def test_movie_name_function(self):
        movies = [
            {"original_title": "Inception"},
            {"original_title": "Interstellar"},
            {"original_title": "The Dark Knight"}
        ]

        expected_list = ["Inception", "Interstellar", "The Dark Knight"]

        self.assertEqual(get_movie_names(movies), expected_list)

if __name__ == "__main__":
    unittest.main()