## Class Descriptions

### `ArtExhibitor`

- **Purpose**: Core class managing wallet addresses and retrieved NFT metadata.
- **Attributes**:
  - `wallets`: List of wallet addresses being tracked.
  - `nft_data`: Dictionary mapping wallet addresses to a list of `NFTMetadata`.
  - `fetcher`: Instance of `NFTFetcher` to retrieve NFT data.
- **Methods**:
  - `add_wallet`: Add a wallet address to track.
  - `remove_wallet`: Remove a wallet from tracking.
  - `refresh_nfts`: Fetch NFT data for all wallets.
  - `get_nfts`: Retrieve NFTs for a specific wallet.

### `NFTFetcher`

- **Purpose**: Handles the logic to fetch NFTs from a blockchain API.
- **Attributes**:
  - `api_client`: Instance of `APIClient` for making API requests.
- **Methods**:
  - `fetch_nfts`: Fetch all NFTs for a given wallet address.

### `NFTMetadata`

- **Purpose**: Represents metadata for a single NFT.
- **Attributes**:
  - `name`: Name of the NFT.
  - `description`: Description of the NFT.
  - `artist`: Name of the NFT artist.
  - `artwork_url`: URL to the image/video associated with the NFT.
  - `contract_address`: Smart contract address of the NFT.
  - `token_id`: Token ID of the NFT.
- **Methods**:
  - `from_api_response`: Static method to construct an `NFTMetadata` object from API response data.

### `APIClient`

- **Purpose**: Low-level class for handling API calls to fetch raw NFT data.
- **Attributes**:
  - `base_url`: Base URL for the API (e.g., OpenSea or Moralis).
  - `api_key`: API key for authentication (if required).
- **Methods**:
  - `get_assets`: Retrieve NFT data for a wallet.
  - `get_metadata`: Retrieve specific metadata for a contract and token ID.


## NFT Retrieval Endpoint API - `/api/nfts`

### Overview
The `/api/nfts` endpoint allows users to fetch NFT metadata associated with a given wallet address. The endpoint interacts with the OpenSea API via `ArtExhibitor` and `APIClient` to retrieve NFT details such as the name, artist, image URL, contract address, and token ID.

---

### Endpoint Details

#### **URL**
```
GET /api/nfts
```

#### **Query Parameters**
| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `wallet`  | string | ✅ Yes  | The Ethereum wallet address for which NFT metadata should be retrieved. |

#### **Request Example**
```
GET /api/nfts?wallet=0xabc123...
```

---

### **Response Details**

#### **Success Response**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`
- **Response Body:**
```json
[
  {
    "name": "Artwork 1",
    "artist": "Artist 1",
    "image_url": "http://example.com/nft1.png",
    "contract_address": "0xabc123...",
    "token_id": "1001"
  },
  {
    "name": "Artwork 2",
    "artist": "Artist 2",
    "image_url": "http://example.com/nft2.png",
    "contract_address": "0xdef456...",
    "token_id": "1002"
  }
]
```

#### **Error Responses**

##### **1. Missing Wallet Address**
- **Status Code:** `400 Bad Request`
- **Response Body:**
```json
{
  "error": "Wallet address is required"
}
```

##### **2. Internal Server Error**
- **Status Code:** `500 Internal Server Error`
- **Response Body:**
```json
{
  "error": "An unexpected error occurred"
}
```

---

### **Backend Implementation**
The endpoint is implemented using Flask, leveraging `ArtExhibitor` to retrieve NFT metadata.

```python
from flask import Flask, request, jsonify
from src.application.art_exhibitor import ArtExhibitor
from src.utils.setup_env import OPENSEA_API_KEY

app = Flask(__name__)

# Initialize ArtExhibitor
_art_exhibitor = ArtExhibitor(api_key=OPENSEA_API_KEY)

@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    wallet = request.args.get('wallet')
    if not wallet:
        return jsonify({"error": "Wallet address is required"}), 400

    try:
        # Use ArtExhibitor to fetch NFTs for the wallet
        nfts = _art_exhibitor.get_nfts(wallet)
        return jsonify(nfts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

---

### **Usage in Frontend**

The frontend calls this API to retrieve NFTs for a given wallet and display them in a slideshow.

#### **Frontend API Call (Example)**
```javascript
import axios from "axios";

const BASE_URL = "http://localhost:5000";

export const fetchNFTsAPI = async (wallet) => {
  const response = await axios.get(`${BASE_URL}/api/nfts`, {
    params: { wallet },
  });
  return response.data;
};
```

---

### **Conclusion**
The `/api/nfts` endpoint:
- Retrieves NFT metadata from OpenSea.
- Returns structured JSON responses for frontend integration.  
