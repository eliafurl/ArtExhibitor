import unittest
from unittest.mock import patch
from src.services.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient(base_url="https://api.opensea.io/api/v1")

    @patch("requests.get")
    def test_get_assets(self, mock_get):
        # Mock the requests.get call
        mock_response = {"assets": []}
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200

        # Call the method
        wallet = "0xTestWallet"
        response = self.api_client.get_assets(wallet)

        # Assertions
        self.assertEqual(response, mock_response)
        mock_get.assert_called_once_with(
            f"https://api.opensea.io/api/v1/assets?owner={wallet}", headers={}
        )

if __name__ == "__main__":
    unittest.main()