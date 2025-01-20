import React from "react";
import { render, fireEvent, screen } from "@testing-library/react";
import ControlPanel from "./ControlPanel";

describe("ControlPanel Component", () => {
  test("allows adding and removing wallets", () => {
    const mockAddWallet = jest.fn();
    const mockRemoveWallet = jest.fn();

    render(
      <ControlPanel
        onAddWallet={mockAddWallet}
        onRemoveWallet={mockRemoveWallet}
        onUpdateSettings={jest.fn()}
        wallets={[]}
      />
    );

    // Add Wallet
    fireEvent.change(screen.getByPlaceholderText("Enter wallet address"), {
      target: { value: "0x123" },
    });
    fireEvent.click(screen.getByText("Add Wallet"));
    expect(mockAddWallet).toHaveBeenCalledWith("0x123");

    // Remove Wallet
    render(
      <ControlPanel
        onAddWallet={mockAddWallet}
        onRemoveWallet={mockRemoveWallet}
        onUpdateSettings={jest.fn()}
        wallets={["0x123"]}
      />
    );
    fireEvent.click(screen.getByText("Remove"));
    expect(mockRemoveWallet).toHaveBeenCalledWith("0x123");
  });

  test("allows updating the interval", () => {
    const mockUpdateSettings = jest.fn();

    render(
      <ControlPanel
        onAddWallet={jest.fn()}
        onRemoveWallet={jest.fn()}
        onUpdateSettings={mockUpdateSettings}
        wallets={[]}
      />
    );

    fireEvent.change(screen.getByLabelText("Interval (ms):"), {
      target: { value: "5000" },
    });
    expect(mockUpdateSettings).toHaveBeenCalledWith({ interval: 5000 });
  });
});
