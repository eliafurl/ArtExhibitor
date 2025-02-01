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

    expect(screen.getByText("Artwork 1")).toBeInTheDocument();
    expect(screen.getByText("Artist 1")).toBeInTheDocument();

    // Check that the image has the correct src
    const imageElement = screen.getByRole("img");
    expect(imageElement).toHaveAttribute("src", "http://example.com/nft1.png");
    expect(imageElement).toHaveAttribute("alt", "Artwork 1");
  });

  test("displays fallback image when image_url is missing", () => {
    const mockNFT = {
      name: null,
      artist: "Artist 2",
      image_url: null,
    };

    render(<NFTCard nft={mockNFT} />);

    // Check that the image source is the fallback image
    const imageElement = screen.getByRole("img");
    expect(imageElement).toHaveAttribute("src", "https://arweave.net/c354rSc2YXAYmeRgmAM3dEoRoOPY9Fdwy_tWHLtCEWI");
    expect(imageElement).toHaveAttribute("alt", "NFT Image");
  });
});