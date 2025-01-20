import React, { useState } from "react";
import Slideshow from "./components/Slideshow";
import ControlPanel from "./components/ControlPanel";

function App() {
  const [wallets, setWallets] = useState([]);
  const [settings, setSettings] = useState({ interval: 3000 });

  const addWallet = (wallet) => {
    setWallets((prev) => [...prev, wallet]);
  };

  const removeWallet = (wallet) => {
    setWallets((prev) => prev.filter((w) => w !== wallet));
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
