## NFT Retrieval API - `/api/nfts` Endpoint Documentation

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
GET /api/nfts?wallet=0x23C37B17F87c5033C160f113E7EB65D9a9B857DE
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

export const fetchNFTs = async (wallet) => {
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
