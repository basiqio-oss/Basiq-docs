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

**Returns**\
Returns an empty body if the delete succeeded. Otherwise, this call returns an [error](https://basiq.readme.io/v1.0/reference#errors) in the event of a failure.

```json  
DELETE /users/{user.id}
```

```json Example Request
DELETE /users/ea3a81 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 204 No Content
```
