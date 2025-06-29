import logging
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from src.application.art_exhibitor import ArtExhibitor
from src.utils.setup_env import OPENSEA_API_KEY

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Allow requests from http://localhost:3000 (frontend)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Initialize ArtExhibitor
_art_exhibitor = ArtExhibitor(api_key=OPENSEA_API_KEY)

@app.route('/api/nfts', methods=['GET'])
def get_nfts() -> Response:
    """
    Endpoint to retrieve NFTs for a specific wallet.
    Query Parameters:
        wallet (str): The wallet address to fetch NFTs for.
    Returns:
        Response: A JSON response containing the list of NFTs and a 200 OK status code,
                  or an error message with a 400 or 500 status code.
    """
    # Get the wallet address from query parameters
    wallet = request.args.get('wallet')
    if not wallet:
        return jsonify({"error": "Wallet address is required"}), 400 # Bad request

    try:
        # Use ArtExhibitor to fetch NFTs for the wallet
        nfts = _art_exhibitor.get_nfts(wallet)
        nft_data = [nft.to_dict() for nft in nfts]

        return jsonify(nft_data), 200 # OK
    except Exception as e:
        logging.exception(f"Exception in /api/nfts:")
        return jsonify({"error": str(e)}), 500 # Internal server error

@app.route('/api/wallets', methods=['GET'])
def get_wallets() -> Response:
    """
    Endpoint to retrieve a list of wallets.

    Returns:
        Response: A JSON response containing the list of wallets and a 200 OK status code.
    """
    wallets = _art_exhibitor.get_wallets()
    return jsonify(wallets), 200 # OK

@app.route('/api/wallets/<wallet>', methods=['DELETE'])
def delete_wallet(wallet) -> Response:
    """
    Delete a wallet from the ArtExhibitor system.

    Args:
        wallet (str): The wallet address to be removed.

    Returns:
        Empty response with HTTP 204 status code if successful,
        or 404 if the wallet was not found.
    """
    try:
        removed = _art_exhibitor.remove_wallet(wallet)
        if not removed:
            return jsonify({"error": "Wallet not found"}), 404
        return '', 204  # No content
    except Exception as e:
        logging.exception(f"Exception in /api/wallets/<wallet>:")
        return jsonify({"error": str(e)}), 500

@app.route('/api/')
def home() -> Response:
    """ Home endpoint to check if the ArtExhibitor is running.
    Returns:
        Response: A simple message indicating the service is running with a 200 OK status code.
    """
    # This endpoint can be used to check if the service is running
    return "ArtExhibitor is running!", 200 # OK

if __name__ == '__main__':
    # Run the Flask application

    # This will allow the application to be accessed from any IP address on port 5001.
    # Make sure to set the OPENSEA_API_KEY environment variable before running the application.
    # You can set it in your terminal or in a .env file if you're using a library like python-dotenv.
    # Example: export OPENSEA_API_KEY='your_opensea_api_key_here' 
    app.run(host="0.0.0.0", port=5001, debug=True)
    # Note: The debug=True option is set for development purposes.
    # In production, it should be set to False or removed.