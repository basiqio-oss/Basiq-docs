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
Use this to retrieve the latest financial data. 


[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the connection to be refreshed."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**
Returns a [connection](https://basiq.readme.io/v0.9/reference#connections) object if the request succeeded. The returned object will have an embedded accounts collection object, as well as links to the latest [account](https://basiq.readme.io/v0.9/reference#accounts) and [transaction](https://basiq.readme.io/v0.9/reference#transactions) data.

Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors).
[block:code]
{
  "codes": [
    {
      "code": "POST /connections/{connection.id}/refresh",
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
      "code": "POST /connections/1/refresh HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"connection\",\n  \"id\": \"1\",\n  \"externalUserId\": \"721832\",\n  \"status\": \"active\",\n  \"lastUsed\": \"2017-09-28T11:15:09.756Z\",\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"accounts\": {\n    \"type\": \"list\",\n    \"data\": [\n      {\n        \"type\": \"account\",\n        \"id\": \"1\",\n        \"accountNo\": \"105148119695\",\n        \"name\": \"Business account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"10.00\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/1/accounts/1\",\n          \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1\"\n        }\n      },\n      {\n        \"type\": \"account\",\n        \"id\": \"2\",\n        \"accountNo\": \"533705985043\",\n        \"name\": \"Choice Account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"-10.09\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/1/accounts/2\",\n          \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=2\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/1\",\n    \"accounts\": \"https://au-api.basiq.io/connections/1/accounts\",\n    \"transactions\": \"https://au-api.basiq.io/connections/1/transactions\"\n  }",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]