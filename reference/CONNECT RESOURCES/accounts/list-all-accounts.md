---
title: List all accounts
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Use this collection to retrieve a list of [accounts](https://basiq.readme.io/v1.0/reference#accounts). Each entry in the array is a separate account object.

**Returns**

Returns a list with a data property that contains an array of accounts. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v1.0/reference#errors) in the event of a failure.

```json Definition
GET /users/{user.id}/accounts
```

```json Example Request
GETGET  /users/ea3a81/accounts/users/ea3a81/a  HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "data": [
    {
      "type": "account",
      "id": "s55bf3",
      "accountNo": "600000-157441965",
      "name": "Master Savings",
      "currency": "AUD",
      "balance": "356.50",
      "availableFunds": "420.28",
      "lastUpdated": "2017-09-28T13:39:33.144Z",
      "class": {
        "type": "savings",
        "product": "Saver"
      },
      "status": "available",
      "institution": "AU00000",
      "connection": "8fce3b",
      "links": {
        "self": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf3",
        "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')",
        "connection": "https://au-api.basiq.io/users/ea3a81/connections/8fce3b",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
    {
      "type": "account",
      "id": "s55bf4",
      "accountNo": "600000-157441111",
      "name": "Basiq loan",
      "currency": "AUD",
      "balance": "303000.50",
      "availableFunds": "525.28",
      "lastUpdated": "2017-09-28T13:39:33.144Z",
      "class": {
        "type": "mortgage",
        "product": "Home Loan",
        "meta": {
          "accountNumber": "600000-157441111",
          "availableRedraw": "5098.64",
          "endDate": "12/01/25",
          "fee": "Waived",
          "instalmentAmount": "1768.23",
          "interestRate": "4.8% p.a.",
          "interestType": "Fixed rate",
          "nextInstalmentDate": "22/02/18",
          "offsetAccountNumber": "1098 5678",
          "repaymentFrequency": "Weekly",
          "repaymentType": "Interest only"
        }
      },
      "status": "available",
      "institution": "AU00000",
      "connection": "8fce3b",
      "links": {
        "self": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf4",
        "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf4')",
        "connection": "https://au-api.basiq.io/users/ea3a81/connections/8fce3b",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/accounts"
  }
}
```
