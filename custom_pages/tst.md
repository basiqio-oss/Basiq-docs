---
title: tst
fullscreen: false
hidden: true
---
import React, { useEffect, useState } from "react";

export const TokenFetcher = () => {
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("https://au-api.basiq.io/token", {
      method: "POST",
      headers: {
        "Authorization": "Basic NjMxMjNmMWMtZjYxMy00ZjMyLWFiYzUtYzBhZDdhYTY2YmU1OjQ3NWYwMzhkLTBlZmItNGM1ZS1iMzQ0LTAzMzYxOTkyYTRlMw==",
        "Accept": "application/json",
        "Basiq-Version": "3.0",
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: "scope=SERVER_ACCESS"
    })
      .then((response) => {
        console.log('Response Status:', response.status);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log("Token response:", data);
        if (data && data.access_token) {
          setToken(data.access_token);
        } else {
          throw new Error("No access token received.");
        }
      })
      .catch((error) => {
        console.error("Error fetching token:", error);
        setError(`Error fetching token: ${error.message}`);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Token Fetch Result</h1>
      {error && <div className="text-red-500 mb-4">{error}</div>}
      {loading ? (
        <div>Loading token...</div>
      ) : token ? (
        <div>
          <h2 className="text-xl font-semibold mb-2">Access Token:</h2>
          <pre className="bg-gray-100 p-4 rounded-lg overflow-x-auto">
            {token}
          </pre>
        </div>
      ) : (
        <div>No token available.</div>
      )}
    </div>
  );
};

export default TokenFetcher;

<TokenFetcher />