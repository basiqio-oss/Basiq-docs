---
title: Refresh all connections
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
Use this to refresh of all connections. Check how to [refresh a connection](https://basiq.readme.io/v2.1/reference/refresh-a-connection) for more details.

**Returns**

Returns a list of URLs of the created jobs. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed.

```json Definition
POST /users/{user.id}/connections/refresh
```

```json Example Request
POST /users/ea3a81/connections/refresh/  HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "type": "list",
  "data": [
    {
      "type": "job",
      "id": "61725",
      "self": "https://au-api.basiq.io/jobs/61725"
    },
    {
      "type": "job",
      "id": "61726",
      "self": "https://au-api.basiq.io/jobs/61726"
    }
  ]
}
```
