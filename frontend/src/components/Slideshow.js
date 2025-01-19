import React, { useState, useEffect } from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { fetchNFTs } from "../services/api";
import NFTCard from "./NFTCard";

function Slideshow() {
  const [nfts, setNfts] = useState([]);
  const [interval, setInterval] = useState(3000); // Default interval in ms

  useEffect(() => {
    // Fetch NFT data from backend
    fetchNFTs()
      .then((data) => setNfts(data))
      .catch((error) => console.error("Error fetching NFTs:", error));
  }, []);

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
      <Slider {...sliderSettings}>
        {nfts.map((nft, index) => (
          <NFTCard key={index} nft={nft} />
        ))}
      </Slider>
    </div>
  );
}

export default Slideshow;
