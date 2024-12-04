---
title: Create an expense summary
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
Use this to create a new expense summary for an individual user. 

> 🚧 You will need to create a user and create or refresh all connections before creating the expenses resource.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Arguments (body)
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **fromMonth**
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        the first/start month to be included in the expense output e.g. "fromMonth":"2019-05". Resulting income resource will be based on data between fromMonth and toMonth
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **toMonth**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        the last/end month to be included in the expense output e.g. "toMonth":"2019-09". Resulting income resource will be based on data between fromMonth and toMonth
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        e.g. of body text\
        \{\
        "fromMonth":"2019-05",\
        "toMonth":"2019-09"\
        }
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **accounts**\
        *array, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        an array of account ids
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        e.g. of body text

        \{\
          "accounts": [\
            "20024b08",\
            "64880430"\
          ][
            "20024b08",
            "64880430"
          ]\
        }
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

If the **optional** arguments (above) are not specified then the expense resource will be created for the default dates: 13 months ago until current month and the resource is created for all accounts under the user if none are specified as arguments.  **All transactions in non-specified accounts are ignored.**

**Returns**

Returns a created expenses resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Definition
POST /users/{user.id}/expenses HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json Example Request
POST /users/25c8d1ed77/expenses HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json Example Response
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
