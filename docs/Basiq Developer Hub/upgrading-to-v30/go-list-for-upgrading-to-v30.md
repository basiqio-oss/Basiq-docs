---
title: Go-List for Upgrading to v3.0
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
## 1. Update version in all your authorisation requests

To upgrade to our version 3.0 of the API all you need to do is change the **basiq-version** header in the `/token` response to **3.0**

## 2. Include token scope in all your authorisation requests

You can now specify either a **CLIENT\_ACCESS** or **SERVER\_ACCESS** scope in the `/token` request. 

Read more about authorisation requests \[ [here](https://api.basiq.io/reference/authentication) ]

*example authorisation request:*

```curl
curl --location --request POST 'https://au-api.basiq.io/token' \
--header 'Authorization: Basic [YOUR-API-KEY]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'basiq-version: 3.0' \
--data-urlencode 'scope=SERVER_ACCESS' \
```

## 3. Upgrade to the Consent UI

3.0 version of the API uses Basiq's Consent UI - you no longer need to manage creating connections via the `/connections` endpoint. 

Read more about the Consent UI \[ [here](https://api.basiq.io/docs/consent-ui) ]

*example authorisation request with userId bound to CLIENT\_ACCESS token:*

```curl
curl --location --request POST 'https://au-api.basiq.io/token' \
--header 'Authorization: Basic [YOUR-API-KEY]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'basiq-version: 3.0' \
--data-urlencode 'scope=CLIENT_ACCESS' \
--data-urlencode 'userId=e6f5a9e3-62b8-40ec-9b7f-5629577384ef'
```

*example code on configuring Consent UI url:*

```javascript
// Redirect to the external Basiq Consent UI to connect
  async function goToConsent(action = null) {
    let userId = sessionStorage.getItem("userId");
    const token = await getClientToken(userId);
    window.location = (`https://consent.basiq.io/home?&token=${token}&action=${action}`);
  }

<Button onClick={goToConsent}>Connect your accounts</Button>
```

## 4. Configure your Consent UI and Consent Policy

You can modify the Consent UI to suit your needs - this includes updating the Consent Policy and updating the UI with your own branding. 

Read more about the Consent UI \[ [here](https://api.basiq.io/docs/dash-configuration) ]

## 5. Learn about `/events` and Data Governance

With the the inclusion of the Consent UI and the increase of Data Governance please read the following pages

* Events API \[ [here](https://api.basiq.io/reference/events) ]

* Data Governance \[ [here](https://api.basiq.io/reference/data-governance#data-governance-events) ]

## 6. Retrieve a user's consent

Version 3.0 now supports the ability to fetch and delete a user's consent object.

Learn how to manage this data object in the API \[ [here](https://api.basiq.io/reference/user-consent) ]

## 7. How to utilise the Consent Flow

The Consent UI allows the passing of flags in order to complete certain `actions`. 

Read more about the Consent Flow \[ [here](https://api.basiq.io/docs/consent-ui#the-consent-flow) ]
