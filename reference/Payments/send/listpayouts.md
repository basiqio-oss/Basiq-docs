---
title: List payouts
excerpt: ''
api:
  file: payments.json
  operationId: listPayouts
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
You can Use the limit to list the required payouts from the Basiq API. 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"list\",\n  \"count\": 2,\n  \"size\": 2,\n  \"data\": [\n    {\n      \"type\": \"payout\",\n      \"id\": \"b1824ad0-73f1-0138-3700-0a58a9feac09\",\n      \"requestId\": \"01824ad0-73f1-0138-3700-0a58a9feac09\",\n      \"created\": \"2022-03-21T20:28:22.378Z\",\n      \"updated\": \"2022-03-21T20:28:22.378Z\",\n      \"method\": \"batch\",\n      \"status\": \"in-progress\",\n      \"payee\": {\n        \"payeeUserId\": \"21824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"payeeBankBranchCode\": \"730002\",\n        \"payeeAccountNumber\": \"123456789\",\n        \"payeeAccountId\": \"31824ad0-73f1-0138-3700-0a58a9feac09\"\n      },\n      \"description\": \"Dividends\",\n      \"amount\": 173.45,\n      \"currency\": \"AUD\",\n      \"links\": {\n        \"self\": \"/payments/payouts/b1824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"job\": \"/jobs/b1824ad0-73f1-0138-3700-0a58a9feac09\"\n      }\n    },\n    {\n      \"type\": \"payout\",\n      \"id\": \"c1024ad0-73f1-0138-3700-0a58a9feac09\",\n      \"requestId\": \"a1824ad0-73f1-0138-3700-0a58a9feac09\",\n      \"created\": \"2022-03-21T20:28:22.378Z\",\n      \"updated\": \"2022-03-21T20:28:22.378Z\",\n      \"method\": \"batch\",\n      \"status\": \"in-progress\",\n      \"payer\": {\n        \"payeeUserId\": \"21824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"payeeBankBranchCode\": \"730002\",\n        \"payeeAccountNumber\": \"123456789\",\n        \"payeeAccountId\": \"31824ad0-73f1-0138-3700-0a58a9feac09\"\n      },\n      \"description\": \"Dividends\",\n      \"amount\": 200.45,\n      \"currency\": \"AUD\",\n      \"links\": {\n        \"self\": \"/payments/payouts/c1024ad0-73f1-0138-3700-0a58a9feac09\",\n        \"job\": \"/jobs/c1024ad0-73f1-0138-3700-0a58a9feac09\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/payments/payouts\",\n    \"next\": \"https://au-api.basiq.io/payments/payouts?next=049fde\"\n  }\n}",
      "language": "json",
      "name": "Payouts"
    }
  ]
}
[/block]