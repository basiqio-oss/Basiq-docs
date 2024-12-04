---
title: Income
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
The Income Summary object with income summarised and classified by type: regular, irregular or other sources (created/refreshed across up to 10 institutions)

> 📘
>
> Income sources are identified based on patterns by amounts and frequency - to determine the regularity and reliability of each income source

> 👍 Sandbox testing the Income endpoint (independently of Affordability)
>
> You will need to create a user and create or refresh all connections before creating a new income resource.  Use the *Wentworth-Smith* test credentials to create a connection for our test institution AU00000 before calling the Income endpoint. See our [testing](https://api.basiq.io/reference#testing) section for more information.
>
> **The Affordability API returns links to Income and Expenses resources -  if you use the Affordability endpoint there is no need to create an Income or Expense resource**

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
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
        Value of this resource is "income".
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
        The identifier of the income resource to be retrieved.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `fromMonth`
      </td>

      <td style={{ textAlign: "left" }}>
        Start month for the period for which the Income summary is generated. The period of time relates to the account and transaction data used as input into the report.
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
        End month (usually the current month)  for the period for which the Income summary is generated.
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

    <tr>
      <td style={{ textAlign: "left" }}>
        `summary`
      </td>

      <td style={{ textAlign: "left" }}>
        Summary totals relating to income analysis:
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
        * `regularIncomeAvg`- total median regular income monthly calculated over the past 3 months for all regular sources

        * `regularIncomeYTD`- total regular income so far this financial year (year to date)

        * `regularIncomeYear`- total predicted regular income for this financial year year

        * `irregularIncomeAvg` - total mean of irregular income monthly calculated across the whole time period for all irregular sources
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

> 📘
>
> Our complex income algorithm uses over 50 rules to identify different types of income sources. For example, to identify a regular income source - a fortnightly salary should have a repeating pattern over a 90 day time period with regular intervals and similar amounts. Additionally, tolerances are applied based on confidence in identified income source patterns (by amount and frequency). This means that a stable pattern with a gap in payment intervals will still be considered a regular income source with the stability being less than 1.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Regular Sources
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `source`
      </td>

      <td style={{ textAlign: "left" }}>
        Source regular income (cleaned transaction description).
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
        `frequency`
      </td>

      <td style={{ textAlign: "left" }}>
        Enum detailing frequency regular income e.g. "bi-weekly"
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
        * `daily`
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
        * `weekly`
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
        * `bi-weekly` (fortnightly)
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
        * `monthly`
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
        * `bi-monthly` (every 2 months)
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
        * `quarterly`
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
        * `half-year`
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
        `irregularity`
      </td>

      <td style={{ textAlign: "left" }}>
        Indication of income gaps within the regular income series
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
        * `stability` an indicative score between 0 and 1 that factors in the gaps between credits in a regular income series as well as the variation in the credit amounts. Stability scores close to 1 indicate highly stable income. Stability scores lower than 0.5 would be unusual as the series has to show a level of uniformity to be categorised as Regular Income. The calculation is based on pairing sequential credits and then conducting Fourier Transformation.
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
        * `gaps` array of dates for which the expected credit is not met
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
        `ageDays`
      </td>

      <td style={{ textAlign: "left" }}>
        Duration regular income (number days from first to last occurrence) returned as an **integer** with values zero or greater
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
        `previous3Months`
      </td>

      <td style={{ textAlign: "left" }}>
        Summary for regular income sources for past 3 months:
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
        * `amountAvg` - median regular income amount - calculated across all occurrences in last 3 months (note: median provides a more reliable amount than mean for a regular income source as it is less affected by outliers and skewed data - use `variance` amount to understand outliers and `changeHistory` to view actual credits)

        * `amountAvgMonthly`- median monthly regular income amount 

        * `variance` - standard deviation in credits for the regular income series. The algorithm works out the Mean (the simple average of the numbers) Then for each credit: subtract the Mean and square the result. Then work out the mean of those squared differences. The variance is the square root of that.
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
        `current`
      </td>

      <td style={{ textAlign: "left" }}>
        Most recent data relating to regular income source:
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
        * `date` - most recent regular income payment date

        * `amount` - most recent regular income payment amount

        * `nextdate` - predicted next occurrence for regular income (note: where the pattern has recently ceased there would be no predicted next occurrence)
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
        Each amount classified as income (repeated for each income credit and ordered by most recent):
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
        * `date`  - date income received e.g. "2018-03-15T17:00:00"

        * `amount` - amount of income for that period

        * `source` - source income (cleaned transaction description).
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

> 📘
>
> Irregular Income sources typically require repeating credits with pattern by frequency or amount across a minimum 90 day time period

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Irregular Sources
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `source`
      </td>

      <td style={{ textAlign: "left" }}>
        Source irregular income (cleaned transaction description).
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
        `frequency`
      </td>

      <td style={{ textAlign: "left" }}>
        Frequency is "irregular"
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
        `ageDays`
      </td>

      <td style={{ textAlign: "left" }}>
        Duration irregular income (number days from first to last occurrence) returned as an **integer** with values zero or greater
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
        `amountAvg`
      </td>

      <td style={{ textAlign: "left" }}>
        Mean of irregular income amount - calculated across all occurrences identified.
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
        `noOccurrences`
      </td>

      <td style={{ textAlign: "left" }}>
        Number of instances of credits in the series.
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
        `avgMonthlyOccurence`
      </td>

      <td style={{ textAlign: "left" }}>
        Average (mean) number of times per calendar month the credits in the series occur.
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
        `current`
      </td>

      <td style={{ textAlign: "left" }}>
        Most recent data relating to irregular income source:
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
        * `date` - most recent irregular income payment date

        * `amount` - most recent irregular income payment amount
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
        Each amount classified as income (repeated for each income credit and ordered by most recent):
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
        * `date`  - date income received e.g. "2018-03-15T17:00:00"

        * `amount` - amount of income for that period

        * `source` - source income (cleaned transaction description).
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

> 📘 Other Credit Series are series where a pattern of credit is detected but the pattern does not meet the requirements for regular or irregular income, or the income series is too old e.g. former regular income or a potential future income

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Other Credit Sources
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `source`
      </td>

      <td style={{ textAlign: "left" }}>
        Source Other Credit income (cleaned transaction description).
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
        `frequency`
      </td>

      <td style={{ textAlign: "left" }}>
        Frequency is "other", "irregular" or a time period e.g. "bi-weekly"
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
        `age day`
      </td>

      <td style={{ textAlign: "left" }}>
        Duration other income (number days from first to last occurrence) returned as an **integer** with values zero or greater.
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
        `amountAvg`
      </td>

      <td style={{ textAlign: "left" }}>
        Mean of irregular income amount - calculated across all occurrences identified.
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
        `noOccurrences`
      </td>

      <td style={{ textAlign: "left" }}>
        Number of instances of credits in the series.
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
        `avgMonthlyOccurence`
      </td>

      <td style={{ textAlign: "left" }}>
        Average (mean) number of times per calendar month the credits in the series occur.
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
        `current`
      </td>

      <td style={{ textAlign: "left" }}>
        Most recent data relating to other income source:
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
        * `date` - most recent irregular income payment date

        * `amount` - most recent irregular income payment amount

        * `otherCreditLabel` - description of the other credit series e.g. 'former regular income'
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
        Each amount classified as income (repeated for each income credit and ordered by most recent):
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `date`  - date income received e.g. "2018-03-15T17:00:00"

        * `amount` - amount of income for that period

        * `source` - source income (cleaned transaction description).
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
        * `self` link to the requested income resource

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

> 🚧 You will need to create a user and create or refresh all connections before creating the income resource.

**Returns**

Returns a created income resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).

```json Example Income object
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
