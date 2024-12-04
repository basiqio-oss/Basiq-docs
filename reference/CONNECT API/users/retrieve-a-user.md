---
title: Retrieve a user
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
Retrieves the details of an existing user. You need only supply the unique user identifier that was returned upon user creation.
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*string, required*",
    "h-0": "Arguments",
    "0-1": "The identifier of the user to be retrieved.",
    "1-0": ""
  },
  "cols": 2,
  "rows": 2
}
[/block]
**Returns**
Returns a user if a valid user ID was provided. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}",
      "language": "http",
      "name": "Defintion"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/ea3a81 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"user\",\n  \"id\": \"ea3a81\",\n  \"email\": \"gavin@hooli.com\",\n  \"mobile\": \"+61410888666\",\n  \"firstName\": \"Joe\",\n  \"lastName\": \"Bloggs\",\n  \"connections\": {\n    \"type\": \"list\",\n    \"count\": 1,\n    \"data\": [\n      {\n        \"type\": \"connection\",\n        \"id\": \"aaaf2c3b\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/connections/aaaf2c3b\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81\",\n    \"connections\": \"https://au-api.basiq.io/users/ea3a81/connections\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]