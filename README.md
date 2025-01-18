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
