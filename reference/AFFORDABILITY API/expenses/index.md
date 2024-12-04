---
title: Expenses
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
The Expenses object returns an aggregated list of expenses by category of spend.

> 📘 Living Expenses Classification Standard
>
> Living Expenses are classified using Household Expense Classification (HEC) from the Australian Bureau of Statistics (ABS)
>
> Identify spend on utility bills, medical expenses, groceries and discretionary spend such as takeaways, gambling and clothing based on up to 13 months worth of data.

> 👍 Sandbox testing the Expenses endpoint (independently of Affordability)
>
> You will need to create a user and create or refresh all connections before creating a new income resource.  Use the *Wentworth-Smith* test credentials to create a connection for our test institution AU00000 before calling the Income endpoint. See our [testing](https://api.basiq.io/docs/testing-1) section for more information.
>
> **The Affordability API returns links to Income and Expenses resources -  if you use the Affordability endpoint there is no need to create an Income or Expense resource**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Expenses
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value of this resource is "expenses".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the affordability resource to be retrieved.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `fromMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        First 'month' occurrence of expenses categorised going back as far as 13 months. e.g. "2017-09"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `toMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        Latest 'month' occurrence of expenses categorised e.g. "2018-10"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `coverageDays`
      </td>

      <td style={{ textAlign: "left" }}>
        Number of days included in the report period.
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

> 📘 Living expenses are summarised at the both the broadest and most granular level of categorisation allowing you to roll up and roll down in your UI.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Payments Summary
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `division`
      </td>

      <td style={{ textAlign: "left" }}>
        Top level summary: category name.\
        e.g. Medical care and heath expenses, Food and non-alcoholic beverages, Education
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `avgMonthly`
      </td>

      <td style={{ textAlign: "left" }}>
        Average monthly amount by category for defined period (up to 13 months).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `percentageTotal`
      </td>

      <td style={{ textAlign: "left" }}>
        Average monthly amount expressed as a percentage of total expenses.
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

> 📘 Average Monthly Expenses
>
> This number monthly is calculated as follows: (Total Expenses/Report Coverage Days)\*30.\
> This allows data with partial months to be calculated correctly.

> 👍 Living expenses are also summarised at the most granular level
>
> Household Expenditure Classification (HEC) comes with four levels Division > Subdivisions > Groups > Classes

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Payments Sub-Category
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `summary`
      </td>

      <td style={{ textAlign: "left" }}>
        Summary period "monthly".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `category.expenseClass`
      </td>

      <td style={{ textAlign: "left" }}>
        Default is HEC classification: 4 levels class, group, subdivision and division. Two levels returned (broadest and most granular)

        Custom categories can be mapped to two levels output as `class` for the most granular level and `division` for the broadest level.  Ask us about custom category mapping.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `classCode` - classification code for HEC classification: e.g. class code = "0703030101" (or custom defined `classCode`)

        * `classTitle` - classification description for HEC classification:  e.g. class title =  "Non-electrical household appliances" (or custom defined `classTitle`)

        * `divisionCode` - classification description for HEC classification: e.g. division code =  "07" 

        * `divisionTitle` - classification description for HEC classification: 4 levels class, group, subdivision and division. e.g. class title =  "Household furnishings and equipment "
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `changeHistory`
      </td>

      <td style={{ textAlign: "left" }}>
        Amount classified as spent that month (repeated each month of data):
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `date`  - month expense relates e.g. "2018-09"

        * `amount` - amount of expense that period
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        note: aggregated expenses are rounded (to the nearest dollar) for each individual expense and then returned as the sum of the rounded figures for each month .
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Rounding of aggregated expenses
>
> Aggregated expenses are rounded (to the nearest dollar) for each individual expense and then returned as the sum of the rounded figures for each month .

```json Example of a single living expense by category
{
  "summary": "monthly",
  "category": {
    "hec": {
      "class": {
        "code": "0704019999",
        "title": "Glassware, tableware, cutlery and household utensils nec"
      },
      "group": {
        "code": "070401",
        "title": "Glassware, tableware, cutlery and household utensils"
      },
      "subdivision": {
        "code": "0704",
        "title": "Glassware, tableware, cutlery and household utensils"
      },
      "division": {
        "code": "07",
        "title": "Household furnishings and equipment"
      }
    }
  },
  "changeHistory": [
    {
      "date": "2018-09",
      "amount": "-29.65"
    },
    {
      "date": "2018-10",
      "amount": "-25.52"
    }
  ]
}
```

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Other
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `cashWithdrawals`
      </td>

      <td style={{ textAlign: "left" }}>
        Average monthly amount for *cash-withdrawal* for defined period:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `avgMonthly` - average amount monthly

        * `summary` -  summary period  "monthly"

        * `changeHistory` -  each amount classified, repeated by month, ordered by most recent

          * `date`  - month expense relates e.g. "2018-09"

          * `amount` - amount of classified that period
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `bankfees`
      </td>

      <td style={{ textAlign: "left" }}>
        Average monthly amount for *bank-fee* for defined period:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `avgMonthly` - average amount monthly

        * `summary` -  summary period  "monthly"

        * `changeHistory` -  each amount classified, repeated by month, ordered by most recent

          * `date`  - month expense relates e.g. "2018-09"

          * `amount` - amount of classified that period
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `externalTransfers`
      </td>

      <td style={{ textAlign: "left" }}>
        Average monthly amount for *external-transfer* for defined period:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `avgMonthly` - average amount monthly

        * `summary` -  summary period  "monthly"

        * `changeHistory` -  each amount classified, repeated by month, ordered by most recent

          * `date`  - month expense relates e.g. "2018-09"

          * `amount` - amount of classified that period
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `loanInterests`
      </td>

      <td style={{ textAlign: "left" }}>
        Average monthly amount debited for *loan-interest* for defined period:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `avgMonthly` - average amount monthly

        * `summary` -  summary period  "monthly"

        * `changeHistory` -  each amount classified, repeated by month, ordered by most recent

          * `date`  - month expense relates e.g. "2018-09"

          * `amount` - amount of classified that period
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `loanRepayments`
      </td>

      <td style={{ textAlign: "left" }}>
        [coming soon] Average monthly amount for *loan-repayment* for defined period:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `avgMonthly` - average amount monthly

        * `summary` -  summary period  "monthly"

        * `changeHistory` -  each amount classified, repeated by month, ordered by most recent

          * `date`  - month expense relates e.g. "2018-09"

          * `amount` - amount of classified that period
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

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Links
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `self` link to the requested expenses resource

        * `accounts` an array of [accounts](ref:accounts)\
          links
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

> 🚧 You will need to create a user and create or refresh all connections before creating the expenses resource.

**Returns**

Returns a created expenses resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Example Expense object
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
    "avgMonthly": "-3273.69",
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
