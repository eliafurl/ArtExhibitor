from flask import Flask, request, jsonify
from flask_cors import CORS
from src.application.art_exhibitor import ArtExhibitor
from src.utils.setup_env import OPENSEA_API_KEY

app = Flask(__name__)

# Allow requests from http://localhost:3000 (frontend)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Initialize ArtExhibitor
_art_exhibitor = ArtExhibitor(api_key=OPENSEA_API_KEY)

@app.route('/api/nfts', methods=['GET'])
def get_nfts():
    wallet = request.args.get('wallet')
    if not wallet:
        return jsonify({"error": "Wallet address is required"}), 400 # Bad request

    try:
        # Use ArtExhibitor to fetch NFTs for the wallet
        nfts = _art_exhibitor.get_nfts(wallet)
        nft_data = [nft.to_dict() for nft in nfts]

        return jsonify(nft_data), 200 # OK
    except Exception as e:
        return jsonify({"error": str(e)}), 500 # Internal server error

@app.route('/api/wallets', methods=['GET'])
def get_wallets():
    wallets = _art_exhibitor.get_wallets()
    return jsonify(wallets), 200 # OK

@app.route('/api/wallets/<wallet>', methods=['DELETE'])
def delete_wallet(wallet):
    _art_exhibitor.remove_wallet(wallet)
    return '', 204 # No content

@app.route("/")
def home():
    return "ArtExhibitor is running!", 200 # OK

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)