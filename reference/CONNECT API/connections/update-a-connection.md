---
title: Update a connection
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
Use this to update the details of a specific connection.
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**id**\n*string, required*",
    "2-0": "**password**\n*string, required*",
    "4-0": "**securityCode**\n*string, conditional*",
    "6-0": "**secondaryLoginId**\n*string, conditional*",
    "0-1": "The identifier of the connection to be updated.",
    "2-1": "User's (new or old) institution password.",
    "4-1": "User's institution security code.",
    "6-1": "User's institution secondary login id."
  },
  "cols": 2,
  "rows": 7
}
[/block]
**Returns**

Returns a [job](https://api.basiq.io/v2.1/reference/jobs) object if the request succeeded.

Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1).
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/connections/{connection.id}",
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
      "code": "POST /users/ea3a81/connections/8fce3b HTTP/1.1\nContent-Type: application/json\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n\n{\n  \"password\": \"Pied-Piper\"\n}",
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
      "code": "HTTP/1.1 202 Accepted\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61724\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/jobs/61724\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]