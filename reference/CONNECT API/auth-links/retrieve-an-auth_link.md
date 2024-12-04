---
title: Retrieve an auth_link
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
Use this to retrieve the latest/last auth_link generated for the specified user..
[block:parameters]
{
  "data": {
    "0-0": "*no arguments required*",
    "0-1": "",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 2
}
[/block]
**Returns**

Returns the latest/last auth_link generated for the specified user. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/auth_link",
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
      "code": "GET /users/{user.id}/auth_link HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nAccept: application/json\n",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"auth_link\",\n  \"id\": \"63448be4\",\n  \"userId\": \"ec4ea48d\",\n  \"expiresAt\": \"2019-11-21T04:08:50Z\",\n  \"mobile\": \"+61410000000\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ec4ea48d/auth_link\",\n    \"public\": \"https://connect.basiq.io/63448be4\"\n  }\n}\n\n",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]