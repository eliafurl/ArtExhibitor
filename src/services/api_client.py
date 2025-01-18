import requests

class APIClient:
    def __init__(self, base_url: str = "https://api.opensea.io/api/v1", api_key: str = None):
        self.base_url = base_url
        self.api_key = api_key

    def get_assets(self, wallet: str) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        url = f"{self.base_url}/assets?owner={wallet}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
