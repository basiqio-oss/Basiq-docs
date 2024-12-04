---
title: Jobs
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
Some of the services provided by Basiq are quite resource intensive, and may take a little time to process. To ensure that we provide a pleasant experience to you and your end-users, and that we avoid timeouts of long running connections to our server - we will handle these processes (jobs) asynchronously.

Asynchronous operations are great as they enable us to return an immediate result when an endpoint is queried, and also enable us to scale the requests optimally behind the scenes.

When an asynchronous operation is initiated (e.g. refreshing a connection) the Basiq server will create a job resource and return a status code of 202 - Accepted along with the job details (in the body). You can then query the job url to track its progress.

**Tracking the status of a job**

Every step of the job has a status property that depicts its current state. The possible status values for each step are as follows:

- `pending` - The job has been created and is waiting to be started.
- `in-progress` - The job has started and is currently processing.
- `success` - The job has successfully completed.
- `failed` - The job has failed.


**Find out what steps have been completed**

Depending on the job being executed, some jobs will have multiple steps which need to be executed, for e.g. refreshing a connection requires the following steps to be completed:

  1.  Establish successful authentication with institution
  2. Fetch latest list of accounts
  3. Fetch latest list of transactions

You can keep track of the steps that have been completed by observing the results array property. As each step is successfully completed, its status will be updated and a result object with the link to the affected resource will be present. In the event that a step has failed, the result object will contain an embedded `error` object.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "`type`",
    "0-1": "Value is \"job\".",
    "2-0": "`id`",
    "2-1": "A string that uniquely identifies the job.",
    "4-0": "`created`",
    "4-1": "The date time when the job was created.",
    "6-0": "`updated`",
    "6-1": "The date time when the job was last updated.",
    "8-0": "`steps`",
    "8-1": "List of steps that need to be completed. With the following properties:",
    "12-0": "`links`",
    "12-1": "Links to the following resources:",
    "14-1": "- `self` - URL of job resource\n\n- `source` - Resource that initiated creation of this Job. For example, for operations on [Connection](https://basiq.readme.io/v2.1/reference/connections), this is a Connection URL.  This is only returned for Connection jobs and not for Statement jobs.",
    "10-1": "- `title` - Name of the step the job needs to complete e.g. \"verify-credentials\"\n\n- `status` - Step status: `pending`, `in-progress`, `success`, `failed`.\n\n- `result` - List of URLs of the updated (or created) resources. \n       - `type` :e.g. \"link\"\n       - `url`: url to resource\n\nOtherwise if a step `failed` contains an [error](https://api.basiq.io/docs/errors-1) response"
  },
  "cols": 2,
  "rows": 16
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e8ecae5-job.png",
        "job.png",
        708,
        731,
        "#9faea0"
      ]
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2016-06-08T09:10:32.000Z\",\n  \"updated\": \"2016-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/accounts?filter=institution.id.eq('AU00000')\"\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"in-progress\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "Example Job Object"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Below is detailed the list of resources relating to the `mfa-challenge` step to engage rendering of challenge and completion of connection.",
  "title": "Alternate flow with MFA challenge step"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Result (type = mfa)",
    "0-0": "`type`",
    "0-1": "Type of resource e.g. \"mfa\"",
    "2-0": "`method`",
    "2-1": "This will list out the type of mfa challenge presented to the user. The values can include:",
    "6-0": "`description`",
    "6-1": "A description to be presented to the user that includes instructions e.g. \"An SMS code has been sent to your device, please enter valid number\"",
    "8-1": "An array of inputs (mfa challenges) that he end-user must complete. e.g. \"OTP Password\"",
    "4-1": "- `token` - The user is asked to enter the token associated with the account. This token may be generated by an app like Google Authenticator or delivered to the user via email, SMS or phone.\n\n - `security-questions` -  Security questions are a type of knowledge-based authentication (KBA) where the user is presented with a series of personal questions that they are meant to answer.",
    "8-0": "`input`",
    "10-0": "`expiryMs`",
    "10-1": "Maximum time to enter MFA before expiry e.g. 3600",
    "12-1": "Array of links to the following resources:",
    "12-0": "`links`",
    "14-1": "- `response` The URL where the input responses must be submitted."
  },
  "cols": 2,
  "rows": 16
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2021-06-08T09:10:32.000Z\",\n  \"updated\": \"2021-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"mfa-challenge\",\n      \"status\": \"in-progress\",\n      \"result\": [\n        {\n          \"type\": \"mfa\",\n          \"method\": \"token\",\n          \"description\": \"A SMS code has been sent to your device, please enter valid number\",\n          \"input\": [\n            \"OTP Password\"\n          ],\n          \"expiryMs\": 3600,\n          \"links\": {\n            \"response\": \"/jobs/61723/mfa\"\n          }\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"pending\",\n      \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "Example Job object with MFA challenge"
    }
  ],
  "sidebar": true
}
[/block]