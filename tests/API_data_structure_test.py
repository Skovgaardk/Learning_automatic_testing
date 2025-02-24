import unittest
from unittest.mock import patch, Mock
import json
from Main import get_movies_by_popularity
from dotenv import load_dotenv


class TestMovieAPIDataStructure(unittest.TestCase):
    @patch("Main.requests.get")
    def test_api_response_structure(self, mock_get):
        load_dotenv()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            "results": [
                {"original_title": "Inception"},
                {"original_title": "Interstellar"},
            ]
        })

        mock_get.return_value = mock_response
        response = get_movies_by_popularity()
        data = json.loads(response.text)

        self.assertIn("results", data)
        self.assertTrue(all("original_title" in movie for movie in data["results"]))

if __name__ == "__main__":
    unittest.main()
