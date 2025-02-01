import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { fetchNFTs } from "../services/api";
import NFTCard from "./NFTCard";

function Slideshow({ wallets, interval }) {
  const [nfts, setNfts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadNFTs = async () => {
      setLoading(true);
      setError(null);
      try {
        const results = await Promise.all(wallets.map(fetchNFTs));
        const allNFTs = results.flat(); // Merge arrays into one list
        setNfts(allNFTs);
      } catch (err) {
        setError("Failed to load NFTs. Please try again.");
      }
      setLoading(false);
    };

    if (wallets.length > 0) {
      loadNFTs();
    } else {
      setNfts([]);
    }
  }, [wallets]);

  const sliderSettings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: interval,
  };

  return (
    <div>
      <h2>NFT Slideshow</h2>
      {loading && <p>Loading NFTs...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {!loading && nfts.length === 0 && <p>No NFTs found. Add a wallet to get started.</p>}
      {nfts.length > 0 && (
        <Slider {...sliderSettings}>
          {nfts.map((nft, index) => (
            <NFTCard key={index} nft={nft} />
          ))}
        </Slider>
      )}
    </div>
  );
}

export default Slideshow;
