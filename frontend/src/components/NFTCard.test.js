import React from "react";
import { render, screen } from "@testing-library/react";
import NFTCard from "./NFTCard";

describe("NFTCard Component", () => {
  test("renders NFT details correctly", () => {
    const mockNFT = {
      name: "Artwork 1",
      artist: "Artist 1",
      image_url: "http://example.com/nft1.png",
    };

    render(<NFTCard nft={mockNFT} />);

    // Check if the image is rendered
    const imageElement = screen.getByAltText("Artwork 1");
    expect(imageElement).toBeInTheDocument();
    expect(imageElement).toHaveAttribute("src", "http://example.com/nft1.png");

    // Check if the name and artist are rendered
    expect(screen.getByText("Artwork 1")).toBeInTheDocument();
    expect(screen.getByText("Artist 1")).toBeInTheDocument();
  });
});
