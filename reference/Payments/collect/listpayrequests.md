---
title: List payrequests
excerpt: ''
api:
  file: payments.json
  operationId: listPayrequests
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
You can Use the limit to list the required pay requests from the Basiq API. 
[block:code]
{
  "codes": [
    {
      "code": "GET /payments/payrequests HTTP/1.1\nAccept: application/json\nContent-Type: application/json\nAuthorization: Basic $YOUR_ACCESS_TOKEN\n\n{\n  \"type\": \"list\",\n  \"count\": 2,\n  \"size\": 2,\n  \"data\": [\n    {\n      \"type\": \"payrequest\",\n      \"id\": \"b1824ad0-73f1-0138-3700-0a58a9feac09\",\n      \"requestId\": \"01824ad0-73f1-0138-3700-0a58a9feac09\",\n      \"created\": \"2022-03-21T20:28:22.378Z\",\n      \"updated\": \"2022-03-21T20:28:22.378Z\",\n      \"method\": \"batch\",\n      \"status\": \"in-progress\",\n      \"payer\": {\n        \"payerUserId\": \"21824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"payerBankBranchCode\": \"730002\",\n        \"payerAccountNumber\": \"123456789\",\n        \"payerAccountId\": \"31824ad0-73f1-0138-3700-0a58a9feac09\"\n      },\n      \"description\": \"Investment\",\n      \"amount\": 173.45,\n      \"currency\": \"AUD\",\n      \"links\": {\n        \"self\": \"/payments/payrequests/b1824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"job\": \"/jobs/b1824ad0-73f1-0138-3700-0a58a9feac09\"\n      }\n    },\n    {\n      \"type\": \"payrequest\",\n      \"id\": \"c1024ad0-73f1-0138-3700-0a58a9feac09\",\n      \"requestId\": \"a1824ad0-73f1-0138-3700-0a58a9feac09\",\n      \"created\": \"2022-03-21T20:28:22.378Z\",\n      \"updated\": \"2022-03-21T20:28:22.378Z\",\n      \"method\": \"batch\",\n      \"status\": \"in-progress\",\n      \"payer\": {\n        \"payerUserId\": \"21824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"payerBankBranchCode\": \"730002\",\n        \"payerAccountNumber\": \"123456789\",\n        \"payerAccountId\": \"31824ad0-73f1-0138-3700-0a58a9feac09\"\n      },\n      \"description\": \"Investment\",\n      \"amount\": 173.45,\n      \"currency\": \"AUD\",\n      \"links\": {\n        \"self\": \"/payments/payrequests/c1024ad0-73f1-0138-3700-0a58a9feac09\",\n        \"job\": \"/jobs/c1024ad0-73f1-0138-3700-0a58a9feac09\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/payments/payrequests\",\n    \"next\": \"https://au-api.basiq.io/payments/payrequests?next=049fde\"\n  }\n}",
      "language": "json",
      "name": "List payrequests"
    }
  ]
}
[/block]