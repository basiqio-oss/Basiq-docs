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
    "0-0": "**id**\n*required*",
    "h-0": "Arguments",
    "0-1": "The identifier of the job to be retrieved."
  },
  "cols": 2,
  "rows": 1
}
[/block]
Returns
Returns a job if a valid job ID was provided. Returns an[ error](https://basiq.readme.io/v1.0/reference#errors) otherwise.
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"created\": \"2016-06-08T09:10:32.000Z\",\n  \"updated\": \"2016-06-08T09:14:28.000Z\",\n  \"steps\": [\n    {\n      \"title\": \"verify-credentials\",\n      \"status\": \"success\",\n      \"result\": [\n        {\n          \"type\": \"link\",\n          \"url\": \"/users/ea3a81/connections/8fce3b\"\n        }\n      ]\n    },\n    {\n      \"title\": \"retrieve-accounts\",\n        \"status\": \"in-progress\",\n        \"result\": null\n    },\n    {\n      \"title\": \"retrieve-transactions\",\n      \"status\": \"pending\",\n      \"result\": null\n    }\n  ],\n  \"links\": {\n    \"self\": \"/jobs/61723\",\n    \"source\": \"/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]