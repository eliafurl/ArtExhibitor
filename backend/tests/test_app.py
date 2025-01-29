import unittest
from unittest.mock import MagicMock, patch
from src.application.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client."""
        self.client = app.test_client()
        self.client.testing = True

    @patch("src.application.app._art_exhibitor")
    def test_get_nfts_success(self, mock_art_exhibitor):
        """Test the /api/nfts endpoint with a valid wallet."""
        # Mock ArtExhibitor's get_nfts method
        mock_art_exhibitor.get_nfts.return_value = [
            {
                "name": "Artwork 1",
                "artist": "Artist 1",
                "image_url": "http://example.com/nft1.png",
                "contract_address": "0xabc",
                "token_id": "1",
            }
        ]

        # Perform the test request
        wallet = "0x123"
        response = self.client.get(f"/api/nfts?wallet={wallet}")
        print(
            f"response: {response.status_code}, {response.json}"
        )

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            [
                {
                    "name": "Artwork 1",
                    "artist": "Artist 1",
                    "image_url": "http://example.com/nft1.png",
                    "contract_address": "0xabc",
                    "token_id": "1",
                }
            ],
        )
        mock_art_exhibitor.get_nfts.assert_called_once_with(wallet)

    def test_get_nfts_missing_wallet(self):
        """Test the /api/nfts endpoint without a wallet parameter."""
        response = self.client.get("/api/nfts")

        # Assertions
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Wallet address is required"})

    @patch("src.application.app._art_exhibitor")
    def test_get_nfts_error(self, mock_art_exhibitor):
        """Test the /api/nfts endpoint when an exception occurs."""
        # Mock ArtExhibitor's get_nfts method to raise an exception
        mock_art_exhibitor.get_nfts.side_effect = Exception("Mocked exception")

        # Perform the test request
        wallet = "0x123"
        response = self.client.get(f"/api/nfts?wallet={wallet}")

        # Assertions
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Mocked exception"})
        mock_art_exhibitor.get_nfts.assert_called_once_with(wallet)


if __name__ == "__main__":
    unittest.main()