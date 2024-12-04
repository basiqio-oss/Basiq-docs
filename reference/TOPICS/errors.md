---
title: Errors
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
The Connect API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, user's credentials are invalid, etc.), and codes in the `5xx` range indicate an error with the Connect API's servers (these are rare).

In addition to returning an appropriate HTTP code the body will also include a JSON formatted error object that provides more details about the specifics of the error. The error object will return the error as an array to indicate multiple errors (where present).
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**correlationId**\n*string, read-only*",
    "1-0": "**code**\n*string, read-only*",
    "2-0": "**title**\n*string, read-only*",
    "3-0": "**detail**\n*string, read-only*",
    "4-0": "**source**\n*object, read-only*",
    "0-1": "a unique identifier for this particular occurrence of the problem.",
    "1-1": "an application-specific [error code](https://basiq.readme.io/v0.9/reference#error-codes), expressed as a string value.",
    "2-1": "a short, human-readable summary of the problem.",
    "3-1": "a human-readable explanation specific to this occurrence of the problem.",
    "4-1": "an object containing references to the source of the error, optionally including any of the following members:\n- `pointer` the location to the object or attribute that the error relates to\n- `parameter` a string indicating which URI query parameter caused the error."
  },
  "cols": 2,
  "rows": 5
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTPHTTP//1.11.1  400400  Bad RequestBad Request\n Content-TypeContent-Type::  application/jsonapplication/json\n\n  {{\n     \"type\"\"type\"::  \"list\"\"list\",,\n     \"correlationId\"\"correlationId\"::  \"bd1183d9-c9d8-11e7-909a-6789bfc80ac5\"\"bd1183d9-c9d8-11e7- ,\n  \"data\": [\n    {\n      \"type\": \"error\",\n      \"code\": \"parameter-not-supplied\",\n      \"title\": \"Required parameter not supplied\",\n      \"detail\": \"Institution ID  parameter is required.\",\n      \"source\": {\n        \"pointer\": \"connection/institution/id\",\n        \"parameter\": \"id\"\n      }\n    }",
      "language": "json",
      "name": "EXAMPLE ERROR OBJECT"
    }
  ],
  "sidebar": true
}
[/block]