from typing import List
from src.models.nft_metadata import NFTMetadata

class NFTFetcher:
    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_nfts(self, wallet: str) -> List[NFTMetadata]:
        raw_data = self.api_client.get_assets(wallet)
        return [NFTMetadata.from_api_response(nft) for nft in raw_data.get("nfts", [])]
