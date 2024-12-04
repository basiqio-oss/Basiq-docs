---
title: Retrieve an affordability summary
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
Retrieves the details of an affordability summary. You need only supply the unique transaction identifier.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Arguments
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **id**
        *required*
      </td>

      <td style={{ textAlign: "left" }}>
        A string that uniquely identifies the affordability summary as a resource
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

> 🚧 You will need an affordability id from an object you have created to retrieve an affordability object.

**Returns**

Returns a created affordability resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

> 📘 PDF Response also available
>
> The affordability API returns a JSON response by default however you can specify to return a PDF report version of the affordability summary (examples below)

```json Definition
GET /users/{user.id}/affordability/{afforability.id} HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/json
```

```json
GET /users/25c8d1ed77/affordability/s55bf3 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/json
```

```json Example Reponse
HTTP/1.11.1 200 OK
Content-Type: application/json

{
  "type": "affordability",
  "id": "s55bf3",
  "fromMonth": "2019-03",
  "toMonth": "2020-03",
  "coverageDays": 392,
  "generatedDate": "2020-03-26T06:56:44",
  "summary": {
    "assets": "59983.11",
    "liabilities": "-323946.20",
    "netPosition": "-263963.09",
    "creditLimit": "20000.00",
    "expenses": "-12046.00",
    "savings": "93.00",
    "regularIncome": {
      "previous3Months": {
        "avgMonthly": "18098.00"
      }
    }
  },
  "assets": [
    {
      "currency": "AUD",
      "balance": "35298.67",
      "availableFunds": "35298.67",
      "institution": "Hooli",
      "type": "account",
      "account": {
        "product": "Hooli Saver",
        "type": "savings"
      },
      "previous6Months": {
        "minBalance": "32427.79",
        "maxBalance": "34798.67"
      }
    },
    {
      "currency": "AUD",
      "balance": "24684.44",
      "availableFunds": "24684.44",
      "institution": "Hooli",
      "type": "account",
      "account": {
        "product": "Hooli Transaction",
        "type": "transaction"
      },
      "previous6Months": {
        "minBalance": "10032.81",
        "maxBalance": "38309.44"
      }
    }
  ],
  "liabilities": {
    "loan": [
      {
        "currency": "AUD",
        "balance": "-312233.00",
        "availableFunds": "87767.00",
        "institution": "Hooli",
        "account": {
          "type": "mortgage",
          "product": "Hooli Home Loan"
        },
        "previousMonth": {
          "totalCredits": "5768.00",
          "totalDebits": "-4303.50",
          "totalInterestCharged": "-4303.50",
          "totalRepayments": "5768.00"
        },
        "changeHistory": [
          {
            "direction": "debit",
            "amount": "-4220.75",
            "date": "2019-03-19",
            "source": "Mortgage Interest Payment 746833"
          },
          {
            "direction": "credit",
            "amount": "5768.00",
            "date": "2019-03-31",
            "source": "Transfer Platnm Homeloan 346454"
          },
          {
            "direction": "debit",
            "amount": "-4228.50",
            "date": "2019-04-19",
            "source": "Mortgage Interest Payment 746833"
          }
        ],
        "previous6Months": {
          "arrears": false
        }
      }
    ],
    "credit": [
      {
        "currency": "AUD",
        "balance": "-11713.20",
        "availableFunds": "8286.80",
        "institution": "Hooli",
        "creditLimit": "20000.00",
        "account": {
          "type": "credit-card",
          "product": "Hooli Visa"
        },
        "previousMonth": {
          "totalCredits": "0.00",
          "totalDebits": "-8287.10",
          "minBalance": "-3174.16",
          "maxBalance": "-12329.16"
        },
        "previous6Months": {
          "cashAdvances": "-2053.50"
        }
      }
    ]
  },
  "external": [
    {
      "source": "afterpay",
      "payments": {
        "first": "2019-11-15",
        "last": "2019-11-15",
        "noOccurrences": 2,
        "amountAvg": "-146.50",
        "amountAvgMonthly": "-12.00",
        "total": "-146.50"
      },
      "changeHistory": [
        {
          "amount": "-146.50",
          "date": "2019-11-15",
          "source": "AFTERPAY MELBOURNE VI AUS Card xx3854 Value Date: 10/11/2019"
        },
        {
          ...
        }
      ]
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/25c8d1ed77/affordability/s55bf3",
    "income": "https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4",
    "expenses": "https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5",
    "accounts": [
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08",
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430",
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089",
      "https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056"
    ]
  }
}
```
