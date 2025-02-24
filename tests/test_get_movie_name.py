import unittest
from main_module.movie_name_getter import get_movie_names


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