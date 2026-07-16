---
title: Account Verification
description: >-
  Account verification involves connecting to a user's bank account and
  retrieving their financial data for various purposes like identity
  verification or financial analysis.
hidden: true
recipe:
  color: '#018FF4'
  icon: ''
---
```javascript JavaScript
var axios = require('axios');
var qs = require('qs');
var data = qs.stringify({
  'scope': 'SERVER_ACCESS' 
})

var config = {
  method: 'post',
  url: 'https://au-api.basiq.io/token',
  headers: { 
    'Authorization': `Basic ${YOUR_API_KEY}`, 
    'Content-Type': 'application/x-www-form-urlencoded', 
    'basiq-version': '3.0'
  },
  data : data
};

axios(config)
  .then((response) => {
  console.log(response.data)
})
  .catch((error) => {
  console.log(error)
})

var data = JSON.stringify({
  "email": "max@hooli.com",
  "mobile": "+614xxxxxxxx"
});

var config = {
  method: 'post',
  url: 'https://au-api.basiq.io/users',
  headers: { 
    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', 
    'Accept': 'application/json', 
    'Content-Type': 'application/json'
  },
  data: data
};

axios(config)
.then(function (response) {
  console.log(response.data);
})
.catch(function (error) {
  console.log(error);
});

window.location = `https://consent.basiq.io/home?token=${token}`;

var config = {
  method: 'get',
  url: 'https://au-api.basiq.io/users/{user.id}/accounts',
  headers: { 
    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', 
    'Accept': 'application/json'
  }
};

axios(config)
.then(function (response) {
  console.log(response.data);
})
.catch(function (error) {
  console.log(error);
});

```

```json Response Example
{"success":true}
```

# Authenticate your application

<!-- javascript@1-24 -->

Trade your new API key for an access token.
The response will contain an access token which will allow you to make secure calls to the Basiq API. They expire every 60 minutes, so we recommend you store it globally and refresh 2-3 times an hour.

# Create a user

<!-- javascript@26-48 -->

Creating a user gives you a "bucket" to store all your financial data.
Upon successful creation of a user, you will receive a userId. With that and the access_token you created earlier, you have everything you need to start creating and fetching financial data.

# Consent & Connect via the Consent UI

<!-- javascript@50 -->

Before you can retrieve a users financial data, you first need to link to their financial institutions by creating a connection. This can only be done once a user has explicitly consented to share their data. This can be done via the Basiq Consent UI. While you are starting out in sandbox mode, use the institutions and credentials provided here.

# Fetch your consented data

<!-- javascript@52-67 -->

Once you have successfully created a connection, you can go ahead and retrieve the data belonging to it. Let’s retrieve a list of all the accounts this user has connected through Basiq.