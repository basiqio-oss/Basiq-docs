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
  description: ''
---
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
      "code": "// STEP 4: Consent & Create a connection \n\nwindow.location = `https://consent.basiq.io/home?userId=${userId}&token=${token}`;",
      "language": "javascript",
      "name": "STEP 4: Create a connection"
    },
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/users/a920c00f-df79-4a12-b711-2ac461c8090b/connections' \\\n--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--data-raw '{\n  \"loginId\": \"gavinBelson\",\n  \"password\": \"hooli2016\",\n  \"institution\":{\n    \"id\":\"AU00000\"\n  }\n}'",
      "language": "curl",
      "name": null
    }
  ],
  "sidebar": true
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
      "name": "STEP 5: Fetch accounts"
    },
    {
      "code": "curl --location --request GET 'https://au-api.basiq.io/users/a920c00f-df79-4a12-b711-2ac461c8090b/accounts' \\\n--header 'Authorization: Bearer $YOUR_ACCESS_TOKEN' \\\n--header 'Accept: application/json'",
      "language": "curl"
    }
  ],
  "sidebar": true
}
[/block]
The response will contain an array of Account objects, containing specific account details such as the account number, balance and available funds.

#### **Congratulations! ** You have now created a user consent, connected a financial institution, and retrieved their financial data. 

&nbsp;

Feel free to deep dive into our [full API reference](https://api.basiq.io/) to see what else is possible with Basiq.