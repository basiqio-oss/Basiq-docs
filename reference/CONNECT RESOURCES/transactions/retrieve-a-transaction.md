---
title: Retrieve a transaction
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
Retrieves the details of an existing transaction. You need only supply the unique transaction identifier.
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the transaction to be retrieved."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns a transaction if a valid transaction ID was provided. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/transactions/{transaction.id}\n",
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
      "code": "GET /users/ea3a81/transactions/fx789e HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP//1.11.1 200 OK\n Content-TypeContent-Type::  application/jsonapplication/json\n\n{\n  \"type\": \"transaction\",\n  \"id\": \"fx789e\",\n  \"status\": \"posted\",\n  \"description\": \"FLIGHT CENTRE CO    BRISB    QL\",\n  \"postDate\": \"2016-01-01\",\n  \"transactionDate\": \"\",\n  \"amount\": \"-139.98\",\n  \"balance\": \"356.50\",\n  \"bankCategory\": \"\",\n  \"account\": \"s55bf3\",\n  \"institution\": \"AU00101\",\n  \"connection\": \"8fce3b\",\n  \"direction\": \"debit\",\n  \"class\": \"payment\",\n  \"subClass\": {\n    \"code\": \"722\",\n    \"title\": \"Travel Agency and Tour Arrangement Services\"\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/transactions/fx789e\",\n    \"account\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00101\",\n    \"connection\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\"\n  }\n}\n",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]