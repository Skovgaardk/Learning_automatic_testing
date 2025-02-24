import unittest
from unittest.mock import patch, Mock
import json
from main_module import get_movies_by_popularity
from dotenv import load_dotenv

class TestAPI(unittest.TestCase):

        @patch("main_module.requests.get")
        def test_API_response_status_code(self, mock_get):
            load_dotenv()
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = json.dumps({"results": []})  # Simulate empty movie list

            mock_get.return_value = mock_response

            response = get_movies_by_popularity()
            self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()