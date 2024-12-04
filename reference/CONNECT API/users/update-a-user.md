---
title: Update a user
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
Updates the specified user by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
[block:parameters]
{
  "data": {
    "0-0": "**email**\n*string, optional*",
    "2-0": "**mobile**\n**string, optional**",
    "h-0": "Arguments",
    "0-1": "The end-users email address.",
    "2-1": "The end-users mobile number."
  },
  "cols": 2,
  "rows": 4
}
[/block]
**Returns**
Returns the user object if the update succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if update parameters are invalid (e.g. specifying an email address).
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}",
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
      "code": "POST /users/ea3a81 HTTP/1.1\nContent-Type: application/json\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n\n{\n  \"email\": \"gavin@hooli.xyz\"\n}",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"user\",\n  \"id\": \"ea3a81\",\n  \"email\": \"gavin@hooli.xyz\",\n  \"mobile\": \"+61410888666\",\n  \"firstName\": \"Gavin\",\n  \"lastName\": \"Hooli\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81\",\n    \"connections\": \"https://au-api.basiq.io/users/ea3a81/connections\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]