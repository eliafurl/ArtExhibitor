import axios from "axios";

const BASE_URL = "http://localhost:5000";

export const fetchNFTs = async () => {
  const response = await axios.get(`${BASE_URL}/api/nfts`);
  return response.data;
};
