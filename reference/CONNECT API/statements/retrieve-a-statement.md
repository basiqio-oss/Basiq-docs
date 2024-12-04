---
title: Retrieve a statement
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
Use this to download a specific bank statement. This request will return back a pdf file to save locally.
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*required*",
    "0-1": "The identifier of the statement to be retrieved.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 2
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "",
  "body": "Specify attribute application/pdf or application/json in the Accept header of your request."
}
[/block]
**Returns**

Returns pdf bank statement if a valid statement ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/statements/{statement.id}",
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
      "code": "GET /users/ea3a81/statements/1a73e HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nAccept: application/pdf\n",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/pdf\n\n",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]