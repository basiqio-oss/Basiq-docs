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
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7f8dc12-Group_5_1.svg",
        "Group 5 (1).svg",
        1037,
        324,
        "#4f6772"
      ],
      "sizing": "80"
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

*Ensure you toggle on "Enable 3.0" when you are setting up your application."*
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
  "body": "Make sure you copy and save the key we give you straight away, as it will only be exposed it in full once. Your API keys carry many privileges, so be sure to keep them secret! \n\nDo not share your API keys in publicly accessible areas such GitHub, client-side code, etc",
  "title": "Keep your key secret"
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
      "name": "STEP 2: Authenticate"
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/token' \\\n  --header 'Authorization: Basic $YOUR_API_KEY' \\\n  --header 'Content-Type: application/x-www-form-urlencoded' \\\n  --header 'basiq-version: 2.0' \\\n  --data-urlencode 'scope=SERVER_ACCESS'",
      "language": "curl"
    }
  ],
  "sidebar": true
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
      "name": "STEP 3: Create a user"
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/users' \\\n  --header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n  --header 'Accept: application/json' \\\n  --header 'Content-Type: application/json' \\\n  --data-raw '{\n    \"email\": \"max@hooli.com\",\n    \"mobile\": \"+614xxxxxxxx\"\n  }'",
      "language": "curl"
    }
  ],
  "sidebar": true
}
[/block]
#### **Congratulations! ** You have registered your application, and made your first, authenticated call to Basiq to create a user!