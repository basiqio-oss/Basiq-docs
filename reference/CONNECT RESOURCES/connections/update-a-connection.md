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
Use this to update an existing [connection](https://basiq.readme.io/v0.9/reference#connections).

If the server has successfully acquired the financial records, connection's `status` will be set to `active`. Otherwise, if the server was unable to acquire the data using the supplied connection details, the status will be se to `invalid`.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**id**\n*string, required*",
    "1-0": "**password**\n*string, required*",
    "2-0": "**securityCode**\n*string, conditional*",
    "3-0": "**externalUserId**\n*string, conditional*",
    "0-1": "The identifier of the connection to be updated.",
    "1-1": "User's (new or old) institution password.",
    "2-1": "User's institution security code.",
    "3-1": "A identifier that uniqely identifies a user within your application."
  },
  "cols": 2,
  "rows": 4
}
[/block]
**Returns**
Returns a [connection](https://basiq.readme.io/v0.9/reference#connections) object if the request succeeded. The returned object will have links to the acquired [account](https://basiq.readme.io/v0.9/reference#accounts) and [transaction](https://basiq.readme.io/v0.9/reference#transactions) data.

Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors).
[block:code]
{
  "codes": [
    {
      "code": "POST /connections/{connection.id}",
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
      "code": "PUT /connections/1 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n{\n  \"password\": \"Pied-Piper\",\n  \"externalUserId\": \"1\"\n}",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"connection\",\n  \"id\": \"1\",\n  \"externalUserId\": \"1\",\n  \"status\": \"active\",\n  \"lastUsed\": \"2017-09-28T11:15:09.756Z\",\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/1\",\n    \"accounts\": \"https://au-api.basiq.io/connections/1/accounts\",\n    \"transactions\": \"https://au-api.basiq.io/connections/1/transactions\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]