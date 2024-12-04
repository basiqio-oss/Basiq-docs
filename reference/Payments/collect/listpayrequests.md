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

```json List payrequests
GET /payments/payrequests HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Basic $YOUR_ACCESS_TOKEN

{
  "type": "list",
  "count": 2,
  "size": 2,
  "data": [
    {
      "type": "payrequest",
      "id": "b1824ad0-73f1-0138-3700-0a58a9feac09",
      "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
      "created": "2022-03-21T20:28:22.378Z",
      "updated": "2022-03-21T20:28:22.378Z",
      "method": "batch",
      "status": "in-progress",
      "payer": {
        "payerUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
        "payerBankBranchCode": "730002",
        "payerAccountNumber": "123456789",
        "payerAccountId": "31824ad0-73f1-0138-3700-0a58a9feac09"
      },
      "description": "Investment",
      "amount": 173.45,
      "currency": "AUD",
      "links": {
        "self": "/payments/payrequests/b1824ad0-73f1-0138-3700-0a58a9feac09",
        "job": "/jobs/b1824ad0-73f1-0138-3700-0a58a9feac09"
      }
    },
    {
      "type": "payrequest",
      "id": "c1024ad0-73f1-0138-3700-0a58a9feac09",
      "requestId": "a1824ad0-73f1-0138-3700-0a58a9feac09",
      "created": "2022-03-21T20:28:22.378Z",
      "updated": "2022-03-21T20:28:22.378Z",
      "method": "batch",
      "status": "in-progress",
      "payer": {
        "payerUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
        "payerBankBranchCode": "730002",
        "payerAccountNumber": "123456789",
        "payerAccountId": "31824ad0-73f1-0138-3700-0a58a9feac09"
      },
      "description": "Investment",
      "amount": 173.45,
      "currency": "AUD",
      "links": {
        "self": "/payments/payrequests/c1024ad0-73f1-0138-3700-0a58a9feac09",
        "job": "/jobs/c1024ad0-73f1-0138-3700-0a58a9feac09"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/payments/payrequests",
    "next": "https://au-api.basiq.io/payments/payrequests?next=049fde"
  }
}
```
