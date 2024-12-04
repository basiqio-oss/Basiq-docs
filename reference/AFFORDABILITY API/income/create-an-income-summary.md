---
title: Create an income summary
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
Use this to create a new income summary for an individual user. 

> 🚧 You will need to create a user and create or refresh all connections before creating the income resource.

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
        the first/start month to be included in the affordability output e.g. "fromMonth":"2019-05". Resulting income resource will be based on data between fromMonth and toMonth
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **toMonth**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        the last/end month to be included in the affordability output e.g. "toMonth":"2019-09". Resulting income resource will be based on data between fromMonth and toMonth
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

If the **optional** arguments (above) are not specified then the income resource will be created for the default dates: 13 months ago until current month and the resource is created for all accounts under the user if none are specified as arguments.  **All transactions in non-specified accounts are ignored.**

**Returns**

Returns a created income resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Definition
POST /users/{user.id}/income HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json Example Request
POST /users/25c8d1ed77/income HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json
```

```json Example Response
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
