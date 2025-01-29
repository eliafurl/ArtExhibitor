from src.application.art_exhibitor import ArtExhibitor
from src.utils.setup_env import OPENSEA_API_KEY
from src.utils.setup_env import TEST_WALLET_1

# Real wallet address from .env file
TEST_WALLET = TEST_WALLET_1
print(f"Testing on wallet: {TEST_WALLET}")

# Initialize Art Exhibitor
art_exhibitor = ArtExhibitor(OPENSEA_API_KEY)

# Add the wallet and fetch NFTs
art_exhibitor.add_wallet(TEST_WALLET)
art_exhibitor.refresh_nfts()

# Display fetched NFTs
nfts = art_exhibitor.get_nfts(TEST_WALLET)
for nft in nfts:
    print(f"Name: {nft.name}")
    print(f"Description: {nft.description}")
    print(f"Image URL: {nft.image_url}")
    print(f"Contract Address: {nft.contract_address}")
    print(f"Token ID: {nft.token_id}")
    print("---")
