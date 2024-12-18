---
title: 'Quickstart: API'
excerpt: Make your first call to the Basiq API.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<Image align="center" alt={1037} border={false} caption="Quickstart" title="Group 5 (1).svg" src="https://files.readme.io/7f8dc12-Group_5_1.svg" width="60% " />

 

## STEP 1: Register

<Image align="left" src="https://files.readme.io/1433553-263205a-Group_7_1.svg" />

<br />

<br />

To begin, register your application via our [dashboard](https://dashboard.basiq.io/) and configure it accordingly. Before proceeding to create a new API key, ensure your application settings are in order.

> 📘 API Keys
>
> You can create as many API keys as you want, which allows you to use keys across different applications and environments. It’s a good idea to give each API key a meaningful name in order to differentiate between them.

> 🚧 Keep your key secret
>
> Make sure you copy and save the key we give you straight away, as it will only be exposed it in full once. Your API keys carry many privileges, so be sure to keep them secret!
>
> Do not share your API keys in publicly accessible areas such GitHub, client-side code, etc

## STEP 2: Authenticate

Exchange your newly acquired API key for an access token. This token enables secure interactions with the Basiq API and expires every 60 minutes. We recommend storing it globally and refreshing it 2-3 times per hour.

> 📘 Scope
>
> The scope you supply will depend on the action you are performing, see the [authentication section](https://api.basiq.io/reference/authentication) for further detail. For this quick start we will be using `SERVER_ACCESS`.

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
```curl
curl --location --request POST 'https://au-api.basiq.io/token' \
  --header 'Authorization: Basic $YOUR_API_KEY' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'basiq-version: 3.0' \
  --data-urlencode 'scope=SERVER_ACCESS'
```

## STEP 3: Create a user

Creating a user establishes a repository for all financial data. Upon successful creation, you'll receive a userId. With this and the previously acquired access token, you possess all the necessary components to commence creating and fetching financial data.

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

## STEP 4: Consent & Connect via the Consent UI

Before you can retrieve a users financial data, you first need to link to their financial institutions by creating a connection. This can only be done once a user has explicitly consented to share their data. This can be done via the [Basiq Consent UI](https://api.basiq.io/docs/consent#consent-ui). While you are starting out in sandbox mode, use the institutions and credentials provided [here](https://api.basiq.io/reference/testing).

```javascript STEP 4: Create a connection
// STEP 4: Consent & Create a connection 

window.location = `https://consent.basiq.io/home?token={{client_token_bound_to_userId}}`;
```
```curl CLIENT token bound to userID
curl --location --request POST 'https://au-api.basiq.io/token' \
--header 'Authorization: Basic [YOUR-API-KEY]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'basiq-version: 3.0' \
--data-urlencode 'scope=CLIENT_ACCESS' \
--data-urlencode 'userId=1234567-1234-1234-1234-123456781234'
```

## STEP 5: Fetch Job History

After completing the consent journey and creating a connection, the consent UI will return a jobID or multiple jobIds if there are multiple connections in the consent UI.

Use the following cURL command to fetch job history:

```curl
curl --request GET \
     --url https://au-api.basiq.io/jobs/jobId \
     --header 'accept: application/json'
```

The job response will contain three steps associated if this is a data connector job.

```json
{
  "type": "job",
  "id": "e9132638",
  "created": "2020-06-10T09:59:00Z",
  "updated": "2020-06-10T09:59:00Z",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "success",
      "result": {
        "type": "link",
        "url": "/users/ea3a81/connections/8fce3b"
      }
    },
    {
      "title": "retrieve-accounts",
      "status": "in-progress",
      "result": null
    },
    {
      "title": "retrieve-transactions",
      "status": "pending",
      "result": null
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/jobs/61723",
    "source": "https://au-api.basiq.io/users/ea3a81/connections/8fce3b"
  }
}
```

Upon successful completion of all three steps, the job moves to the fetch stage to retrieve the data.

To ensure you receive the data once it's available, continue polling this jobs endpoint until you receive a success status for all three steps. Once all steps are successfully completed, you can proceed to fetch the data.

## STEP 6: Fetch your aggregated data

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

<div
  style={{
    border: "2px solid #4e9ccf", // Classic blue border
    borderRadius: "8px",
    backgroundColor: "#e3f2fd", // Light blue background (cascade effect)
    padding: "16px",
    margin: "16px 0",
    fontFamily: "Arial, sans-serif",
    color: "#333", // Dark text for readability
  }}
>
  <strong style={{ color: "#1e88e5" }}>📢 Attention!</strong> If you have any issues, please reach out to our amazing support team.

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
        padding: '12px 30px',
        backgroundColor: '#1e88e5', // Classic blue button color
        color: '#ffffff',
        border: 'none',
        borderRadius: '50px',
        fontSize: '16px',
        fontWeight: '600',
        textTransform: 'uppercase',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
        outline: 'none',
        display: 'flex',
        justifyContent: 'center',
        height: '45px',
        position: 'relative',
        overflow: 'hidden',
        marginLeft: '10px', // Add space between text and button
        minWidth: '150px', // Ensure the button has enough width for the text
      }}
      onMouseEnter={(e) => {
        e.target.style.transform = 'scale(1.1)';
        e.target.style.backgroundColor = '#1565c0'; // Darker blue on hover
      }}
      onMouseLeave={(e) => {
        e.target.style.transform = 'scale(1)';
        e.target.style.backgroundColor = '#1e88e5'; // Original blue
      }}
    >
      Support team
    </button>
  </div>
</div>