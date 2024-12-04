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
## STEP 4: Consent & Connect via the Consent UI

<img align="left" src="https://files.readme.io/263205a-Group_7_1.svg" />
<br />
<br />
<br />

Before you can retrieve a users financial data, you first need to link to their financial institutions by creating a connection. This can only be done once a user has explicitly consented to share their data. This can be done via the [Basiq Consent UI](https://api.basiq.io/docs/consent-ui). While you are starting out in sandbox mode, use the institutions and credentials provided [here](https://api.basiq.io/reference/testing).

```javascript STEP 4: Create a connection
// STEP 4: Consent & Create a connection 

window.location = `https://consent.basiq.io/home?userId=${userId}&token=${token}`;
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

#### **Congratulations!** You have now created a user consent, connected a financial institution, and retrieved their financial data.

Feel free to deep dive into our [full API reference](https://api.basiq.io/) to see what else is possible with Basiq.