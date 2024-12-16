---
title: Consent UI Live Example
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
        "Authorization":
          "sha512-XBK+44B5anpMFsb9wZGbCxLuA0MLTw4wOg/fRfgnCFKzVho1vwwlbEUVWmIqiCa3R5AOKdPqONPrNslmn+YYkg==?Mw==",
        "User-Agent": "ReadMe-API-Explorer",
        "Accept": "application/json",
        "Basiq-Version": "3.0",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: "",
    })
      .then((response) => {
        console.log("Response Status:", response.status);
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
          setError("No access token received.");
        }
      })
      .catch((error) => {
        console.error("Error fetching token:", error);
        setError(`Error fetching token: ${error.message}`);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <div>Loading token...</div>;
  }

  return (
    <div>
      <h1>Token Fetch Result</h1>
      {error && <div style={{ color: "red" }}>{error}</div>}
      {token ? (
        <div>
          <h2>Access Token:</h2>
          <pre>{token}</pre> {/* Display the token */}
        </div>
      ) : (
        <div>No token available.</div>
      )}
    </div>
  );
};

<br />

<TokenFetcher />