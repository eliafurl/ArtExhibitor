import time
import requests

class APIClient:
    def __init__(self, base_url: str = "https://api.opensea.io/api/v2", api_key: str =""):
        self.base_url = base_url
        self.api_key = api_key

    def get_assets(self, wallet: str) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        headers = {
                    "accept": "application/json",
                    "x-api-key": self.api_key
                }
        url = f"{self.base_url}/chain/ethereum/account/{wallet}/nfts"

        for attempt in range(3):  # Retry mechanism
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:  # Rate limit error
                print("Rate limit reached. Retrying...")
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                response.raise_for_status()

        raise requests.exceptions.RequestException("Failed to fetch assets after retries.")