import React, { useState } from "react";

function ControlPanel({ onAddWallet, onRemoveWallet, onUpdateSettings, wallets }) {
  const [walletInput, setWalletInput] = useState("");
  const [interval, setInterval] = useState(3000);

  const handleAddWallet = () => {
    if (walletInput.trim()) {
      onAddWallet(walletInput.trim());
      setWalletInput("");
    }
  };

  const handleRemoveWallet = (wallet) => {
    onRemoveWallet(wallet);
  };

  const handleIntervalChange = (e) => {
    const newInterval = parseInt(e.target.value, 10);
    if (!isNaN(newInterval)) {
      setInterval(newInterval);
      onUpdateSettings({ interval: newInterval });
    }
  };

  return (
    <div>
      <h2>Control Panel</h2>
      {/* Add Wallet */}
      <div>
        <input
          type="text"
          value={walletInput}
          onChange={(e) => setWalletInput(e.target.value)}
          placeholder="Enter wallet address"
        />
        <button onClick={handleAddWallet}>Add Wallet</button>
      </div>
      {/* Wallet List */}
      <ul>
        {wallets.map((wallet, index) => (
          <li key={index}>
            {wallet}
            <button onClick={() => handleRemoveWallet(wallet)}>Remove</button>
          </li>
        ))}
      </ul>
      {/* Slideshow Settings */}
      <div>
        <label>
          Interval (ms):
          <input
            type="number"
            value={interval}
            onChange={handleIntervalChange}
          />
        </label>
      </div>
    </div>
  );
}

export default ControlPanel;
