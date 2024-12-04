---
title: Retrieve jobs
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
Retrieves the job details for an existing user for all jobs performed against that user over the previous 7 days. You need only supply the unique user identifier that was returned upon user creation. Jobs are returned in descending order of the *updated* field
[block:parameters]
{
  "data": {
    "0-0": "**[filter](https://api.basiq.io/docs/collections-filters)**\n*optional*",
    "h-0": "Arguments",
    "0-1": "This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following property: `connection.id`."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**
Returns an array of jobs if a valid user ID was provided. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/jobs",
      "language": "http",
      "name": "Defintion"
    },
    {
      "code": "$ curl \\\n-s https://api.intercom.io/users/5714dd359a3fd47136000001 \\\n-H 'Authorization:Bearer <Your access token>' \\\n-H 'Accept:application/json'",
      "language": "curl"
    },
    {
      "code": "POST /users/ea3a81 HTTP/1.1\nContent-Type: application/json\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n\n{\n  \"email\": \"gavin@hooli.xyz\"\n}",
      "language": "http",
      "name": "HTTP Request"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/ea3a81/jobs HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"size\": 2,\n  \"data\": [\n    {\n      \"type\": \"job\",\n      \"id\": \"3d7827b4\",\n      \"created\": \"2019-11-19T02:29:19Z\",\n      \"updated\": \"2019-11-19T02:29:21Z\",\n      \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00000\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n        }\n      },\n      \"steps\": [\n        {\n          \"title\": \"verify-credentials\",\n          \"status\": \"success\",\n          \"result\": {\n            \"type\": \"link\",\n            \"url\": \"/users/55bfd18/connections/5f84ff2\"\n          }\n        },\n        {\n          \"title\": \"retrieve-accounts\",\n          \"status\": \"success\",\n          \"result\": {\n            \"type\": \"link\",\n            \"url\": \"/users/55bfd18/accounts?filter=institution.id.eq('AU00000')\"\n          }\n        },\n        {\n          \"title\": \"retrieve-transactions\",\n          \"status\": \"in-progress\",\n          \"result\": null\n        }\n      ],\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/jobs/3d7827b4\",\n        \"source\": \"https://au-api.basiq.io/users/55bfd18/connections/5f84ff\"\n      }\n    },\n    {\n      \"type\": \"job\",\n      \"id\": \"ac85c3f\",\n      \"created\": \"2019-11-19T02:26:01Z\",\n      \"updated\": \"2019-11-19T02:27:50Z\",\n      \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00000\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n        }\n      },\n      \"steps\": [\n        {\n          \"title\": \"verify-credentials\",\n          \"status\": \"success\",\n          \"result\": {\n            \"type\": \"link\",\n            \"url\": \"/users/55bfd18/connections/c148bbb\"\n          }\n        },\n        {\n          \"title\": \"retrieve-accounts\",\n          \"status\": \"success\",\n          \"result\": {\n            \"type\": \"link\",\n            \"url\": \"/users/55bfd18/accounts?filter=institution.id.eq('AU00000')\"\n          }\n        },\n        {\n          \"title\": \"retrieve-transactions\",\n          \"status\": \"success\",\n          \"result\": {\n            \"type\": \"link\",\n            \"url\": \"/users/55bfd18/transactions?filter=institution.id.eq('AU00000')\"\n          }\n        }\n      ],\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/jobs/ac85c3f\",\n        \"source\": \"https://au-api.basiq.io/users/55bfd18/connections/c148bbb\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/55bfd18/jobs\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]