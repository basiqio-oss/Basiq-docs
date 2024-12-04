---
title: Retrieve a connection
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
Use this to retrieve details of a specific connection. This request will return back a connection object with most of the fields that were submitted when the connection was first created. The connection object will also return a list of URLs to the associated account, transaction and institution objects.

The status property of the connection object identifies the state of the connection. Use this to work out if the connection is still valid, or whether to take further action (e.g. if the connection credentials are no longer valid you may ask the user to re-submit their details).
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*required*",
    "0-1": "The identifier of the connection to be retrieved.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 1
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Note that due to security the loginId, password, securityCode are never returned."
}
[/block]
**Returns**

Returns a connection if a valid connection ID was provided. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /user/{user.id}/connections/{connection.id}",
      "language": "json"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/ea3a81/connections/8fce3b HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"connection\",\n  \"id\": \"8fce3b\",\n  \"status\": \"active\",\n  \"lastUsed\": \"2017-09-28T11:15:09Z\",\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"accounts\": {\n    \"type\": \"list\",\n    \"data\": [\n      {\n        \"type\": \"account\",\n        \"id\": \"s55bf3\",\n        \"accountNo\": \"105148119695\",\n        \"name\": \"Business account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"10.00\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')\"\n        }\n      },\n      {\n        \"type\": \"account\",\n        \"id\": \"ar36y2\",\n        \"accountNo\": \"533705985043\",\n        \"name\": \"Choice Account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"-10.09\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/ar36y2\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('ar36y2')\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n    \"accounts\": \"https://au-api.basiq.io/users/ea3a81/accounts?filter=connection.id.eq('8fce3b')\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=connection.id.eq('8fce3b')\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]