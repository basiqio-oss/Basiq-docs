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
    // POST request to get the token
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
      .then((response) => response.json())
      .then((data) => {
        console.log("Token response:", data); // Log the response from the token request
        if (data && data.access_token) {
          setToken(data.access_token); // Set the token state if the token is returned
        } else {
          setError("No access token received.");
        }
      })
      .catch((error) => {
        console.error("Error fetching token:", error);
        setError("Error fetching token.");
      })
      .finally(() => {
        setLoading(false); // Stop loading once the request is complete
      });
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