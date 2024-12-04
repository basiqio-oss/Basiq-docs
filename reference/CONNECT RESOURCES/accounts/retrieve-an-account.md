---
title: Retrieve an account
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
Use this to retrieve the details of a specific account. This request will return back an account object with the latest data since the last refresh. If you require the latest account details you will need to call the [connection refresh](https://basiq.readme.io/v0.9/reference#refresh-a-connection) resource.
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the account to be retrieved.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns an account if a valid account ID was provided. Returns an [error](https://basiq.readme.io/v0.9/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /connections/{connection.id}/accounts/{account.id}\n",
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
      "code": "GET /connections/1/accounts/1 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"account\",\n  \"id\": \"1\",\n  \"accountNo\": \"600000-157441965\",\n  \"name\": \"Master Savings\",\n  \"currency\": \"AUD\",\n  \"balance\": \"356.50\",\n  \"availableFunds\": \"420.28\",\n  \"lastUpdated\": \"2017-09-28T13:39:33.144Z\",\n  \"class\": {\n      \"type\": \"savings\",\n      \"product\": \"Saver\"\n  },\n  \"status\": \"available\",\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU0000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"connection\": {\n    \"type\": \"connection\",\n    \"id\": \"1\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/connections/1\"\n    }\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/1/accounts/1\",\n    \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]