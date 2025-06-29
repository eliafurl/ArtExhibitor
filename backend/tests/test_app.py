import unittest
from unittest.mock import MagicMock, patch
from src.application.app import app
from src.models.nft_metadata import NFTMetadata

class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client."""
        self.client = app.test_client()
        self.client.testing = True

    @patch("src.application.app._art_exhibitor")
    def test_get_nfts_success(self, mock_art_exhibitor):
        """Test the /api/nfts endpoint with a valid wallet."""
        # Create mock NFTMetadata objects
        mock_nft = NFTMetadata(
            name="Artwork 1",
            description="Test NFT",
            image_url="http://example.com/nft1.png",
            contract_address="0xabc",
            token_id="1"
        )
        # Mock ArtExhibitor's get_nfts method
        mock_art_exhibitor.get_nfts.return_value = [mock_nft]

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
                    "description": "Test NFT",
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
    def test_get_wallets(self, mock_art_exhibitor):
        """Test the /api/wallets endpoint."""
        # Mock ArtExhibitor's get_wallets method
        mock_art_exhibitor.get_wallets.return_value = ["0x123", "0x456"]

        # Perform the test request
        response = self.client.get("/api/wallets")

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ["0x123", "0x456"])
        mock_art_exhibitor.get_wallets.assert_called_once()

    @patch("src.application.app._art_exhibitor")
    def test_delete_wallet_found(self, mock_art_exhibitor):
        """Test the /api/wallets/<wallet> DELETE endpoint."""
        # Mock remove_wallet to ensure it returns None
        mock_art_exhibitor.remove_wallet.return_value = True

        # Perform the test request
        wallet = "0x123"
        response = self.client.delete(f"/api/wallets/{wallet}")

        # Assertions
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b"")
        mock_art_exhibitor.remove_wallet.assert_called_once_with(wallet)

    @patch("src.application.app._art_exhibitor")
    def test_delete_wallet_not_found(self, mock_art_exhibitor):
        """Test the /api/wallets/<wallet> DELETE endpoint."""
        # Mock remove_wallet to ensure it returns None
        mock_art_exhibitor.remove_wallet.return_value = False

        # Perform the test request
        wallet = "0xnotfound"
        response = self.client.delete(f"/api/wallets/{wallet}")

        # Assertions
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Wallet not found"})
        mock_art_exhibitor.remove_wallet.assert_called_once_with(wallet)

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

    def test_home(self):
        """Test the /api/ endpoint."""
        response = self.client.get("/api/")

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "ArtExhibitor is running!")

if __name__ == "__main__":
    unittest.main()