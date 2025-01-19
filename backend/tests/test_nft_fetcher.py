import unittest
from unittest.mock import MagicMock
from src.services.nft_fetcher import NFTFetcher
from src.models.nft_metadata import NFTMetadata
from src.services.api_client import APIClient

class TestNFTFetcher(unittest.TestCase):
    def setUp(self):
        self.mock_api_client = MagicMock(spec=APIClient)
        self.fetcher = NFTFetcher(self.mock_api_client)

    def test_fetch_nfts(self):
        # Mock response
        mock_response = {
            "nfts": [
                {
                    "name": "Test NFT",
                    "description": "A test NFT",
                    "image_url": "http://example.com/nft.png",
                    "asset_contract": {"address": "0x12345"},
                    "token_id": "123"
                }
            ]
        }

        self.mock_api_client.get_assets.return_value = mock_response

        # Call the method
        wallet = "0xTestWallet"
        nfts = self.fetcher.fetch_nfts(wallet)

        # Assertions
        self.assertEqual(len(nfts), 1)
        self.assertIsInstance(nfts[0], NFTMetadata)
        self.assertEqual(nfts[0].name, "Test NFT")
        self.assertEqual(nfts[0].contract_address, "0x12345")

        self.mock_api_client.get_assets.assert_called_once_with(wallet)

if __name__ == "__main__":
    unittest.main()