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

```json Payouts
{
  "type": "list",
  "count": 2,
  "size": 2,
  "data": [
    {
      "type": "payout",
      "id": "b1824ad0-73f1-0138-3700-0a58a9feac09",
      "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
      "created": "2022-03-21T20:28:22.378Z",
      "updated": "2022-03-21T20:28:22.378Z",
      "method": "batch",
      "status": "in-progress",
      "payee": {
        "payeeUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
        "payeeBankBranchCode": "730002",
        "payeeAccountNumber": "123456789",
        "payeeAccountId": "31824ad0-73f1-0138-3700-0a58a9feac09"
      },
      "description": "Dividends",
      "amount": 173.45,
      "currency": "AUD",
      "links": {
        "self": "/payments/payouts/b1824ad0-73f1-0138-3700-0a58a9feac09",
        "job": "/jobs/b1824ad0-73f1-0138-3700-0a58a9feac09"
      }
    },
    {
      "type": "payout",
      "id": "c1024ad0-73f1-0138-3700-0a58a9feac09",
      "requestId": "a1824ad0-73f1-0138-3700-0a58a9feac09",
      "created": "2022-03-21T20:28:22.378Z",
      "updated": "2022-03-21T20:28:22.378Z",
      "method": "batch",
      "status": "in-progress",
      "payer": {
        "payeeUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
        "payeeBankBranchCode": "730002",
        "payeeAccountNumber": "123456789",
        "payeeAccountId": "31824ad0-73f1-0138-3700-0a58a9feac09"
      },
      "description": "Dividends",
      "amount": 200.45,
      "currency": "AUD",
      "links": {
        "self": "/payments/payouts/c1024ad0-73f1-0138-3700-0a58a9feac09",
        "job": "/jobs/c1024ad0-73f1-0138-3700-0a58a9feac09"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/payments/payouts",
    "next": "https://au-api.basiq.io/payments/payouts?next=049fde"
  }
}
```
