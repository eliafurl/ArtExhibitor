import React, { useState } from "react";
import Slideshow from "./components/Slideshow";
import ControlPanel from "./components/ControlPanel";
import { removeWalletAPI } from "./services/api";

function App() {
  const [wallets, setWallets] = useState([]);
  const [settings, setSettings] = useState({ interval: 3000 });

  const addWallet = (wallet) => {
    setWallets((prev) => [...prev, wallet]);
  };

  const removeWallet = async (wallet) => {
    const updatedWallets = wallets.filter((w) => w !== wallet);
    setWallets(updatedWallets); // Optimistically update UI
  
    try {
      const response = await removeWalletAPI(wallet);
      if (response.status !== 204) {
        throw new Error("Backend failed to remove wallet");
      }
    } catch (error) {
      console.error("Error removing wallet:", error);
      alert("Error removing wallet. Restoring it.");
      setWallets((prev) => [...prev, wallet]); // Restore wallet if API fails
    }
  };

  const updateSettings = (newSettings) => {
    setSettings((prev) => ({ ...prev, ...newSettings }));
  };

  return (
    <div>
      <header>
        <h1>Art Exhibitor</h1>
      </header>
      <ControlPanel
        onAddWallet={addWallet}
        onRemoveWallet={removeWallet}
        onUpdateSettings={updateSettings}
        wallets={wallets}
      />
      <Slideshow wallets={wallets} interval={settings.interval} />
    </div>
  );
}

export default App;
