---
title: Retrieve an income summary
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
Retrieves the details of an income summary. You need only supply the unique transaction identifier.

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
        A string that uniquely identifies the income summary as a resource
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

> 🚧 You will need an income id from an object you have created to retrieve an income object.

**Returns**

Returns a created income resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Definition
GET /users/{user.id}/income/{income.id} HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json
GET /users/25c8d1ed77/income/s55bf4 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json Example Reponse
HTTP/1.11.1 200 OK
Content-Type: application/json

{
  "type": "income",
  "id": "s55bf4",
  "fromMonth": "2018-11",
  "toMonth": "2019-11",
  "coverageDays": 394,
  "generatedDate": "2019-12-10T05:49:15",
  "summary": {
    "regularIncomeAvg": "18098.00",
    "regularIncomeYTD": "90490.00",
    "regularIncomeYear": "217176.00",
    "irregularIncomeAvg": "55.00"
  },
  "regular": [
    {
      "source": "payroll wfrms 15439393",
      "frequency": "monthly",
      "ageDays": 334,
      "irregularity": {
        "stability": "1.00",
        "gaps": []
      },
      "previous3Months": {
        "amountAvg": "18098.00",
        "amountAvgMonthly": "18098.00",
        "variance": "0.00"
      },
      "current": {
        "date": "2018-11-30T09:23:37",
        "amount": "18098.00",
        "nextDate": "2018-12-30T18:30:49"
      },
      "changeHistory": [
        {
          "source": "Payroll WFRMS 15439393",
          "date": "2018-11-30T09:23:37",
          "amount": "18098.00"
        },
        {
          ...
        }
      ]
    }
  ],
  "irregular": [
    {
      "source": "ctrlink carers 998r6789201610974v",
      "frequency": "irregular",
      "ageDays": 253,
      "amountAvg": "55.00",
      "noOccurrences": 5,
      "avgMonthlyOccurence": "1",
      "current": {
        "date": "2018-10-13T20:03:37",
        "amount": "62.00"
      },
      "changeHistory": [
        {
          "source": "CTRLINK CARERS Ref: 998R6789201610974V",
          "date": "2018-10-13T20:03:37",
          "amount": "62.00"
        },
        {
          ...
        }
      ]
    }
  ],
  "otherCredit": [
    {
      "source": "savings interest cr bal - Account 1",
      "frequency": "monthly",
      "ageDay": 335,
      "amountAvg": "110.85",
      "noOccurrences": 12,
      "avgMonthlyOccurence": "1",
      "current": {
        "date": "2019-10-29T00:00:00",
        "amount": "92.99",
        "otherCreditLabel": "regular income small amount"
      },
      "changeHistory": [
        {
          "source": "savings interest cr bal - Account 1",
          "date": "2018-10-13T20:03:37",
          "amount": "62.00"
        },
        {
          ...
        }
      ]
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4",
    "accounts": [
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08",
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430",
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089",
         "https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056"
     ]
  }
}
```
