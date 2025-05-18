"use client";
import { useState } from "react";

export default function Home() {
  const [wins, setWins] = useState({
    readQuran: false,
    workout: false,
    deepWork: false,
  });

  const handleChange = (key: string) => {
    setWins((prev) => ({
      ...prev,
      [key]: !prev[key as keyof typeof prev],
    }));
  };

  const handleSubmit = async () => {
    const count = Object.values(wins).filter(Boolean).length;

    if (count === 0) {
      alert("No wins checked!");
      return;
    }

    await fetch("http://localhost:8000/daily/log", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ quantity: count }),
    });

    alert(`Logged ${count} wins to Pixela!`);
  };

return (
  <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
    <h1 className="text-2xl font-bold mb-4">Daily Wins</h1>

    <div className="space-y-2">
      {/* checkboxes here */}
    </div>

    <button
      onClick={handleSubmit}
      className="mt-6 px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700 transition"
    >
      Submit Wins
    </button>

    {/* ✅ Add Pixela Graph below */}
    <h2 className="text-xl font-semibold mt-10 mb-2">Streak Progress</h2>
    <iframe
      src="https://pixe.la/v1/users/tolbra/graphs/daily-wins"
      className="w-full max-w-md h-80 border rounded"
      style={{ backgroundColor: "white" }}
    ></iframe>
  </div>
);
;
}
