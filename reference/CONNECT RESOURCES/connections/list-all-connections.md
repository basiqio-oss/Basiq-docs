---
title: List all connections
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
Use this collection to retrieve a list of [connections](https://basiq.readme.io/v1.0/reference#connections).
[block:parameters]
{
  "data": {
    "0-0": "**[filter](https://basiq.readme.io/v1.0/reference#filters)**\n*optional*",
    "0-1": "This list can be [filtered](https://basiq.readme.io/v1.0/reference#filters) by the following properties: `id` , `status` , `institution.id`.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns a list with a data property that contains an array of connections. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/connectionsGET /users",
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
      "code": "GET users/ea3a81/connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"data\": [\n    {\n      \"type\": \"connection\",\n      \"id\": \"8fce3b\",\n      \"status\": \"active\",\n      \"lastUsed\": \"2017-09-28T11:15:09Z\",\n      \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00000\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/connections/8fce3b\",\n        \"accounts\": \"https://au-api.basiq.io/users/ea3a81/accounts?filter=connection.id.eq('8fce3b')\",\n        \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=connection.id.eq('8fce3b')\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"/users/ea3a81/connections\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]