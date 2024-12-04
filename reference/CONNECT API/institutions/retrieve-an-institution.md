---
title: Retrieve an institution
excerpt: ''
deprecated: true
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
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

Returns an institution if a valid ID was provided. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n      \"type\": \"institution\",\n      \"id\": \"AU00000\",\n      \"name\": \"Hooli Bank\",\n      \"shortName\": \"Hooli\",\n      \"institutionType\": \"Test Bank\",\n      \"country\": \"Australia\",\n      \"serviceName\": \"Personal Online Banking\",\n      \"serviceType\": \"Personal Banking\",\n      \"loginIdCaption\": \"Login\",\n      \"passwordCaption\": \"Password\",\n      \"tier\": \"4\",\n      \"authorization\": \"user\",\n      \"features\": {\n        \"login\":[\n           \"web\"\n         ],\n        \"mfaChallenge\": [],\n        \"accounts\": {\n          \"accountNo\": [\n            \"web\"\n          ],\n          \"name\": [\n            \"web\"\n          ],\n          ...\n        },\n        \"transactions\": {\n          \"status\": [\n            \"web\"\n          ],\n          \"description\": [\n            \"web\"\n          ],\n          ...\n        },\n        \"profile\": {\n          \"fullName\": [\n            \"web\"\n          ],\n          \"firstName\": [\n            \"web\"\n          ],\n          ...\n        }\n      },\n      \"forgottenPasswordUrl\": \"https://hooli.com.au/forgotten...\",\n      \"stage\": \"beta\",\n      \"status\": \"under-maintenance\",\n      \"stats\": {\n        \"averageDurationMs\": {\n          \"verifyCredentials\": 3600,\n          \"retrieveAccounts\": 4500,\n          \"retrieveTransactions\": 2300,\n          \"retrieveMeta\": 1200,\n          \"total\": 11600\n        }\n      },\n      \"logo\": {\n        \"type\": \"image\",\n        \"colors\": null,\n        \"links\": {\n          \"square\": \"https://d388vpyfrt4zrj.cloudfront.net/AU00000.svg\",\n          \"full\": \"https://d388vpyfrt4zrj.cloudfront.net/AU00000-full.svg\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n }",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]