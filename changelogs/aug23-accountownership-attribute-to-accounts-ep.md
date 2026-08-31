---
title: Aug'23 - accountOwnership attribute to Accounts EP
author: Ashman Malik
hidden: false
published_at: '2023-08-15T00:06:24.098Z'
type: added
---
## Improvements :heart_decoration:

**accountOwnership**

A value indicating the number of customers that have ownership of the account, according to the data holder's definition of account ownership. Does not indicate that all account owners are eligible consumers.

The enum options for accountOwnership are:

* `UNKNOWN`
* `ONE_PARTY`
* `TWO_PARTY`
* `MANY_PARTY`
* `OTHER`

For more info, please read our docs [here](https://api.basiq.io/reference/accounts). 

```json accountOwnership
{
  "type": "list",
  "data": [
    {
      "type": "account",
      "id": "s55bf3",
      "accountHolder": "GAVIN BELSON",
      "accountOwnership": "ONE_PARTY",
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
      "meta": {
        "fees": [
          {
            "name": "Dishonour fee",
            "feeType": "EVENT",
            "amount": "10.00",
            "accrualFrequency": "P1M"
          }
        ],
        "depositRates": [
          {
            "depositRateType": "VARIABLE",
            "rate": "0.0385",
            "applicationFrequency": "P1M"
          }
        ],
        "lendingRates": [
          {
            "lendingRateType": "PURCHASE",
            "rate": "0.2024",
            "applicationFrequency": "P1M"
          }
        ],
        "loan": {
          "startDate": "2019-10-01",
          "endDate": "2045-10-01",
          "repaymentType": "PRINCIPAL_AND_INTEREST",
          "minInstalmentAmount": "5500"
        },
        "creditCard": {
          "minPaymentAmount": "117.00",
          "paymentDueAmount": "5847.00",
          "paymentCurrency": "AUD",
          "paymentDueDate": "2023-12-12"
        }
      },
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