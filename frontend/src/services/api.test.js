import axios from "axios";
import { fetchNFTsAPI, removeWalletAPI } from "./api";

// Mock axios
jest.mock("axios");

// Mock window.alert
global.alert = jest.fn();

describe("API Service", () => {
  test("fetchNFTsAPI makes a GET request and returns data", async () => {
    const mockData = [
      { name: "Artwork 1", artist: "Artist 1", image_url: "http://example.com/nft1.png" },
    ];

    axios.get.mockResolvedValueOnce({ data: mockData });

    const data = await fetchNFTsAPI("0x123");
    expect(axios.get).toHaveBeenCalledWith("http://localhost:5001/api/nfts", {
      params: { wallet: "0x123" },
    });
    expect(data).toEqual(mockData);
  });

  test("fetchNFTsAPI handles errors", async () => {
    axios.get.mockRejectedValueOnce(new Error("Network Error"));

    await expect(fetchNFTsAPI("0x123")).rejects.toThrow("Network Error");
  });

  test("removeWalletAPI makes a DELETE request", async () => {
    axios.delete.mockResolvedValueOnce({status: 204});

    await removeWalletAPI("0x123");
    expect(axios.delete).toHaveBeenCalledWith("http://localhost:5001/api/wallets/0x123");
  });
});