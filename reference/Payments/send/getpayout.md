---
title: Retrieve Payout
excerpt: ''
api:
  file: payments.json
  operationId: getPayout
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
[block:callout]
{
  "type": "info",
  "title": "Note",
  "body": "The `jobId` returned can also be used to retrieve the `payout` directly via the API"
}
[/block]
You can use Use the returned `job.Id` you receive to enquire about the payout progress.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"payout\",\n    \"id\": \"33454ad0-73f1-0138-3700-0a58a9feac09\",\n    \"requestId\": \"01824ad0-73f1-0138-3700-0a58a9feac09\",\n    \"created\": \"2022-11-10T12:01:24Z\",\n    \"updated\": \"2022-11-10T13:00:33Z\",\n    \"method\": \"fast\",\n    \"requestedMethod\": \"fast/batch\",\n    \"status\": \"successful\",\n    \"payer\": {\n        \"payeeUserId\": \"21824ad0-73f1-0138-3700-0a58a9feac09\",\n        \"payeeBankBranchCode\": \"730002\",\n        \"payeeAccountNumber\": \"123456787\",\n        \"payeeAccountId\": \"100f1793-bb73-4c77-a3c8-d8497801191f\"\n    },\n    \"description\": \"Investment profits\",\n    \"amount\": 512.56,\n    \"currency\": \"AUD\",\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/payments/payouts/33454ad0-73f1-0138-3700-0a58a9feac09\",\n        \"job\": \"https://au-api.basiq.io/jobs/33454ad0-73f1-0138-3700-0a58a9feac09\"\n    }\n}",
      "language": "json"
    }
  ]
}
[/block]