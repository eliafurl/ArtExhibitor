import axios from "axios";

const BASE_URL = "http://localhost:5001";

export const fetchNFTsAPI = async (wallet) => {
  try {
    const response = await axios.get(`${BASE_URL}/api/nfts`, {
      params: { wallet },
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error("Error fetching NFTs:", error.response.data);
    } else if (error.request) {
      console.error("Error fetching NFTs: No response received");
    } else {
      console.error("Error fetching NFTs:", error.message);
    }
    throw error;
  }
};

export const removeWalletAPI = async (wallet) => {
  try {
    return await axios.delete(`${BASE_URL}/api/wallets/${wallet}`);
  } catch (error) {
    console.error("Error removing wallet:", error);
    throw error;
  }
};