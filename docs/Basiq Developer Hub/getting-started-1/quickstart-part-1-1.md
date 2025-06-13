---
title: 'Quickstart: part 1'
excerpt: Make your first call to the Basiq API.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
<Image align="center" width="80%" src="https://files.readme.io/7f8dc12-Group_5_1.svg" />

## STEP 1: Register

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />

Register your application via our [dashboard](https://dashboard.basiq.io/) and create a new API key under the Developers tab.

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

Trade your new API key for an access token.

The response will contain an access token which will allow you to make secure calls to the Basiq API. They expire every 60 minutes, so we recommend you store it globally and refresh 2-3 times an hour.

> 📘 Scope
>
> The scope you supply will depend on the action you are performing, see the [authentication section](https://api.basiq.io/v2.1/reference/authentication) for further detail. For this quick start we will be using `SERVER_ACCESS`.

```javascript STEP 2: Authenticate
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
    'basiq-version': '2.0'
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
```Text cURL
curl --location --request POST 'https://au-api.basiq.io/token' \
  --header 'Authorization: Basic $YOUR_API_KEY' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'basiq-version: 2.0' \
  --data-urlencode 'scope=SERVER_ACCESS'
```

## STEP 3: Create a user

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />

Creating a user gives you a "bucket" to store all your financial data.

Upon successful creation of a user, you will receive a `userId`. With that and the `access_token` you created earlier, you have everything you need to start creating and fetching financial data.

```javascript STEP 3: Create a user
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
```curl
curl --location --request POST 'https://au-api.basiq.io/users' \
  --header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "email": "max@hooli.com",
    "mobile": "+614xxxxxxxx"
  }'
```

#### **Congratulations!** You have registered your application, and made your first, authenticated call to Basiq to create a user!