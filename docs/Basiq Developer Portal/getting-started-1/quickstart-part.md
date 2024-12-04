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
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8f134fc-7f8dc12-Group_5_1.svg",
        "8f134fc-7f8dc12-Group_5_1.svg",
        1037,
        324,
        "#4f6772",
        null,
        "64e2beed5fd7230013237adb"
      ]
    }
  ]
}
[/block]
&nbsp;
## STEP 1: Register

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg">
<br />
<br />
<br />

Register your application via our [dashboard](https://dashboard.basiq.io/) and configure your application before creating a new API key. 

[block:callout]
{
  "type": "info",
  "body": "You can create as many API keys as you want, which allows you to use keys across different applications and environments. It’s a good idea to give each API key a meaningful name in order to differentiate between them.",
  "title": "API Keys"
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Keep your key secret",
  "body": "Make sure you copy and save the key we give you straight away, as it will only be exposed it in full once. Your API keys carry many privileges, so be sure to keep them secret! \n\nDo not share your API keys in publicly accessible areas such GitHub, client-side code, etc"
}
[/block]
## STEP 2: Authenticate
<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg">
<br />
<br />
<br />
Trade your new API key for an access token. 

The response will contain an access token which will allow you to make secure calls to the Basiq API. They expire every 60 minutes, so we recommend you store it globally and refresh 2-3 times an hour. 
[block:callout]
{
  "type": "info",
  "body": "The scope you supply will depend on the action you are performing, see the [authentication section](https://api.basiq.io/reference/authentication) for further detail. For this quick start we will be using `SERVER_ACCESS`.",
  "title": "Scope"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "var axios = require('axios');\nvar qs = require('qs');\nvar data = qs.stringify({\n  'scope': 'SERVER_ACCESS' \n})\n\nvar config = {\n  method: 'post',\n  url: 'https://au-api.basiq.io/token',\n  headers: { \n    'Authorization': `Basic ${YOUR_API_KEY}`, \n    'Content-Type': 'application/x-www-form-urlencoded', \n    'basiq-version': '3.0'\n  },\n  data : data\n};\n\naxios(config)\n  .then((response) => {\n  console.log(response.data)\n})\n  .catch((error) => {\n  console.log(error)\n})",
      "language": "javascript",
      "name": null
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/token' \\\n  --header 'Authorization: Basic $YOUR_API_KEY' \\\n  --header 'Content-Type: application/x-www-form-urlencoded' \\\n  --header 'basiq-version: 3.0' \\\n  --data-urlencode 'scope=SERVER_ACCESS'",
      "language": "curl",
      "name": "cURL"
    }
  ]
}
[/block]
## STEP 3: Create a user
<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg">
<br />
<br />
<br />
Creating a user gives you a "bucket" to store all your financial data.

Upon successful creation of a user, you will receive a `userId`. With that and the `access_token` you created earlier, you have everything you need to start creating and fetching financial data.
[block:code]
{
  "codes": [
    {
      "code": "var axios = require('axios');\nvar data = JSON.stringify({\n  \"email\": \"max@hooli.com\",\n  \"mobile\": \"+614xxxxxxxx\"\n});\n\nvar config = {\n  method: 'post',\n  url: 'https://au-api.basiq.io/users',\n  headers: { \n    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', \n    'Accept': 'application/json', \n    'Content-Type': 'application/json'\n  },\n  data: data\n};\n\naxios(config)\n.then(function (response) {\n  console.log(response.data);\n})\n.catch(function (error) {\n  console.log(error);\n});",
      "language": "javascript",
      "name": "Step 3: Create a User"
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/users' \\\n  --header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n  --header 'Accept: application/json' \\\n  --header 'Content-Type: application/json' \\\n  --data-raw '{\n    \"email\": \"max@hooli.com\",\n    \"mobile\": \"+614xxxxxxxx\"\n  }'",
      "language": "curl",
      "name": "cURL"
    }
  ]
}
[/block]
&nbsp;

## STEP 4: Consent & Connect via the Consent UI

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg">
<br />
<br />
<br />

Before you can retrieve a users financial data, you first need to link to their financial institutions by creating a connection. This can only be done once a user has explicitly consented to share their data. This can be done via the [Basiq Consent UI](https://api.basiq.io/docs/consent-ui). While you are starting out in sandbox mode, use the institutions and credentials provided [here](https://api.basiq.io/reference/testing).
[block:code]
{
  "codes": [
    {
      "code": "// STEP 4: Consent & Create a connection \n\nwindow.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}`;",
      "language": "javascript",
      "name": "Step 4: Create a Connection"
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/token' \\\n--header 'Authorization: Basic [YOUR-API-KEY]' \\\n--header 'Content-Type: application/x-www-form-urlencoded' \\\n--header 'basiq-version: 3.0' \\\n--data-urlencode 'scope=CLIENT_ACCESS' \\\n--data-urlencode 'userId=1234567-1234-1234-1234-123456781234'",
      "language": "curl",
      "name": "Client token bound to userID"
    }
  ]
}
[/block]
## STEP 5: Fetch your aggregated data
<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg">
<br />
<br />
<br />
Once you have successfully created a connection, you can go ahead and retrieve the data belonging to it. Let’s retrieve a list of all the accounts this user has connected through Basiq. 
[block:code]
{
  "codes": [
    {
      "code": "// STEP 5: Fetch your aggregated data \n\nvar axios = require('axios');\n\nvar config = {\n  method: 'get',\n  url: 'https://au-api.basiq.io/users/{user.id}/accounts',\n  headers: { \n    'Authorization': 'Bearer $YOUR_ACCESS_TOKEN', \n    'Accept': 'application/json'\n  }\n};\n\naxios(config)\n.then(function (response) {\n  console.log(response.data);\n})\n.catch(function (error) {\n  console.log(error);\n});",
      "language": "javascript",
      "name": "Step: Fetch accounts"
    },
    {
      "code": "curl --location --request GET 'https://au-api.basiq.io/users/a920c00f-df79-4a12-b711-2ac461c8090b/accounts' \\\n--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n--header 'Accept: application/json'",
      "language": "curl",
      "name": "cURL"
    }
  ]
}
[/block]
The response will contain an array of Account objects, containing specific account details such as the account number, balance and available funds.

#### **Congratulations! ** You have now created a user consent, connected a financial institution, and retrieved their financial data. 

&nbsp;

Feel free to deep dive into our [full API reference](https://api.basiq.io/) to see what else is possible with Basiq.