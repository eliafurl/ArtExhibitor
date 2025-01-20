import React from "react";

function NFTCard({ nft }) {
  return (
    <div>
      <img src={nft.image_url} alt={nft.name} style={{ maxWidth: "100%" }} />
      <h3>{nft.name}</h3>
      <p>{nft.artist}</p>
    </div>
  );
}

export default NFTCard;
