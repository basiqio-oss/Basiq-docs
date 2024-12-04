---
title: Retrieve Float account
excerpt: ''
api:
  file: payments.json
  operationId: getFloatAccount
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Retrieve a float account using float account id, the `id`.

```json
{
    "type": "floataccount",
    "id": "786ffcce-a112-43d8-8bad-b38393fe0a9f",
    "bankBranchCode": "802919",
    "accountNumber": "1111111",
    "availableBalance": 14733.15,
    "status": "active",
    "links": {
        "self": "https://au-api.basiq.io/payments/float-accounts/786ffcce-a112-43d8-8bad-b38393fe0a9f"
    }
}
```
