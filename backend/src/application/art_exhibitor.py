from typing import List, Dict
from src.services.nft_fetcher import NFTFetcher
from src.models.nft_metadata import NFTMetadata

class ArtExhibitor:
    def __init__(self, api_key: str):
        self.wallets: List[str] = []
        self.nft_data: Dict[str, List[NFTMetadata]] = {}
        self.fetcher = NFTFetcher(api_key)

    def add_wallet(self, address: str):
        if address not in self.wallets:
            self.wallets.append(address)

    def remove_wallet(self, address: str) -> bool:
        if address in self.wallets:
            self.wallets.remove(address)
            self.nft_data.pop(address, None)
            return True
        return False

    def get_wallets(self) -> List[str]:
        return self.wallets

    def refresh_nfts(self):
        for wallet in self.wallets:
            self.nft_data[wallet] = self.fetcher.fetch_nfts(wallet)

    def get_nfts(self, address: str) -> List[NFTMetadata]:
        if self.nft_data.get(address) is None:
            if address not in self.wallets:
                self.add_wallet(address)
            self.refresh_nfts()
        return self.nft_data.get(address)
