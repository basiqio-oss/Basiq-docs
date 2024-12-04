---
title: Refresh a connection
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
Use this to retrieve the latest financial data. Similar to when a connection is first created, the refresh resource will initiate the following series of steps to retrieve the latest financial data from the target institution:
[block:parameters]
{
  "data": {
    "h-0": "#",
    "h-1": "Step",
    "h-2": "Description",
    "0-0": "1",
    "2-0": "2",
    "4-0": "3",
    "0-1": "verify-credentials",
    "2-1": "retrieve-accounts",
    "4-1": "retrieve-transactions",
    "0-2": "The server will attempt to authenticate with the target institution using the supplied credentials",
    "2-2": "The server will retrieve the complete list of accounts and their details e.g. account number, name and balances",
    "4-2": "The server will fetch the associated transactions for each of the accounts"
  },
  "cols": 3,
  "rows": 5
}
[/block]
You can [check the status of each step](https://basiq.readme.io/v2.1/reference/retrieve-a-job) by querying the job resource (returned when the connection is created).
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the connection to be refreshed."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns a created job resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed.
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/connections/{connection.id}/refresh",
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
      "code": "POST /users/ea3a81/connections/8fce3b/refresh HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 202 Accepted\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61724\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/jobs/61724\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]