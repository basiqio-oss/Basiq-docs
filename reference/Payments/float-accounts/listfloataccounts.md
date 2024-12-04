---
title: List float accounts
excerpt: ''
api:
  file: payments.json
  operationId: listFloatAccounts
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
When list float accounts, you will receive a below response. 

```json
{
    "type": "list",
    "count": 1,
    "data": [
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
    ],
    "links": {
        "self": "https://au-api.basiq.io/payments/float-accounts"
    }
}
```
