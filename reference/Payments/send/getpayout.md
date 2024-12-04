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
> 📘 Note
>
> The `jobId` returned can also be used to retrieve the `payout` directly via the API

You can use Use the returned `job.Id` you receive to enquire about the payout progress.

```json
{
    "type": "payout",
    "id": "33454ad0-73f1-0138-3700-0a58a9feac09",
    "requestId": "01824ad0-73f1-0138-3700-0a58a9feac09",
    "created": "2022-11-10T12:01:24Z",
    "updated": "2022-11-10T13:00:33Z",
    "method": "fast",
    "requestedMethod": "fast/batch",
    "status": "successful",
    "payer": {
        "payeeUserId": "21824ad0-73f1-0138-3700-0a58a9feac09",
        "payeeBankBranchCode": "730002",
        "payeeAccountNumber": "123456787",
        "payeeAccountId": "100f1793-bb73-4c77-a3c8-d8497801191f"
    },
    "description": "Investment profits",
    "amount": 512.56,
    "currency": "AUD",
    "links": {
        "self": "https://au-api.basiq.io/payments/payouts/33454ad0-73f1-0138-3700-0a58a9feac09",
        "job": "https://au-api.basiq.io/jobs/33454ad0-73f1-0138-3700-0a58a9feac09"
    }
}
```
