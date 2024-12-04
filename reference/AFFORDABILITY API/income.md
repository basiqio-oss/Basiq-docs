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
[block:callout]
{
  "type": "info",
  "title": "",
  "body": "Income sources are identified based on patterns by amounts and frequency - to determine the regularity and reliability of each income source"
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "You will need to create a user and create or refresh all connections before creating a new income resource.  Use the *Wentworth-Smith* test credentials to create a connection for our test institution AU00000 before calling the Income endpoint. See our [testing](https://api.basiq.io/reference#testing) section for more information.\n\n**The Affordability API returns links to Income and Expenses resources -  if you use the Affordability endpoint there is no need to create an Income or Expense resource**",
  "title": "Sandbox testing the Income endpoint (independently of Affordability)"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "`type`",
    "2-0": "`id`",
    "9-0": "`summary`",
    "11-0": "",
    "11-1": "* `regularIncomeAvg`- total median regular income monthly calculated over the past 3 months for all regular sources\n\n* `regularIncomeYTD`- total regular income so far this financial year (year to date)\n\n* `regularIncomeYear`- total predicted regular income for this financial year year\n\n* `irregularIncomeAvg` - total mean of irregular income monthly calculated across the whole time period for all irregular sources",
    "0-1": "Value of this resource is \"income\".",
    "2-1": "The identifier of the income resource to be retrieved.",
    "9-1": "Summary totals relating to income analysis:",
    "3-0": "`fromMonth`",
    "5-0": "`toMonth`",
    "7-0": "`coverageDays`",
    "7-1": "Number of days included in the report period.",
    "3-1": "Start month for the period for which the Income summary is generated. The period of time relates to the account and transaction data used as input into the report.",
    "5-1": "End month (usually the current month)  for the period for which the Income summary is generated."
  },
  "cols": 2,
  "rows": 13
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Our complex income algorithm uses over 50 rules to identify different types of income sources. For example, to identify a regular income source - a fortnightly salary should have a repeating pattern over a 90 day time period with regular intervals and similar amounts. Additionally, tolerances are applied based on confidence in identified income source patterns (by amount and frequency). This means that a stable pattern with a gap in payment intervals will still be considered a regular income source with the stability being less than 1.",
  "title": ""
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Regular Sources",
    "0-0": "`source`",
    "2-0": "`frequency`",
    "24-0": "`ageDays`",
    "26-0": "`previous3Months`",
    "28-0": "",
    "30-0": "`current`",
    "32-0": "",
    "0-1": "Source regular income (cleaned transaction description).",
    "2-1": "Enum detailing frequency regular income e.g. \"bi-weekly\"",
    "24-1": "Duration regular income (number days from first to last occurrence) returned as an **integer** with values zero or greater",
    "26-1": "Summary for regular income sources for past 3 months:",
    "28-1": "* `amountAvg` - median regular income amount - calculated across all occurrences in last 3 months (note: median provides a more reliable amount than mean for a regular income source as it is less affected by outliers and skewed data - use `variance` amount to understand outliers and `changeHistory` to view actual credits)\n\n* `amountAvgMonthly`- median monthly regular income amount \n\n* `variance` - standard deviation in credits for the regular income series. The algorithm works out the Mean (the simple average of the numbers) Then for each credit: subtract the Mean and square the result. Then work out the mean of those squared differences. The variance is the square root of that.",
    "30-1": "Most recent data relating to regular income source:",
    "32-1": "* `date` - most recent regular income payment date\n\n* `amount` - most recent regular income payment amount\n\n* `nextdate` - predicted next occurrence for regular income (note: where the pattern has recently ceased there would be no predicted next occurrence)",
    "34-0": "`changeHistory`",
    "34-1": "Each amount classified as income (repeated for each income credit and ordered by most recent):",
    "36-1": "* `date`  - date income received e.g. \"2018-03-15T17:00:00\"\n\n* `amount` - amount of income for that period\n\n* `source` - source income (cleaned transaction description).",
    "18-0": "`irregularity`",
    "18-1": "Indication of income gaps within the regular income series",
    "20-1": "* `stability` an indicative score between 0 and 1 that factors in the gaps between credits in a regular income series as well as the variation in the credit amounts. Stability scores close to 1 indicate highly stable income. Stability scores lower than 0.5 would be unusual as the series has to show a level of uniformity to be categorised as Regular Income. The calculation is based on pairing sequential credits and then conducting Fourier Transformation.",
    "22-1": "* `gaps` array of dates for which the expected credit is not met",
    "21-1": "",
    "4-1": "- `daily`",
    "6-1": "- `weekly`",
    "8-1": "- `bi-weekly` (fortnightly)",
    "10-1": "- `monthly`",
    "12-1": "- `bi-monthly` (every 2 months)",
    "14-1": "- `quarterly`",
    "16-1": "- `half-year`"
  },
  "cols": 2,
  "rows": 38
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Irregular Income sources typically require repeating credits with pattern by frequency or amount across a minimum 90 day time period",
  "title": ""
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Irregular Sources",
    "0-0": "`source`",
    "2-0": "`frequency`",
    "4-0": "`ageDays`",
    "12-0": "`current`",
    "14-0": "",
    "2-1": "Frequency is \"irregular\"",
    "0-1": "Source irregular income (cleaned transaction description).",
    "4-1": "Duration irregular income (number days from first to last occurrence) returned as an **integer** with values zero or greater",
    "6-0": "`amountAvg`",
    "12-1": "Most recent data relating to irregular income source:",
    "14-1": "* `date` - most recent irregular income payment date\n\n* `amount` - most recent irregular income payment amount",
    "6-1": "Mean of irregular income amount - calculated across all occurrences identified.",
    "16-0": "`changeHistory`",
    "16-1": "Each amount classified as income (repeated for each income credit and ordered by most recent):",
    "18-1": "* `date`  - date income received e.g. \"2018-03-15T17:00:00\"\n\n* `amount` - amount of income for that period\n\n* `source` - source income (cleaned transaction description).",
    "19-0": "",
    "8-0": "`noOccurrences`",
    "10-0": "`avgMonthlyOccurence`",
    "8-1": "Number of instances of credits in the series.",
    "10-1": "Average (mean) number of times per calendar month the credits in the series occur."
  },
  "cols": 2,
  "rows": 20
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Other Credit Series are series where a pattern of credit is detected but the pattern does not meet the requirements for regular or irregular income, or the income series is too old e.g. former regular income or a potential future income"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Other Credit Sources",
    "0-0": "`source`",
    "0-1": "Source Other Credit income (cleaned transaction description).",
    "4-0": "`age day`",
    "4-1": "Duration other income (number days from first to last occurrence) returned as an **integer** with values zero or greater.",
    "6-0": "`amountAvg`",
    "6-1": "Mean of irregular income amount - calculated across all occurrences identified.",
    "8-0": "`noOccurrences`",
    "8-1": "Number of instances of credits in the series.",
    "10-0": "`avgMonthlyOccurence`",
    "10-1": "Average (mean) number of times per calendar month the credits in the series occur.",
    "12-0": "`current`",
    "12-1": "Most recent data relating to other income source:",
    "14-1": "* `date` - most recent irregular income payment date\n\n* `amount` - most recent irregular income payment amount\n\n* `otherCreditLabel` - description of the other credit series e.g. 'former regular income'",
    "16-0": "`changeHistory`",
    "16-1": "Each amount classified as income (repeated for each income credit and ordered by most recent):",
    "17-1": "* `date`  - date income received e.g. \"2018-03-15T17:00:00\"\n\n* `amount` - amount of income for that period\n\n* `source` - source income (cleaned transaction description).",
    "2-0": "`frequency`",
    "2-1": "Frequency is \"other\", \"irregular\" or a time period e.g. \"bi-weekly\""
  },
  "cols": 2,
  "rows": 18
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Links",
    "0-0": "`links`",
    "0-1": "A links object containing the following members:",
    "2-1": "- `self` link to the requested income resource\n\n- `accounts` an array of [accounts](ref:accounts) \nlinks",
    "3-1": ""
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "You will need to create a user and create or refresh all connections before creating the income resource."
}
[/block]
**Returns**

Returns a created income resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.11.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"income\",\n  \"id\": \"s55bf4\",\n  \"fromMonth\": \"2018-11\",\n  \"toMonth\": \"2019-11\",\n  \"coverageDays\": 394,\n  \"generatedDate\": \"2019-12-10T05:49:15\",\n  \"summary\": {\n    \"regularIncomeAvg\": \"18098.00\",\n    \"regularIncomeYTD\": \"90490.00\",\n    \"regularIncomeYear\": \"217176.00\",\n    \"irregularIncomeAvg\": \"55.00\"\n  },\n  \"regular\": [\n    {\n      \"source\": \"payroll wfrms 15439393\",\n      \"frequency\": \"monthly\",\n      \"ageDays\": 334,\n      \"irregularity\": {\n        \"stability\": \"1.00\",\n        \"gaps\": []\n      },\n      \"previous3Months\": {\n        \"amountAvg\": \"18098.00\",\n        \"amountAvgMonthly\": \"18098.00\",\n        \"variance\": \"0.00\"\n      },\n      \"current\": {\n        \"date\": \"2018-11-30T09:23:37\",\n        \"amount\": \"18098.00\",\n        \"nextDate\": \"2018-12-30T18:30:49\"\n      },\n      \"changeHistory\": [\n        {\n          \"source\": \"Payroll WFRMS 15439393\",\n          \"date\": \"2018-11-30T09:23:37\",\n          \"amount\": \"18098.00\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"irregular\": [\n    {\n      \"source\": \"ctrlink carers 998r6789201610974v\",\n      \"frequency\": \"irregular\",\n      \"ageDays\": 253,\n      \"amountAvg\": \"55.00\",\n      \"noOccurrences\": 5,\n      \"avgMonthlyOccurence\": \"1\",\n      \"current\": {\n        \"date\": \"2018-10-13T20:03:37\",\n        \"amount\": \"62.00\"\n      },\n      \"changeHistory\": [\n        {\n          \"source\": \"CTRLINK CARERS Ref: 998R6789201610974V\",\n          \"date\": \"2018-10-13T20:03:37\",\n          \"amount\": \"62.00\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"otherCredit\": [\n    {\n      \"source\": \"savings interest cr bal - Account 1\",\n      \"frequency\": \"monthly\",\n      \"ageDay\": 335,\n      \"amountAvg\": \"110.85\",\n      \"noOccurrences\": 12,\n      \"avgMonthlyOccurence\": \"1\",\n      \"current\": {\n        \"date\": \"2019-10-29T00:00:00\",\n        \"amount\": \"92.99\",\n        \"otherCreditLabel\": \"regular income small amount\"\n      },\n      \"changeHistory\": [\n        {\n          \"source\": \"savings interest cr bal - Account 1\",\n          \"date\": \"2018-10-13T20:03:37\",\n          \"amount\": \"62.00\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4\",\n    \"accounts\": [\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056\"\n     ]\n  }\n}",
      "language": "json",
      "name": "Example Income object"
    }
  ],
  "sidebar": true
}
[/block]