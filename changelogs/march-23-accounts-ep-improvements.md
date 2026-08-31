---
title: March '23 - Accounts EP Improvements
author: Ashman Malik
hidden: false
published_at: '2023-03-02T01:56:54.418Z'
type: improved
---
# Improvements :heart_decoration:

The Accounts endpoint has been extended to include Credit Limit information for applicable accounts.

Users can now retrieve their credit limit for eligible accounts using the Accounts endpoint.

The eligible account types are **credit-card**, **loan** and **mortgage**.

The update is below from our [testing personas](https://api.basiq.io/reference/testing). 

```json
{
  "type": "list",
  "data": [
    {
      "type": "account",
      "id": "s55bf3",
      "accountHolder": "GAVIN BELSON",
      "accountNo": "600000-157441965",
      "availableFunds": "420.28",
      "balance": "356.50",
      "creditLimit": "400000.00",
      "class": {
        "type": "mortgage",
        "product": "Hooli Home Loan"
      },
      "connection": "8fce3b",
      "currency": "AUD",
      "institution": "AU00000",
      "lastUpdated": "2019-09-28T13:39:33Z",
      "name": "Master Savings",
      "status": "available",
      "transactionIntervals": [
        {
          "from": "2018-07-01",
          "to": "2018-12-30"
        }
      ],
      "links": {
        "institution": "https://au-api.basiq.io/institutions/AU00000",
        "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')",
        "self": "https://au-api.basiq.io/users/cd6fbd92/accounts/319ae910"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/cd6fbd92/accounts/319ae910"
  }
}
```

For further info, please check out our docs [here](https://api.basiq.io/reference/getaccounts).