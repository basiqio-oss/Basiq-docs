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
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/connections/refresh",
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
      "code": "POST /users/ea3a81/connections/refresh/  HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 202 Accepted\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"data\": [\n    {\n      \"type\": \"job\",\n      \"id\": \"61725\",\n      \"self\": \"https://au-api.basiq.io/jobs/61725\"\n    },\n    {\n      \"type\": \"job\",\n      \"id\": \"61726\",\n      \"self\": \"https://au-api.basiq.io/jobs/61726\"\n    }\n  ]\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]