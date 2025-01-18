# Art Exhibitor

Welcome to the Art Exhibitor project! This application retrieves and displays NFTs from wallet addresses using the OpenSea API. It includes modularized backend architecture, environment variable management, and unit tests.

---

## **Table of Contents**
- [Art Exhibitor](#art-exhibitor)
  - [**Table of Contents**](#table-of-contents)
  - [**Features**](#features)
  - [**Prerequisites**](#prerequisites)
  - [**Installation**](#installation)
  - [**Configuration**](#configuration)
  - [**Usage**](#usage)
  - [**Testing**](#testing)
  - [**Contributing**](#contributing)
  - [Class Descriptions](#class-descriptions)
    - [`ArtExhibitor`](#artexhibitor)
    - [`NFTFetcher`](#nftfetcher)
    - [`NFTMetadata`](#nftmetadata)
    - [`APIClient`](#apiclient)

---

## **Features**
- Fetch NFT metadata from wallet addresses using the OpenSea API.

---

## **Prerequisites**
1. **Python**: Version 3.10 or later.
2. **Pip**: Ensure you have `pip` installed.
3. **Virtual Environment (Recommended)**: Use Python’s `venv` module for managing dependencies.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone git@github.com:eliafurl/ArtExhibitor.git
   cd ArtExhibitor
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv art_exhibitor
   source art_exhibitor/bin/activate  # For Linux/Mac
   art_exhibitor\Scripts\activate   # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Configuration**
1. Create a `.env` file in the project root:
   ```bash
   touch .env
   ```

2. Add your OpenSea API key to the `.env` file: ([How to get an OpenSea API key](https://docs.opensea.io/reference/api-keys))
   ```plaintext
   OPENSEA_API_KEY=your_api_key_here
   ```

3. Add your test wallets to the `.env` file:
   ```plaintext
   TEST_WALLET_1=your_wallet_1_address_here
   TEST_WALLET_2=your_wallet_2_address_here
   ```

---

## **Usage**
*TODO*

---

## **Testing**
1. Run all tests:
   ```bash
   ./run_tests.sh
   ```

2. View coverage report:
   ```bash
   pytest --cov=src --cov-report=term-missing
   ```

---

## **Contributing**
1. Fork the repository and create your feature branch:
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes and commit:
   ```bash
   git commit -m "Add some feature"
   ```

3. Push to your branch:
   ```bash
   git push origin feature-name
   ```

4. Open a pull request on GitHub.

---

Feel free to reach out for any questions or suggestions!


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
