import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import Slideshow from "./Slideshow";
import { fetchNFTs } from "../services/api";

// Mock API service
jest.mock("../services/api", () => ({
  fetchNFTs: jest.fn(),
}));

describe("Slideshow Component", () => {
    test("renders NFTs in a slideshow", async () => {
      const mockNFTs = [
        { name: "Artwork 1", artist: "Artist 1", image_url: "https://arweave.net/KQJhmrTn_N6aWZy90NF476BC2n4qVoOu85df6yiL2lI" },
        { name: "Artwork 2", artist: "Artist 2", image_url: "https://arweave.net/c354rSc2YXAYmeRgmAM3dEoRoOPY9Fdwy_tWHLtCEWI" },
      ];
  
      fetchNFTs.mockResolvedValueOnce(mockNFTs);

    // Render the component
    render(<Slideshow />);

    // Wait for NFTs to be fetched and rendered
    await waitFor(() => {
      const artwork1Elements = screen.getAllByText("Artwork 1");
      const artwork2Elements = screen.getAllByText("Artwork 2");

      // Check that duplicates are rendered (due to react-slick)
      expect(artwork1Elements.length).toBeGreaterThanOrEqual(2);
      expect(artwork2Elements.length).toBeGreaterThanOrEqual(2);
    });
  });
});
  
