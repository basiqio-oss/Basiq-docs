---
title: Go-List for Upgrading to v3.0
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## 1. Update version in all your authentication requests

To upgrade to our version 3.0 of the API all you need to do is change the **basiq-version** header in the `/token` response to **3.0**

## 2. Include token scope in all your authentication requests

You can now specify either a **CLIENT\_ACCESS** or **SERVER\_ACCESS** scope in the `/token` request. 

Read more about authentication requests \[ [here](https://api.basiq.io/reference/authentication) ]

*example authentication request:*

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

*example authentication request with userId bound to CLIENT\_ACCESS token:*

```curl
curl --location --request POST 'https://au-api.basiq.io/token' \
--header 'Authorization: Basic [YOUR-API-KEY]' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'basiq-version: 3.0' \
--data-urlencode 'scope=CLIENT_ACCESS' \
--data-urlencode 'userId=1234567-1234-1234-1234-123456781234'
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

Read more about the Consent Policy Scopes \[ [here](https://api.basiq.io/docs/consent-scopes) ]

## 5. Learn about `/events` and Data Governance

With the the inclusion of the Consent UI and the increase of Data Governance please read the following pages

Events API \[ [here](https://api.basiq.io/reference/events) ]

Data Governance \[ [here](https://api.basiq.io/reference/data-governance#data-governance-events) ]

## 6. Retrieve a user's consent

Version 3.0 now supports the ability to fetch and delete a user's consent object.

Learn how to manage this data object in the API \[ [here](https://api.basiq.io/reference/user-consent) ]

## 7. How to utilise the Consent Flow

The Consent UI allows the passing of flags in order to complete certain `actions`. 

Read more about the Consent Flow \[ [here](https://api.basiq.io/docs/consent-ui#the-consent-flow) ]

## 8. MFA Support for DDC Connectors

The Consent UI handles MFA for first time connections. 

When refreshing connections if MFA is prompted you will need to handle this but it's quite simple! 

The job response will notify you of an MFA prompt

*example`/job` response with MFA step:*

```json MFA Challenge: OTP
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "job",
  "id": "61723",
  "created": "2021-06-08T09:10:32.000Z",
  "updated": "2021-06-08T09:14:28.000Z",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "success",
      "result": [
        {
          "type": "link",
          "url": "/users/ea3a81/connections/8fce3b"
        }
      ]
    },
    {
      "title": "mfa-challenge",
      "status": "in-progress",
      "result": [
        {
          "type": "mfa",
          "method": "token",
          "description": "A SMS code has been sent to your device, please enter valid number",
          "input": [
            "OTP Password"
          ],
          "expiryMs": 3600,
          "links": {
            "response": "/jobs/61723/mfa"
          }
        }
      ]
    },
    {
      "title": "retrieve-accounts",
      "status": "pending",
      "result": null
    },
    {
      "title": "retrieve-transactions",
      "status": "pending",
      "result": null
    }
  ],
  "links": {
    "self": "/jobs/61723",
    "source": "/users/ea3a81/connections/8fce3b"
  }
}
```
```json MFA Challenge: Question/s
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "job",
  "id": "61723",
  "created": "2021-06-08T09:10:32.000Z",
  "updated": "2021-06-08T09:14:28.000Z",
  "steps": [
    {
      "title": "verify-credentials",
      "status": "success",
      "result": [
        {
          "type": "link",
          "url": "/users/ea3a81/connections/8fce3b"
        }
      ]
    },
    {
      "title": "mfa-challenge",
      "status": "in-progress",
      "result": {
        "type": "mfa",
        "method": "security-questions",
        "description": "security-questions",
        "input": [
          "What's your favourite company?",
          "What's the ID of this institution?"
        ],
        "expiryMs": 120000,
        "links": {
          "response": "https://au-api.basiq.io/jobs/61723/mfa"
        }
      }
    },
    {
      "title": "retrieve-accounts",
      "status": "pending",
      "result": null
    },
    {
      "title": "retrieve-transactions",
      "status": "pending",
      "result": null
    }
  ],
  "links": {
    "self": "/jobs/61723",
    "source": "/users/ea3a81/connections/8fce3b"
  }
}
```

*example`/mfa` request:*

```curl
curl --location --request POST 'https://au-api.basiq.io/jobs/{job.id}/mfa' \
--header 'Authorization: Bearer {{client-access-token}}' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
  "mfa-response": ["1234"]
}'
```

See the API Reference Page \[ [here](https://api.basiq.io/reference/postjobmfa) ]
