import unittest
from random import randint
from src.application.art_exhibitor import ArtExhibitor
from src.utils.setup_env import OPENSEA_API_KEY
from src.utils.setup_env import TEST_WALLET_1

class TestArtExhibitor(unittest.TestCase):
    def setUp(self):
        self.art_exhibitor = ArtExhibitor(OPENSEA_API_KEY)
   
    # TEST_WALLET_1 should be a real wallet address with NFTs
    def test_get_nfts_with_real_data_add_wallet(self):
        print(f"Testing on wallet: {TEST_WALLET_1}")
        self.art_exhibitor.add_wallet(TEST_WALLET_1)
        self.art_exhibitor.refresh_nfts()
        nfts = self.art_exhibitor.get_nfts(TEST_WALLET_1)
        
        self.assertGreater(len(nfts), 0)
        
        nft_index = randint(0, len(nfts) - 1)
        print(f"Name: {nfts[nft_index].name}")
        print(f"Description: {nfts[nft_index].description}")
        print(f"Image URL: {nfts[nft_index].image_url}")
        print(f"Contract Address: {nfts[nft_index].contract_address}")
        print(f"Token ID: {nfts[nft_index].token_id}")
        
        self.assertNotEqual(nfts[nft_index].name, "")
        self.assertNotEqual(nfts[nft_index].description, "")
        self.assertNotEqual(nfts[nft_index].image_url, "")
        # Not all NFTs have contract address and token ID in the metadata
        # self.assertNotEqual(nfts[nft_index].contract_address, "")
        # self.assertNotEqual(nfts[nft_index].token_id, "")
        
    # TEST_WALLET_1 should be a real wallet address with NFTs
    def test_get_nfts_with_real_data(self):
        print(f"Testing on wallet: {TEST_WALLET_1}")
        nfts = self.art_exhibitor.get_nfts(TEST_WALLET_1)
        
        self.assertGreater(len(nfts), 0)
        
        nft_index = randint(0, len(nfts) - 1)
        print(f"Name: {nfts[nft_index].name}")
        print(f"Description: {nfts[nft_index].description}")
        print(f"Image URL: {nfts[nft_index].image_url}")
        print(f"Contract Address: {nfts[nft_index].contract_address}")
        print(f"Token ID: {nfts[nft_index].token_id}")
        
        self.assertNotEqual(nfts[nft_index].name, "")
        self.assertNotEqual(nfts[nft_index].description, "")
        self.assertNotEqual(nfts[nft_index].image_url, "")
        # Not all NFTs have contract address and token ID in the metadata
        # self.assertNotEqual(nfts[nft_index].contract_address, "")
        # self.assertNotEqual(nfts[nft_index].token_id, "")
            