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
        return jsonify({"error": "Wallet address is required"}), 400

    try:
        # Use ArtExhibitor to fetch NFTs for the wallet
        nfts = _art_exhibitor.get_nfts(wallet)
        return jsonify(nfts)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/")
def home():
    return "ArtExhibitor is running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)