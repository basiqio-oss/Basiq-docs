---
title: Delete a connection
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
Permanently deletes a connection. Once the connection has been deleted, all of the associated financial data e.g. accounts and transactions can still be accessed via the users end-point
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the connection to be deleted."
  },
  "cols": 2,
  "rows": 2
}
[/block]

[block:callout]
{
  "type": "danger",
  "body": "Note that this action cannot be undone."
}
[/block]
**Returns**
Returns an empty body if the delete succeeded. Otherwise, this call returns an error in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "DELETE /users/ea3a81/connections/{connection.id}",
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
      "code": "DELETE /users/ea3a81/connections/8fce3b HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 204 No Content",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]