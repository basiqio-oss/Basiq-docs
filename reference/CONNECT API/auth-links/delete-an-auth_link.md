---
title: Delete an auth_link
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
Permanently deletes an auth_link resource. Once deleted the URL associated with the deleted object will no longer be valid.  
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "*no arguments required*",
    "0-1": ""
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

[block:callout]
{
  "type": "info",
  "body": "The auth_link is a URL that directs a User to Basiq's hosted consent workflow to link banks and securely share data. When the user selects 'I have disclosed all my accounts' the auth_link is automatically deleted."
}
[/block]
**Returns**
Returns an empty body if the delete succeeded. Otherwise, this call returns an error in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "DELETE /users/ea3a81/auth_link",
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
      "code": "DELETE /users/ea3a81/auth_link HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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