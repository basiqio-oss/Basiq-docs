---
title: Retrieve Payrequest
excerpt: ''
api:
  file: payments.json
  operationId: getPayrequest
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
  "body": "The `jobId` returned can also be used to retrieve the `payrequest` directly via the API",
  "title": "Note"
}
[/block]
You can use Use the returned `job.Id` you receive to enquire about the payment requests progress.
[block:code]
{
  "codes": [
    {
      "code": "GET /payments/payrequests HTTP/1.1\nAccept: application/json\nContent-Type: application/json\nAuthorization: Basic $YOUR_ACCESS_TOKEN\n\n{\n  \"type\": \"payrequest\",\n  \"id\": \"f7824ad0-73f1-0138-3700-0a58a9feac0f\",\n  \"requestId\": \"01824ad0-73f1-0138-3700-0a58a9feac09\",\n  \"created\": \"2022-03-21T20:28:22.378Z\",\n  \"updated\": \"2022-03-21T20:28:22.378Z\",\n  \"method\": \"batch\",\n  \"status\": \"in-progress\",\n  \"payer\": {\n    \"payerUserId\": \"21824ad0-73f1-0138-3700-0a58a9feac09\",\n    \"payerBankBranchCode\": \"730002\",\n    \"payerAccountNumber\": \"123456789\"\n  },\n  \"description\": \"Spaceship Investment\",\n  \"amount\": 173.45,\n  \"currency\": \"AUD\",\n  \"links\": {\n    \"self\": \"/payments/payrequests/f7824ad0-73f1-0138-3700-0a58a9feac0f\",\n    \"job\": \"/jobs/f7824ad0-73f1-0138-3700-0a58a9feac0f\"\n  }\n}",
      "language": "json",
      "name": "Retrieve Payrequest Response"
    }
  ]
}
[/block]