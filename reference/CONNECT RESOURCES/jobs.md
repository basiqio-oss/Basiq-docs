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

Establish successful authentication with institution
Fetch latest list of accounts
Fetch latest list of transactions
You can keep track of the steps that have been completed by observing the results array property. As each step is successfully completed, its status will be updated and a result object with the link to the affected resource will be present. In the event that a step has failed, the result object will contain an embedded `error` object.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**type**\n*readonly*",
    "0-1": "Value is \"job\".",
    "1-0": "**id**\n*readonly*",
    "1-1": "A string that uniquely identifies the job.",
    "2-0": "**created**\n*readonly*",
    "2-1": "The date time when the job was created.",
    "3-0": "**updated**\n*readonly*",
    "3-1": "The date time when the job was last updated.",
    "4-0": "**steps**\n*readonly*",
    "4-1": "List of steps that need to be completed. With the following properties:\n\n- **title** - Name of the step the job needs to complete.\n- **status** - Step status: `pending`, `in-progress`, `success`, `failed`.\n- **result** - List of URLs of the updated (or created) resources. Otherwise if a step `failed` contains an [error](https://basiq.readme.io/v2.0/reference#errors) response",
    "5-0": "**links**\n*readonly*",
    "5-1": "Links to the following resources:\n- **self** - URL of job resource\n- **source** - Resource that initiated creation of this Job. For example, for operations on [Connection](https://basiq.readme.io/v2.0/reference#connections), this is a Connection URL"
  },
  "cols": 2,
  "rows": 6
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
      "code": "{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2016-06-08T09:10:32.000Z\",\n  \"updated\": \"2016-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/accounts?filter=connection.id.eq(8fce3b)\"\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"in-progress\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "Example Job Object"
    }
  ],
  "sidebar": true
}
[/block]