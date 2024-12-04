---
title: List all institutions
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
Use this collection to retrieve a list of [institutions](https://basiq.readme.io/v2.0/reference#institutions). Each entry in the array is a separate institution object.
[block:parameters]
{
  "data": {
    "0-1": "This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties:\n\n- `country`\n\n- `tier`\n\n- `serviceType`\n\n- `institutionType`\n\n- `stage`\n\nOnly equals (eq) and not equals (ne) operations are currently supported.",
    "0-0": "**[filter](https://api.basiq.io/docs/collections-filters)**\n*optional*"
  },
  "cols": 2,
  "rows": 1
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /institutions",
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
      "code": "GET /institutions HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.11.1 200 OK\nContent-TypeContent-Type::  application/jsonapplication/json\n\n{\n  \"type\": \"list\",\n  \"totalCount\": 56,\n  \"data\": [\n    {\n      \"type\": \"institution\",\n      \"id\": \"AU00000\",\n      \"name\": \"Hooli Bank\",\n      \"shortName\": \"Hooli\",\n      \"institutionType\": \"Test Bank\",\n      \"country\": \"Australia\",\n      \"serviceName\": \"Personal Online Banking\",\n      \"serviceType\": \"Personal Banking\",\n      \"loginIdCaption\": \"Login\",\n      \"passwordCaption\": \"Password\",\n      \"tier\": \"4\",\n      \"authorization\": \"user\",\n      \"features\": {\n        \"login\":[\n           \"web\"\n         ],\n        \"mfaChallenge\": [],\n        \"accounts\": {\n          \"accountNo\": [\n            \"web\"\n          ],\n          \"name\": [\n            \"web\"\n          ],\n          ...\n        },\n        \"transactions\": {\n          \"status\": [\n            \"web\"\n          ],\n          \"description\": [\n            \"web\"\n          ],\n          ...\n        },\n        \"profile\": {\n          \"fullName\": [\n            \"web\"\n          ],\n          \"firstName\": [\n            \"web\"\n          ],\n          ...\n        }\n      },\n      \"forgottenPasswordUrl\": \"https://hooli.com.au/forgotten...\",\n      \"stage\": \"beta\",\n      \"status\": \"under-maintenance\",\n      \"stats\": {\n        \"averageDurationMs\": {\n          \"verifyCredentials\": 3600,\n          \"retrieveAccounts\": 4500,\n          \"retrieveTransactions\": 2300,\n          \"retrieveMeta\": 1200,\n          \"total\": 11600\n        }\n      },\n      \"logo\": {\n        \"type\": \"image\",\n        \"colors\": null,\n        \"links\": {\n          \"square\": \"https://d388vpyfrt4zrj.cloudfront.net/AU00000.svg\",\n          \"full\": \"https://d388vpyfrt4zrj.cloudfront.net/AU00000-full.svg\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n }",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]