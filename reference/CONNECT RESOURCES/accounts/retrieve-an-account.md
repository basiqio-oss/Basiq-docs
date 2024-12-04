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
Use this to retrieve the details of a specific account. This request will return back an account object with the latest data since the last refresh. If you require the latest account details you will need to call the [connection refresh](https://basiq.readme.io/v1.0/reference#refresh-a-connection) resource.
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

Returns an account if a valid account ID was provided. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/accounts/{account.id}\n",
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
      "code": "GET /users/ea3a81/accounts/s55bf3 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n",
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
      "code": "HTTP/1.11.1 200 OK\n Content-TypeContent-Type::  application/jsonapplication/json\n\n{\n  \"type\": \"account\",\n  \"id\": \"s55bf3\",\n  \"accountNo\": \"600000-157441965\",\n  \"name\": \"Master Savings\",\n  \"currency\": \"AUD\",\n  \"balance\": \"356.50\",\n  \"availableFunds\": \"420.28\",\n  \"lastUpdated\": \"2017-09-28T13:39:33.144Z\",\n  \"class\": {\n      \"type\": \"savings\",\n      \"product\": \"Saver\"\n  },\n  \"status\": \"available\",\n  \"institution\": \"AU00000\",\n  \"connection\": \"8fce3b\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')\",\n    \"connection\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]