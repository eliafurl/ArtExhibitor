import axios from "axios";
import { fetchNFTs } from "./api";

// Mock axios
jest.mock("axios");

describe("API Service", () => {
  test("fetchNFTs makes a GET request and returns data", async () => {
    const mockData = [
      { name: "Artwork 1", artist: "Artist 1", image_url: "http://example.com/nft1.png" },
      { name: "Artwork 2", artist: "Artist 2", image_url: "http://example.com/nft2.png" },
    ];

    axios.get.mockResolvedValueOnce({ data: mockData });

    const data = await fetchNFTs();
    expect(axios.get).toHaveBeenCalledWith("http://localhost:5000/api/nfts");
    expect(data).toEqual(mockData);
  });

  test("fetchNFTs handles errors", async () => {
    axios.get.mockRejectedValueOnce(new Error("Network Error"));

    await expect(fetchNFTs()).rejects.toThrow("Network Error");
    expect(axios.get).toHaveBeenCalledWith("http://localhost:5000/api/nfts");
  });
});
