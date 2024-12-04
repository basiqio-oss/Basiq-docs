---
title: List all accounts
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
Use this collection to retrieve a list of [accounts](https://basiq.readme.io/v0.9/reference#accounts). Each entry in the array is a separate account object.



**Returns**

Returns a list with a data property that contains an array of accounts. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors) in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /connections/{connection.id}/accounts",
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
      "code": "GET /connections/1/accounts HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"data\": [\n    {\n      \"type\": \"account\",\n      \"id\": \"1\",\n      \"accountNo\": \"600000-157441965\",\n      \"name\": \"Master Savings\",\n      \"currency\": \"AUD\",\n      \"balance\": \"356.50\",\n      \"availableFunds\": \"420.28\",\n      \"lastUpdated\": \"2017-09-28T13:39:33.144Z\",\n      \"class\": {\n          \"type\": \"savings\",\n          \"product\": \"Saver\"\n      },\n      \"status\": \"available\",\n      \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00000\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n        }\n      },\n      \"connection\": {\n        \"type\": \"connection\",\n        \"id\": \"1\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/1\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/connections/1/accounts/1\",\n        \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1\"\n      }\n    },\n    {\n      \"type\": \"account\",\n      \"id\": \"2\",\n      \"accountNo\": \"100000-403012830\",\n      \"name\": \"Personal Savings\",\n      \"currency\": \"AUD\",\n      \"balance\": \"167.20\",\n      \"availableFunds\": \"160.11\",\n      \"lastUpdated\": \"2017-09-25T16:03:44.111Z\",\n      \"class\": {\n          \"type\": \"savings\",\n          \"product\": \"Saver\"\n      },\n      \"status\": \"available\",\n      \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00000\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n        }\n      },\n      \"connection\": {\n        \"type\": \"connection\",\n        \"id\": \"1\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/1\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/connections/1/accounts/2\",\n        \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=2\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/1/accounts\"\n  }\n}\nUse this collection to retrieve a list of accounts. Each entry in the array is a separate account object.",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]