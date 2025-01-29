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

if __name__ == '__main__':
    app.run(debug=True)