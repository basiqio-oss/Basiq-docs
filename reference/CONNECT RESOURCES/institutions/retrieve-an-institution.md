---
title: Retrieve an institution
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
Retrieves the details of an existing institution. You need only supply the institutions unique identifier.
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*string, required*",
    "0-1": "The identifier of the institution to be retrieved.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns an institution if a valid ID was provided. Returns an [error](https://basiq.readme.io/v0.9/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /institutions/{institution.id}",
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
      "code": "GET /institutions/AU00000 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"institution\",\n  \"id\": \"AU00000\",\n  \"name\": \"Basiq Test Bank\",\n  \"shortName\": \"Basiq Test Bank\",\n  \"institutionType\": \"Test Bank\",\n  \"country\": \"Australia\",\n  \"serviceName\": \"Personal Online Banking\",\n  \"serviceType\": \"Test\",\n  \"loginIdCaption\": \"Login\",\n  \"passwordCaption\": \"Password\",\n  \"logo\": {\n    \"type\": \"image\",\n    \"links\": {\n      \"self\": \"https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000.png\"\n    }\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]