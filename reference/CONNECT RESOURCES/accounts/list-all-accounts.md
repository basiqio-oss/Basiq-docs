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
Use this collection to retrieve a list of [accounts](https://basiq.readme.io/v0.9/reference#accounts). Each entry in the array is a separate account object.

**Returns**

Returns a list with a data property that contains an array of accounts. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors) in the event of a failure.

```json Definition
GET /connections/{connection.id}/accounts
```

```json Example Request
GET /connections/1/accounts HTTP/1.1
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
      "id": "1",
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
      "institution": {
        "type": "institution",
        "id": "AU00000",
        "links": {
          "self": "https://au-api.basiq.io/institutions/AU00000"
        }
      },
      "connection": {
        "type": "connection",
        "id": "1",
        "links": {
          "self": "https://au-api.basiq.io/connections/1"
        }
      },
      "links": {
        "self": "https://au-api.basiq.io/connections/1/accounts/1",
        "transactions": "https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1"
      }
    },
    {
      "type": "account",
      "id": "2",
      "accountNo": "100000-403012830",
      "name": "Personal Savings",
      "currency": "AUD",
      "balance": "167.20",
      "availableFunds": "160.11",
      "lastUpdated": "2017-09-25T16:03:44.111Z",
      "class": {
          "type": "savings",
          "product": "Saver"
      },
      "status": "available",
      "institution": {
        "type": "institution",
        "id": "AU00000",
        "links": {
          "self": "https://au-api.basiq.io/institutions/AU00000"
        }
      },
      "connection": {
        "type": "connection",
        "id": "1",
        "links": {
          "self": "https://au-api.basiq.io/connections/1"
        }
      },
      "links": {
        "self": "https://au-api.basiq.io/connections/1/accounts/2",
        "transactions": "https://au-api.basiq.io/connections/1/transactions?filter[account.id]=2"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/connections/1/accounts"
  }
}
Use this collection to retrieve a list of accounts. Each entry in the array is a separate account object.
```
