---
title: List all affordability summaries
excerpt: List all affordability snapshots generated for this user
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Use this collection to retrieve a list of [Affordability](https://api.basiq.io/reference/affordability) resources generated.  The list provides a short form on the affordability resource responses with a link to the full response.  The collection is ordered by generated date in descending order.

**Returns**

Returns a list with a data property that contains an array of affordability resources. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/affordability",
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
      "code": "GET users/ea3a81/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n{\n    \"type\": \"list\",\n    \"data\": [\n        {\n            \"type\": \"affordability\",\n            \"id\": \"b35f967b\",\n            \"fromMonth\": \"2019-10\",\n            \"toMonth\": \"2020-10\",\n            \"coverageDays\": 393,\n            \"generatedDate\": \"2021-02-17T09:12:25\",\n            \"institutions\": [\n                \"AU00000\"\n            ],\n            \"links\": {\n                \"self\": \"https://au-api.basiq.io/users/e9a95456/affordability/b35f967b\",\n                \"income\": \"https://au-api.basiq.io/users/e9a95456/income/b35f967b\",\n                \"expenses\": \"au-api.basiq.io/users/e9a95456/expenses/b35f967b\"\n            }\n        }\n    ],\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/e9a95456/affordability\"\n    }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]