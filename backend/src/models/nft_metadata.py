class NFTMetadata:
    def __init__(self, name: str, description: str, image_url: str, contract_address: str, token_id: str):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.contract_address = contract_address
        self.token_id = token_id

    @staticmethod
    def from_api_response(data: dict):
        return NFTMetadata(
            name=data.get("name", "Unknown"),
            description=data.get("description", ""),
            image_url=data.get("image_url", ""),
            contract_address=data.get("asset_contract", {}).get("address", ""),
            token_id=data.get("token_id", "")
        )
    
    def to_dict(self):
        """Convert NFTMetadata object to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "image_url": self.image_url,
            "contract_address": self.contract_address,
            "token_id": self.token_id,
        }
