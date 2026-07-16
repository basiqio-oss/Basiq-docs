---
title: Auth Token
description: >-
  This code is used to manage the authentication process for making requests to
  the Basiq API.
hidden: false
recipe:
  color: '#253050'
  icon: ''
---
```javascript JavaScript
// Importing required modules
const axios = require('axios'); // HTTP client library for making API requests
const qs = require('qs'); // Querystring library for encoding data

// Define the refresh interval for the server token (30 minutes)
const REFRESH_INTERVAL = 1000 * 60 * 30; // 30 minutes in milliseconds

// Initialize variables to store the server token and its refresh date
let serverToken = undefined;
let serverTokenRefreshDate = 0;

// Function to get the authorization header with the Basiq server token
export const getBasiqAuthorizationHeader = async () => {
  const token = await getServerToken();
  return `Bearer ${token}`;
};

// Function to get the server token
const getServerToken = async () => {
  if (!serverToken || Date.now() - serverTokenRefreshDate > REFRESH_INTERVAL) {
    // If there's no server token in memory or it's expired, fetch a new one
    await updateServerToken();
  }
  return serverToken;
};

// Function to update the server token
const updateServerToken = async () => {
  serverToken = await getNewServerToken(); // Fetch a new server token
  serverTokenRefreshDate = Date.now(); // Update the refresh date
};

// Function to fetch a new server token from the Basiq API
const getNewServerToken = async () => {
  const { data } = await axios.post(
    'https://au-api.basiq.io/token',
    qs.stringify({ scope: 'SERVER_ACCESS' }), // Requesting a token with SERVER_ACCESS scope
    {
      headers: {
        Authorization: `Basic ${process.env.BASIQ_API_KEY}`, // API key for authorization
        'Content-Type': 'application/x-www-form-urlencoded', // Set the content type
        'basiq-version': '3.0', // Specify the Basiq API version
      },
    }
  );
  return data.access_token; // Return the fetched access token
};

// Function to fetch a new client token for a specific user
export const getNewClientToken = async userId => {
  const { data } = await axios.post(
    'https://au-api.basiq.io/token',
    qs.stringify({ scope: 'CLIENT_ACCESS', userId }), // Requesting a token with CLIENT_ACCESS scope and userId
    {
      headers: {
        Authorization: `Basic ${process.env.BASIQ_API_KEY}`, // API key for authorization
        'Content-Type': 'application/x-www-form-urlencoded', // Set the content type
        'basiq-version': '3.0', // Specify the Basiq API version
      },
    }
  );
  return data.access_token; // Return the fetched access token
};

```

```json Response Example
{
  "access_token": "<<access_token>>",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

# Importing Dependencies

<!-- javascript@1-11 -->

Import the dependencies, with refresh intervals and initialise variables.

# Basiq Authorisation Header

<!-- javascript@ -->

The getBasiqAuthorizationHeader function is used to get the authorization header required for API requests. The getServerToken function manages the retrieval and refreshing of the server token. The updateServerToken function fetches a new server token using the API key, and the getNewClientToken function is used to fetch a client token with a specified user ID.

# Get Server Access Token

<!-- javascript@ -->

Function to fetch a new server token from the Basiq API.

# Get Client Access Token

<!-- javascript@ -->

It maintains a server token in memory and refreshes it only when it's expired.  

Remember that the process.env.BASIQ_API_KEY part is used to access an environment variable that should contain your Basiq API key. This key should be kept secure and not hard-coded directly in your code.