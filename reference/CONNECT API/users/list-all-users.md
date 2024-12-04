---
title: List all users
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
Use this collection to retrieve a list of [Users](ref:users)
[block:parameters]
{
  "data": {
    "0-0": "**[filter](https://api.basiq.io/docs/collections-filters)**\n*optional*",
    "0-1": "This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties: *coming soon*",
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
      "code": "GET /users",
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
      "code": "GET users HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"size\": 431,\n  \"data\": [\n    {\n      \"type\": \"user\",\n      \"id\": \"9ac25c19\",\n      \"email\": \"bertram@anton.com\",\n      \"mobile\": \"\",\n      \"createdTime\": \"2021-05-25T06:29:44Z\",\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/9ac25c19\"\n      }\n    },\n    {\n      \"type\": \"user\",\n      \"id\": \"63e0025d5\",\n      \"firstName\": \"Dinesh\",\n      \"lastName\": \"Chugtai\",\n      \"email\": \"dinesh@piperchat.io\",\n      \"mobile\": \"+61555444776\",\n      \"createdTime\": \"2021-01-19T01:42:30Z\",\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/63e0025d5\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users\"\n  }\n}\n",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]