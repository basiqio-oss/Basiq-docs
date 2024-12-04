---
title: 'Quickstart: part 2'
excerpt: Collect and retrieve financial data in 10 minutes.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: >-
    Now you're integrated with the Basiq API, you can start looking at your UI
    integration options.
  pages:
    - type: basic
      slug: ui-integration-options-1
      title: UI Integration Options
---
<Image width="80%" src="https://files.readme.io/f187581-Group_3_1.svg" />

## STEP 4: Create a Connection

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />

<br />
<br />
<br />

Before you can retrieve a users financial data, you first need to link to their financial institutions by creating a connection. Do this by making a post request with the institution and login credentials. While you are starting out in sandbox mode, use the institutions and credentials provided [here](https://api.basiq.io/reference/testing).

```javascript STEP 4: Create a connection
// STEP 4: Create a connection 

var axios = require('axios');
var data = JSON.stringify({
  "loginId": "gavinBelson",
  "password": "hooli2016",
  "institution": {
    "id": "AU00000"
  }
});

var config = {
  method: 'post',
  url: 'https://au-api.basiq.io/users/{user.id}/connections',
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
```
```curl
curl --location --request POST 'https://au-api.basiq.io/users/a920c00f-df79-4a12-b711-2ac461c8090b/connections' \
--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "loginId": "gavinBelson",
  "password": "hooli2016",
  "institution":{
    "id":"AU00000"
  }
}'
```

> 📘 This guide is only using Node.js to demonstrate a backend integration and does not cover the UI options Basiq offers when connecting a users financial institutions. If you are ready to start building out your UI, see our UI Integration Options to understand what best suits you.

## STEP 5: Fetch your aggregated data

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />

<br />
<br />
<br />

Once you have successfully created a connection, you can go ahead and retrieve the data belonging to it. Let’s retrieve a list of all the accounts this user has connected through Basiq. 

```javascript STEP 5: Fetch accounts
// STEP 5: Fetch your aggregated data 

var axios = require('axios');

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
```curl
curl --location --request GET 'https://au-api.basiq.io/users/a920c00f-df79-4a12-b711-2ac461c8090b/accounts' \
--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
--header 'Accept: application/json'
```

The response will contain an array of Account objects, containing specific account details such as the account number, balance and available funds.

#### **Congratulations!** You have now connected a financial institution, and retrieved their financial data.

Feel free to deep dive into our [full API reference](https://api.basiq.io/) to see what else is possible with Basiq.