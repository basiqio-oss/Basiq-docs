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
Permanently deletes a connection. Once the connection has been deleted, all of the associated financial data e.g. accounts and transactions will no longer be accessible.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the connection to be retrieved."
  },
  "cols": 2,
  "rows": 1
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
      "code": "DELETE /connections/{connection.id}",
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
      "code": "DELETEDELETE  /connections/1/connections/1  HTTPHTTP//1.11.1\n AuthorizationAuthorization::  Bearer YOUR_ACCESS_TOKENBearer YOUR_ACC \n",
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