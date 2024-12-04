---
title: List all transactions
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
Use this collection to retrieve a paginated list of [transactions](https://api.basiq.io/reference/transactions). The transactions are returned sorted by account and then posted date descending order - with pending transactions appearing first. Transactions are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.
[block:parameters]
{
  "data": {
    "0-0": "**limit**\n*string, optional*",
    "h-0": "Arguments",
    "0-1": "This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.",
    "2-0": "**[filter](https://api.basiq.io/reference/collections)**\n*string, optional*",
    "2-1": "This list can be [filtered](https://api.basiq.io/reference/collections) by the following properties:\n\n- `account.id`\n\n- `transaction.postDate`\n\n- `transaction.status`\n\n- `institution.id`\n\n- `transaction.direction`\n\n- `transaction.class`"
  },
  "cols": 2,
  "rows": 4
}
[/block]
**Returns**

Returns a paginated list with a data property that contains an array of transactions. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1) in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/transactions",
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
      "code": "GET /users/ea3a81/transactions HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"count\": 1,\n  \"size\": 432,\n  \"data\": [\n    {\n      \"type\": \"transaction\",\n      \"id\": \"fx789e\",\n      \"status\": \"posted\",\n      \"description\": \"FLIGHT CENTRE CO    BRISB    QL\",\n      \"postDate\": \"2017-11-10T21:46:44Z\",\n      \"transactionDate\": \"2017-11-09T00:00:00Z\",\n      \"amount\": \"-139.98\",\n      \"balance\": \"356.50\",\n      \"account\": \"s55bf3\",\n      \"institution\": \"AU00101\",\n      \"connection\": \"8fce3b\",\n      \"direction\": \"debit\",\n      \"class\": \"payment\",\n      \"subClass\": {\n        \"code\": \"722\",\n        \"title\": \"Travel Agency and Tour Arrangement Services\"\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/ea3a81/transactions/fx789e\",\n        \"account\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00101\",\n        \"connection\": null\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/transactions\",\n    \"next\": \"https://au-api.basiq.io/users/ea3a81/transactions?next=049fde\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]