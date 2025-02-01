import React from "react";

function NFTCard({ nft }) {
  return (
    <div style={{ textAlign: "center" }}>
      <img
        src={nft.image_url || "https://arweave.net/c354rSc2YXAYmeRgmAM3dEoRoOPY9Fdwy_tWHLtCEWI"}
        alt={nft.name || "NFT Image"}
        style={{ maxWidth: "100%", maxHeight: "300px" }}
      />
      <h3>{nft.name || "Untitled NFT"}</h3>
      <p>{nft.artist || "Unknown Artist"}</p>
    </div>
  );
}

export default NFTCard;