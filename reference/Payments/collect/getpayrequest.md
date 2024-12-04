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
> 📘 Note
>
> The `jobId` returned can also be used to retrieve the `payrequest` directly via the API

You can use Use the returned `job.Id` you receive to enquire about the payment requests progress.

```json Retrieve Payrequest Response
GET /payments/payrequests HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Basic $YOUR_ACCESS_TOKEN

{
  "type": "payrequest",
  "id": "f7824ad0-73f1-0138-3700-0a58a9feac0f",
  "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
  "created": "2022-03-21T20:28:22.378Z",
  "updated": "2022-03-21T20:28:22.378Z",
  "method": "batch",
  "status": "in-progress",
  "payer": {
    "payerUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
    "payerBankBranchCode": "730002",
    "payerAccountNumber": "123456789"
  },
  "description": "Spaceship Investment",
  "amount": 173.45,
  "currency": "AUD",
  "links": {
    "self": "/payments/payrequests/f7824ad0-73f1-0138-3700-0a58a9feac0f",
    "job": "/jobs/f7824ad0-73f1-0138-3700-0a58a9feac0f"
  }
}
```
