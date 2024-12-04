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

You can now specify either a **CLIENT_ACCESS** or **SERVER_ACCESS** scope in the `/token` request. 

Read more about authentication requests [ [here](https://api.basiq.io/reference/authentication) ]

*example authentication request:*
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/token' \\\n--header 'Authorization: Basic [YOUR-API-KEY]' \\\n--header 'Content-Type: application/x-www-form-urlencoded' \\\n--header 'basiq-version: 3.0' \\\n--data-urlencode 'scope=SERVER_ACCESS' \\\n",
      "language": "curl"
    }
  ]
}
[/block]
## 3. Upgrade to the Consent UI

3.0 version of the API uses Basiq's Consent UI - you no longer need to manage creating connections via the `/connections` endpoint. 

Read more about the Consent UI [ [here](https://api.basiq.io/docs/consent-ui) ]

*example authentication request with userId bound to CLIENT_ACCESS token:*
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/token' \\\n--header 'Authorization: Basic [YOUR-API-KEY]' \\\n--header 'Content-Type: application/x-www-form-urlencoded' \\\n--header 'basiq-version: 3.0' \\\n--data-urlencode 'scope=CLIENT_ACCESS' \\\n--data-urlencode 'userId=1234567-1234-1234-1234-123456781234'",
      "language": "curl"
    }
  ]
}
[/block]
*example code on configuring Consent UI url:*
[block:code]
{
  "codes": [
    {
      "code": "// Redirect to the external Basiq Consent UI to connect\n  async function goToConsent(action = null) {\n    let userId = sessionStorage.getItem(\"userId\");\n    const token = await getClientToken(userId);\n    window.location = (`https://consent.basiq.io/home?&token=${token}&action=${action}`);\n  }\n\n<Button onClick={goToConsent}>Connect your accounts</Button>",
      "language": "javascript"
    }
  ]
}
[/block]
## 4. Configure your Consent UI and Consent Policy

You can modify the Consent UI to suit your needs - this includes updating the Consent Policy and updating the UI with your own branding. 

Read more about the Consent UI [ [here](https://api.basiq.io/docs/dash-configuration) ]

Read more about the Consent Policy Scopes [ [here](https://api.basiq.io/docs/consent-scopes) ]


## 5. Learn about `/events` and Data Governance 

With the the inclusion of the Consent UI and the increase of Data Governance please read the following pages

Events API [ [here](https://api.basiq.io/reference/events) ]

Data Governance [ [here](https://api.basiq.io/reference/data-governance#data-governance-events) ]


## 6. Retrieve a user's consent

Version 3.0 now supports the ability to fetch and delete a user's consent object.

Learn how to manage this data object in the API [ [here](https://api.basiq.io/reference/user-consent) ]


## 7. How to utilise the Consent Flow 

The Consent UI allows the passing of flags in order to complete certain `actions`. 

Read more about the Consent Flow [ [here](https://api.basiq.io/docs/consent-ui#the-consent-flow) ]


## 8. MFA Support for DDC Connectors

The Consent UI handles MFA for first time connections. 

When refreshing connections if MFA is prompted you will need to handle this but it's quite simple! 

The job response will notify you of an MFA prompt


*example `/job` response with MFA step:*
[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2021-06-08T09:10:32.000Z\",\n  \"updated\": \"2021-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"mfa-challenge\",\n      \"status\": \"in-progress\",\n      \"result\": [\n        {\n          \"type\": \"mfa\",\n          \"method\": \"token\",\n          \"description\": \"A SMS code has been sent to your device, please enter valid number\",\n          \"input\": [\n            \"OTP Password\"\n          ],\n          \"expiryMs\": 3600,\n          \"links\": {\n            \"response\": \"/jobs/61723/mfa\"\n          }\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"pending\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "MFA Challenge: OTP"
    },
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2021-06-08T09:10:32.000Z\",\n  \"updated\": \"2021-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"mfa-challenge\",\n      \"status\": \"in-progress\",\n      \"result\": {\n        \"type\": \"mfa\",\n        \"method\": \"security-questions\",\n        \"description\": \"security-questions\",\n        \"input\": [\n          \"What's your favourite company?\",\n          \"What's the ID of this institution?\"\n        ],\n        \"expiryMs\": 120000,\n        \"links\": {\n          \"response\": \"https://au-api.basiq.io/jobs/61723/mfa\"\n        }\n      }\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"pending\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "MFA Challenge: Question/s"
    }
  ]
}
[/block]
*example `/mfa` request:*
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://au-api.basiq.io/jobs/{job.id}/mfa' \\\n--header 'Authorization: Bearer {{client-access-token}}' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--data-raw '{\n  \"mfa-response\": [\"1234\"]\n}'",
      "language": "curl"
    }
  ]
}
[/block]
See the API Reference Page [ [here](https://api.basiq.io/reference/postjobmfa) ]