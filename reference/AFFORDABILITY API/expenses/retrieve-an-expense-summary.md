---
title: Retrieve an expense summary
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

> 🚧 You will need an expenses id from an object you have created to retrieve an expenses object.

**Returns**

Returns a created expenses resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Definition
GET /users/{user.id}/expenses/{expenses.id} HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json
GET /users/25c8d1ed77/affordability/s55bf5 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json Example Reponse
HTTP/1.11.1 200 OK
Content-Type: application/json

{
  "type": "expenses",
  "id": "s55bf5",
  "fromMonth": "2017-12",
  "toMonth": "2018-12",
  "payments": [
    {
      "division": "Alcoholic beverages",
      "avgMonthly": "-850.00",
      "percentageTotal": 13.41,
      "subCategory": [
        {
          "summary": "monthly",
          "category": {
            "expenseClass": {
              "classCode": "0401000101",
              "classTitle": "Alcoholic beverages nfd for consumption off licensed premises",
              "divisionCode": "04",
              "divisionTitle": "Alcoholic beverages"
            }
          },
          "changeHistory": [
            {
              "date": "2019-07",
              "amount": "-2173.00"
            },
            {
              ...
            }
          ]
        }
      ]
    },
    {
      "division": "Food and non-alcoholic beverages",
      "avgMonthly": "-1933.00",
      "percentageTotal": 30.5,
      "subCategory": [
        {
          "summary": "monthly",
          "category": {
            "expenseClass": {
              "classCode": "0311010202",
              "classTitle": "Fast food and takeaway exc. coffee (not frozen)",
              "divisionCode": "03",
              "divisionTitle": "Food and non-alcoholic beverages"
            }
          },
          "changeHistory": [
            {
              "date": "2019-06",
              "amount": "-183.00"
            },
            {
              ...
            }
          ]
        },
        {
          "summary": "monthly",
          "category": {
            "expenseClass": {
              "classCode": "0300000000",
              "classTitle": "Food and non-alcoholic beverages nfd",
              "divisionCode": "03",
              "divisionTitle": "Food and non-alcoholic beverages"
            }
          },
          "changeHistory": [
            {
              "date": "2019-06",
              "amount": "-682.00"
            },
            {
              ...
            },
          ]
        }
      ]
    },
    {
      "division": "Transport",
      "avgMonthly": "-3553.00",
      "percentageTotal": 56.08,
      "subCategory": [
        {
          "summary": "monthly",
          "category": {
            "expenseClass": {
              "classCode": "1001030101",
              "classTitle": "Petrol",
              "divisionCode": "10",
              "divisionTitle": "Transport"
            }
          },
          "changeHistory": [
            {
              "date": "2019-06",
              "amount": "-2577.00"
            },
            {
              ...
            }
          ]
        }
      ]
    }
  ],
  "cashWithdrawals": {
    "avgMonthly": "-913.14",
    "summary": "monthly",
    "changeHistory": [
      {
        "date": "2018-06",
        "amount": "-240.00"
      },
      {
        ...
      }
    ]
  },
  "bankFees": {
    "avgMonthly": "-30.69",
    "summary": "monthly",
    "changeHistory": [
      {
        "date": "2018-06",
        "amount": "-3550.25"
      },
      {
       ...
      }
    ]
  },
  "externalTransfers": {
    "avgMonthly": "-300.00",
    "summary": "monthly",
    "changeHistory": [
      {
        "date": "2018-06",
        "amount": "-1000.00"
      },
      {
        ...
      }
    ]
  },
  "loanInterests": {
    "avgMonthly": "-4226.00",
    "summary": "monthly",
    "changeHistory": [
      {
      "date": "2018-06",
      "amount": "-1000.00"
      },
      {
        ...
      }
    ]
  },
  "loanRepayments": {
    "avgMonthly": "5658.00",
    "summary": "monthly",
    "changeHistory": [
      {
        "date": "2018-06",
        "amount": "-1000.00"
      },
      {
        ...
      }
    ]
  },
  "links": {
    "self": "https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5",
    "accounts": [
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08",
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430",
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089",
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056"
     ]
  }
}
```
