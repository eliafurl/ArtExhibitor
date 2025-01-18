import unittest
from src.models.nft_metadata import NFTMetadata

class TestNFTMetadata(unittest.TestCase):
    def test_from_api_response(self):
        # Mock API response
        api_response = {
            "name": "Test NFT",
            "description": "A test NFT",
            "image_url": "http://example.com/nft.png",
            "asset_contract": {"address": "0x12345"},
            "token_id": "123"
        }

        # Create metadata
        metadata = NFTMetadata.from_api_response(api_response)

        # Assertions
        self.assertEqual(metadata.name, "Test NFT")
        self.assertEqual(metadata.description, "A test NFT")
        self.assertEqual(metadata.image_url, "http://example.com/nft.png")
        self.assertEqual(metadata.contract_address, "0x12345")
        self.assertEqual(metadata.token_id, "123")

if __name__ == "__main__":
    unittest.main()