---
title: List all statements
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Use this collection to retrieve a list of [statements](https://basiq.readme.io/v2.0/reference#statements)


[block:parameters]
{
  "data": {
    "0-0": "**[filter](https://basiq.readme.io/v2.0/reference#filters)**\n*optional*",
    "h-0": "Arguments",
    "0-1": "This list can be [filtered](https://basiq.readme.io/v2.0/reference#filters) by the following properties: `upload` , `download`."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns a list with a data property that contains an array of statements. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/statements",
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
      "code": "GET users/ea3a81/statements HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n    \"type\": \"list\",\n    \"data\": [\n        {\n            \"type\": \"statement\",\n            \"id\": \"1a73e\",\n            \"links\": {\n                \"self\": \"/users/ea3a81/statements/1a73e\",\n                \"account\": \"/users/ea3a81/accounts/e40f6\"\n            }\n        }\n    ],\n    \"links\": {\n        \"self\": \"/users/ea3a81/statements\"\n    }\n}\n",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]