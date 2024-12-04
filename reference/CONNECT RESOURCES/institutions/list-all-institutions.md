---
title: List all institutions
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
Use this collection to retrieve a list of [institutions](https://basiq.readme.io/v0.9/reference#institutions). Each entry in the array is a separate institution object.
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
      "code": "HTTPHTTP//1.11.1  200200  OKOK\n Content-TypeContent-Type::  application/jsonapplication/json\n\n{\n  \"type\": \"list\",\n  \"size\": 89,\n  \"data\": [\n    {\n      \"type\": \"institution\",\n      \"id\": \"AU00000\",\n      \"name\": \"Basiq Test Bank\",\n      \"shortName\": \"Basiq Test Bank\",\n      \"institutionType\": \"Test Bank\",\n      \"country\": \"Australia\",\n      \"serviceName\": \"Personal Online Banking\",\n      \"serviceType\": \"Test\",\n      \"loginIdCaption\": \"Login\",\n      \"passwordCaption\": \"Password\",\n      \"logo\": {\n        \"type\": \"image\",\n        \"links\": {\n          \"self\": \"https://s3-ap-southeast-2.amazonaws.com/basiq-institutions/AU00000.png\"\n        }\n      },\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n    null\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/institutions\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]