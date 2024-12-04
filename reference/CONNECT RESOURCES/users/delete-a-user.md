---
title: Delete a user
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
Permanently deletes a user along with all of their associated connection details. You need only supply the unique user identifier that was returned upon user creation.

**Returns**
Returns an empty body if the delete succeeded. Otherwise, this call returns an [error](https://basiq.readme.io/v1.0/reference#errors) in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "DELETE /users/{user.id}",
      "language": "json",
      "name": " "
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "DELETE /users/ea3a81 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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