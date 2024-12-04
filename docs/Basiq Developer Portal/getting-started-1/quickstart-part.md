---
title: 'Quickstart: API''s'
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
![1037](https://files.readme.io/8f134fc-7f8dc12-Group_5_1.svg "8f134fc-7f8dc12-Group_5_1.svg")

## STEP 1: Register

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />
<br />
<br />
<br />

Register your application via our [dashboard](https://dashboard.basiq.io/) and configure your application before creating a new API key.

> 📘 API Keys
>
> You can create as many API keys as you want, which allows you to use keys across different applications and environments. It’s a good idea to give each API key a meaningful name in order to differentiate between them.

> 🚧 Keep your key secret
>
> Make sure you copy and save the key we give you straight away, as it will only be exposed it in full once. Your API keys carry many privileges, so be sure to keep them secret!
>
> Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc

## STEP 2: Authenticate

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />
<br />
<br />
<br />
Trade your new API key for an access token.

The response will contain an access token which will allow you to make secure calls to the Basiq API. They expire every 60 minutes, so we recommend you store it globally and refresh 2-3 times an hour.

> 📘 Scope
>
> The scope you supply will depend on the action you are performing, see the [authentication section](https://api.basiq.io/reference/authentication) for further detail. For this quick start we will be using `SERVER_ACCESS`.

```javascript
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
```
```curl cURL
curl --location --request POST 'https://au-api.basiq.io/token' \
  --header 'Authorization: Basic $YOUR_API_KEY' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'basiq-version: 3.0' \
  --data-urlencode 'scope=SERVER_ACCESS'
```

## STEP 3: Create a user

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />
<br />
<br />
<br />
Creating a user gives you a "bucket" to store all your financial data.

Upon successful creation of a user, you will receive a `userId`. With that and the `access_token` you created earlier, you have everything you need to start creating and fetching financial data.

```javascript Step 3: Create a User
var axios = require('axios');
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
```
```curl cURL
curl --location --request POST 'https://au-api.basiq.io/users' \
  --header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "email": "max@hooli.com",
    "mobile": "+614xxxxxxxx"
  }'
```

## STEP 4: Consent & Connect via the Consent UI

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />
<br />
<br />
<br />

Before you can retrieve a users financial data, you first need to link to their financial institutions by creating a connection. This can only be done once a user has explicitly consented to share their data. This can be done via the [Basiq Consent UI](https://api.basiq.io/docs/consent-ui). While you are starting out in sandbox mode, use the institutions and credentials provided [here](https://api.basiq.io/reference/testing).

```javascript Step 4: Create a Connection
// STEP 4: Consent & Create a connection 

window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}`;
```
```curl Client token bound to userID
curl --location --request POST 'https://au-api.basiq.io/token' \
--header 'Authorization: Basic [YOUR-API-KEY]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'basiq-version: 3.0' \
--data-urlencode 'scope=CLIENT_ACCESS' \
--data-urlencode 'userId=1234567-1234-1234-1234-123456781234'
```

## STEP 5: Fetch your aggregated data

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />
<br />
<br />
<br />
Once you have successfully created a connection, you can go ahead and retrieve the data belonging to it. Let’s retrieve a list of all the accounts this user has connected through Basiq.

```javascript Step: Fetch accounts
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
```curl cURL
curl --location --request GET 'https://au-api.basiq.io/users/a920c00f-df79-4a12-b711-2ac461c8090b/accounts' \
--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
--header 'Accept: application/json'
```

The response will contain an array of Account objects, containing specific account details such as the account number, balance and available funds.

#### **Congratulations!** You have now created a user consent, connected a financial institution, and retrieved their financial data.

Feel free to deep dive into our [full API reference](https://api.basiq.io/) to see what else is possible with Basiq.