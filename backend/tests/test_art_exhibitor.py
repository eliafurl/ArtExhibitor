import unittest
from unittest.mock import MagicMock
from src.application.art_exhibitor import ArtExhibitor
from src.services.nft_fetcher import NFTFetcher
from src.models.nft_metadata import NFTMetadata

class TestArtExhibitor(unittest.TestCase):
    def setUp(self):
        mock_fetcher = MagicMock(spec=NFTFetcher)
        mock_fetcher.fetch_nfts.return_value = [
            NFTMetadata("Test NFT", "A test NFT", "http://example.com/nft.png", "0x12345", "123")
        ]
        self.exhibitor = ArtExhibitor("000")
        self.exhibitor.fetcher = mock_fetcher

    def test_add_wallet(self):
        self.exhibitor.add_wallet("0xTestWallet")
        self.assertIn("0xTestWallet", self.exhibitor.wallets)

    def test_remove_wallet(self):
        self.exhibitor.add_wallet("0xTestWallet")
        self.exhibitor.remove_wallet("0xTestWallet")
        self.assertNotIn("0xTestWallet", self.exhibitor.wallets)

    def test_refresh_nfts(self):
        self.exhibitor.add_wallet("0xTestWallet")
        self.exhibitor.refresh_nfts()
        self.assertEqual(len(self.exhibitor.get_nfts("0xTestWallet")), 1)

    def test_get_nfts_empty(self):
        nfts = self.exhibitor.get_nfts("0xNonExistentWallet")
        self.assertEqual(nfts, [])

    def test_get_nfts_with_data(self):
        self.exhibitor.add_wallet("0xTestWallet")
        self.exhibitor.refresh_nfts()
        nfts = self.exhibitor.get_nfts("0xTestWallet")
        self.assertEqual(len(nfts), 1)
        self.assertEqual(nfts[0].name, "Test NFT")
        self.assertEqual(nfts[0].description, "A test NFT")
        self.assertEqual(nfts[0].image_url, "http://example.com/nft.png")
        self.assertEqual(nfts[0].contract_address, "0x12345")
        self.assertEqual(nfts[0].token_id, "123")

if __name__ == "__main__":
    unittest.main()