---
title: Retrieve a job
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
Retrieves the details of an existing job. You need only supply the unique job identifier that was returned upon job creation.
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*string, required*",
    "h-0": "Arguments",
    "0-1": "The identifier of the job to be retrieved."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns a job if a valid job ID was provided. Returns an[ error](https://api.basiq.io/docs/errors-1) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /jobs/{job.id}",
      "language": "json",
      "name": "Definition"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /jobs/61723 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2016-06-08T09:10:32.000Z\",\n  \"updated\": \"2016-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"in-progress\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Jobs with an MFA Challenge",
  "body": "When a user is presented with an MFA challenge, the job flow changes, and there is an additional step to consider; \n1. `verify-credentials`\n2. `mfa-challenge` : **only appears in MFA challenge flow**\n3. `retrieve-accounts`\n4.  `retrieve-transactions`\n\n. See below for the expected flow and how to handle this."
}
[/block]
The `mfa-challenge` step will go through a number of statuses before reaching sucess/failure: 

**Step 1: MFA challenge pending**: When job first starts, the `mfa-challenge` state will be set to `pending` with null result.
[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2021-06-08T09:10:32.000Z\",\n  \"updated\": \"2021-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"mfa-challenge\",\n      \"status\": \"pending\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"pending\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "STEP 1: MFA challenge pending"
    }
  ],
  "sidebar": true
}
[/block]
**Step 2: MFA challenge request**: When a job reaches the `mfa-challenge` step, the status will progress to `in-progress` and the result object with instructions on how to handle MFA will be present.
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"title\": \"mfa-challenge\",\n  \"status\": \"in-progress\",\n \t\"result\": {\n      \"type\": \"mfa\",\n      \"method\": \"token\",\n      \"description\": \"A SMS code has been sent to your device, please enter valid number\",\n      \"input\": [\n        \"OTP Password\"\n      ],\n      \"expiryMs\": 120000,\n      \"links\": {\n        \"response\": \"/jobs/61723/mfa\"\n      }\n    }\n}",
      "language": "json",
      "name": "STEP 2: MFA challenge: OTP"
    },
    {
      "code": "{\n  \"title\": \"mfa-challenge\",\n  \"status\": \"in-progress\",\n  \"result\": {\n    \"type\": \"mfa\",\n    \"method\": \"security-questions\",\n    \"description\": \"security-questions\",\n    \"input\": [\n      \"What's your favourite company?\",\n      \"What's the ID of this institution?\"\n    ],\n    \"expiryMs\": 120000,\n    \"links\": {\n      \"response\": \"https://au-api.basiq.io/jobs/61723/mfa\"\n    }\n  }\n}",
      "language": "json",
      "name": "STEP 2: MFA challenge: Question/s"
    }
  ],
  "sidebar": true
}
[/block]
**The client application should render visually the input for the MFA challenge** so that the end-user can supply a value - details on how to render this can be obtained from the result object. Once a value has been captured it should be posted to the URL supplied in the results attribute i.e. `/jobs/{job.id}/mfa`. See [MFA response](https://api.basiq.io/v2.1/reference/create-mfa-challenge-response). 

**Step 2: MFA skipped (*alternate* flow)**: In the event that an MFA challenge was not encountered, `mfa-challenge` will be present, with a status of skipped. No action is required, the flow will continue to retrieve accounts/transactions for that user. 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"title\": \"mfa-challenege\",\n  \"status\": \"skipped\",\n  \"result\": null\n}",
      "language": "json",
      "name": "STEP 2: MFA skipped (alternate flow)"
    }
  ],
  "sidebar": true
}
[/block]
**Step 3: MFA challenge in progress**: Once an MFA challenge response has been supplied, the `mfa-challenge` state will remain in the in-progress state. This state implies that the connector is carrying out its work, and no further action by the application client is required. The client application should continue to monitor the status of the job to handle future state changes.
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"title\": \"mfa-challenge\",\n   \"status\": \"in-progress\",\n   \"result\": null\n},",
      "language": "json",
      "name": "STEP 3: MFA challenge in progress"
    }
  ],
  "sidebar": true
}
[/block]
**Step 4: MFA failed (*alternate* flow - no retry)**
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"title\": \"mfa-challenge\",\n   \"status\": \"failed\",\n   \"result\": null\n},",
      "language": "json",
      "name": "STEP 4: MFA failed (alternate flow - no retry)"
    }
  ],
  "sidebar": true
}
[/block]
**Step 5: MFA challenge succeeded**: The MFA challenge has successfully completed so the job has progressed to next step to retrieve accounts and complete the job.
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2016-06-08T09:10:32.000Z\",\n  \"updated\": \"2016-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"mfa-challenge\",\n      \"status\": \"success\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"in-progress\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "STEP 5: MFA challenge succeeded"
    }
  ],
  "sidebar": true
}
[/block]