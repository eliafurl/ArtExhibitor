import axios from "axios";

const BASE_URL = "http://localhost:5001";

export const fetchNFTs = async (wallet) => {
  try {
    const response = await axios.get(`${BASE_URL}/api/nfts`, {
      params: { wallet },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching NFTs:", error);
    throw error;
  }
};