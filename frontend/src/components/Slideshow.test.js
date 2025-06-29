import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import Slideshow from "./Slideshow";
import { fetchNFTsAPI } from "../services/api";
import userEvent from "@testing-library/user-event";

// Mock fetchNFTsAPI function
jest.mock("../services/api", () => ({
  fetchNFTsAPI: jest.fn(),
}));

describe("Slideshow Component", () => {
  test("renders loading state when fetching NFTs", async () => {
    fetchNFTsAPI.mockResolvedValueOnce([]); // Mock empty response
    render(<Slideshow wallets={["0x123"]} interval={3000} />);

    expect(screen.getByText("Loading NFTs...")).toBeInTheDocument();
    await waitFor(() => expect(screen.queryByText("Loading NFTs...")).not.toBeInTheDocument());
  });

  test("displays NFTs when fetched successfully", async () => {
    fetchNFTsAPI.mockResolvedValueOnce([
      { name: "Artwork 1", artist: "Artist 1", image_url: "https://arweave.net/KQJhmrTn_N6aWZy90NF476BC2n4qVoOu85df6yiL2lI" },
    ]);

    render(<Slideshow wallets={["0x123"]} interval={3000} />);

    await waitFor(() => expect(screen.getAllByText("Artwork 1").length).toBeGreaterThanOrEqual(2));
    expect(screen.getAllByText("Artist 1").length).toBeGreaterThanOrEqual(2);
    expect(screen.getAllByAltText("Artwork 1").length).toBeGreaterThanOrEqual(2);
  });

  test("shows error message when API fails", async () => {
    fetchNFTsAPI.mockRejectedValueOnce(new Error("Network error"));

    render(<Slideshow wallets={["0x123"]} interval={3000} />);

    await waitFor(() => expect(screen.getByText("Failed to load NFTs. Please try again.")).toBeInTheDocument());
  });

  test("displays 'No NFTs found' when wallet has no NFTs", async () => {
    fetchNFTsAPI.mockResolvedValueOnce([]);

    render(<Slideshow wallets={["0x123"]} interval={3000} />);

    await waitFor(() => expect(screen.getByText("No NFTs found. Add a wallet to get started.")).toBeInTheDocument());
  });
});