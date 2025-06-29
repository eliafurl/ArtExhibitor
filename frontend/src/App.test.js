import React from "react";
import { render, fireEvent, screen } from "@testing-library/react";
import App from "./App";

// Mock window.alert
global.alert = jest.fn();

describe("App Component", () => {
  test("adds and removes wallets via ControlPanel", () => {
    render(<App />);

    // Add a wallet
    const walletInput = screen.getByPlaceholderText("Enter wallet address");
    const addButton = screen.getByText("Add Wallet");

    fireEvent.change(walletInput, { target: { value: "0x123" } });
    fireEvent.click(addButton);

    // Check if wallet is added
    expect(screen.getByText("0x123")).toBeInTheDocument();

    // Remove the wallet
    const removeButton = screen.getByText("Remove");
    fireEvent.click(removeButton);

    // Check if wallet is removed
    expect(screen.queryByText("0x123")).not.toBeInTheDocument();
  });

  test("updates slideshow interval via ControlPanel", () => {
    render(<App />);

    // Change interval
    const intervalInput = screen.getByLabelText("Interval (ms):");
    fireEvent.change(intervalInput, { target: { value: "5000" } });

    // Slideshow should now use the updated interval (mock slider functionality if needed)
    expect(intervalInput.value).toBe("5000");
  });
});