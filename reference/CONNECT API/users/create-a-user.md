---
title: Create a user
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
Use this to create a new user object. 
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**email**\n*string, conditional*",
    "2-0": "**mobile**\n*string, conditional*",
    "0-1": "The end-users email address. **Mandatory if mobile is not supplied.**",
    "2-1": "The end-users mobile number, supplied in international format \n`+[country-code][mobileno] e.g. +61410888999` . **Mandatory if email is not supplied**",
    "4-0": "**firstName**\n*string, optional*",
    "6-0": "**lastName**\n*string, optional*",
    "4-1": "The end-users first name as an optional additional parameter",
    "6-1": "The end-users last name as an optional additional parameter"
  },
  "cols": 2,
  "rows": 7
}
[/block]
**Returns**
Returns the user object if the request succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if update parameters are invalid (e.g. supplying an empty email address).
[block:code]
{
  "codes": [
    {
      "code": "POST /users",
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
      "code": "POST /users HTTP/1.1\nContent-Type: application/json\nAuthorization: Bearer YOUR_ACCESS_TOKEN\n\n{\n  \"email\": \"gavin@hooli.com\",\n  \"mobile\": \"+61410888666\",\n  \"firstName\": \"Joe\",\n  \"lastName\": \"Bloggs\"\n}",
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
      "code": "HTTP/1.1 201 Created\nContent-Type: application/json\n\n{\n  \"type\": \"user\",\n  \"id\": \"ea3a81\",\n  \"email\": \"gavin@hooli.com\",\n  \"mobile\": \"+61410888666\",\n  \"firstName\": \"Joe\",\n  \"lastName\": \"Bloggs\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]