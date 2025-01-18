import unittest
import requests
from unittest.mock import patch
from src.services.api_client import APIClient
from src.utils.setup_env import OPENSEA_API_KEY
from src.utils.setup_env import TEST_WALLET_1

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient(base_url="https://api.opensea.io/api/v2", api_key=OPENSEA_API_KEY)

    @patch("requests.get")
    def test_get_assets_successful(self, mock_get):
        # Mock successful response
        mock_response = {"assets": []}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the method
        wallet = "0xTestWallet"
        response = self.api_client.get_assets(wallet)

        # Assertions
        self.assertEqual(response, mock_response)
        mock_headers = {
                    "accept": "application/json",
                    "x-api-key": OPENSEA_API_KEY
                }
        mock_get.assert_called_once_with(
            f"https://api.opensea.io/api/v2/chain/ethereum/account/{wallet}/nfts", headers=mock_headers
        )

    @patch("requests.get")
    def test_get_assets_rate_limit(self, mock_get):
        # Mock rate limiting (429)
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=429),
            unittest.mock.Mock(status_code=200, json=lambda: {"assets": []}),
        ]

        # Call the method
        wallet = "0xTestWallet"
        response = self.api_client.get_assets(wallet)

        # Assertions
        self.assertEqual(response, {"assets": []})
        self.assertEqual(mock_get.call_count, 2)

    @patch("requests.get")
    def test_get_assets_failure(self, mock_get):
        # Mock failure (403)
        mock_get.return_value.status_code = 403
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        with self.assertRaises(requests.exceptions.HTTPError):
            self.api_client.get_assets("0xInvalidWallet")

    def test_real_data(self):
        response = self.api_client.get_assets(TEST_WALLET_1)
        self.assertNotEqual(len(response.get("nfts")), 0)

if __name__ == "__main__":
    unittest.main()
