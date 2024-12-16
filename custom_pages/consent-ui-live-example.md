---
title: Consent UI Live Example
fullscreen: false
hidden: false
---
import React, { useEffect, useState } from "react";

export const TokenFetcher = () => {
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null); // To handle any errors

useEffect(() => {
  fetch("https://au-api.basiq.io/token", {
    method: "POST",
    headers: {
      "Authorization":
        "Basic NjMxMjNmMWMtZjYxMy00ZjMyLWFiYzUtYzBhZDdhYTY2YmU1OjQ3NWYwMzhkLTBlZmItNGM1ZS1iMzQ0LTAzMzYxOTkyYTRlMw==",
      "Accept": "application/json",
      "Basiq-Version": "3.0",
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "scope=SERVER_ACCESS",
  })
    .then((response) => {
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