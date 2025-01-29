from typing import List
from src.models.nft_metadata import NFTMetadata
from src.services.api_client import APIClient

class NFTFetcher:
    def __init__(self, api_key: str):
        self.api_client = APIClient(api_key=api_key)

    def fetch_nfts(self, wallet: str) -> List[NFTMetadata]:
        raw_data = self.api_client.get_assets(wallet)
        return [NFTMetadata.from_api_response(nft) for nft in raw_data.get("nfts", [])]
