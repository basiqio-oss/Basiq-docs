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
[block:callout]
{
  "type": "info",
  "title": "Living Expenses Classification Standard",
  "body": "Living Expenses are classified using Household Expense Classification (HEC) from the Australian Bureau of Statistics (ABS)\n\nIdentify spend on utility bills, medical expenses, groceries and discretionary spend such as takeaways, gambling and clothing based on up to 13 months worth of data."
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "You will need to create a user and create or refresh all connections before creating a new income resource.  Use the *Wentworth-Smith* test credentials to create a connection for our test institution AU00000 before calling the Income endpoint. See our [testing](https://api.basiq.io/docs/testing-1) section for more information.\n\n**The Affordability API returns links to Income and Expenses resources -  if you use the Affordability endpoint there is no need to create an Income or Expense resource**",
  "title": "Sandbox testing the Expenses endpoint (independently of Affordability)"
}
[/block]

[block:parameters]
{
  "data": {
    "0-0": "`type`",
    "2-0": "`id`",
    "4-0": "`fromMonth`",
    "6-0": "`toMonth`",
    "h-0": "Expenses",
    "0-1": "Value of this resource is \"expenses\".",
    "2-1": "The identifier of the affordability resource to be retrieved.",
    "4-1": "First 'month' occurrence of expenses categorised going back as far as 13 months. e.g. \"2017-09\"",
    "6-1": "Latest 'month' occurrence of expenses categorised e.g. \"2018-10\"",
    "8-1": "Number of days included in the report period.",
    "8-0": "`coverageDays`"
  },
  "cols": 2,
  "rows": 10
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Living expenses are summarised at the both the broadest and most granular level of categorisation allowing you to roll up and roll down in your UI."
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Payments Summary",
    "0-0": "`division`",
    "2-0": "`avgMonthly`",
    "4-0": "`percentageTotal`",
    "0-1": "Top level summary: category name.\ne.g. Medical care and heath expenses, Food and non-alcoholic beverages, Education",
    "2-1": "Average monthly amount by category for defined period (up to 13 months).",
    "4-1": "Average monthly amount expressed as a percentage of total expenses."
  },
  "cols": 2,
  "rows": 6
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "This number monthly is calculated as follows: (Total Expenses/Report Coverage Days)*30.  \nThis allows data with partial months to be calculated correctly.",
  "title": "Average Monthly Expenses"
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "Living expenses are also summarised at the most granular level",
  "body": "Household Expenditure Classification (HEC) comes with four levels Division > Subdivisions > Groups > Classes"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Payments Sub-Category",
    "0-0": "`summary`",
    "2-0": "`category.expenseClass`",
    "4-0": "",
    "6-0": "`changeHistory`",
    "0-1": "Summary period \"monthly\".",
    "2-1": "Default is HEC classification: 4 levels class, group, subdivision and division. Two levels returned (broadest and most granular)\n\nCustom categories can be mapped to two levels output as `class` for the most granular level and `division` for the broadest level.  Ask us about custom category mapping.",
    "4-1": "* `classCode` - classification code for HEC classification: e.g. class code = \"0703030101\" (or custom defined `classCode`)\n\n* `classTitle` - classification description for HEC classification:  e.g. class title =  \"Non-electrical household appliances\" (or custom defined `classTitle`)\n\n* `divisionCode` - classification description for HEC classification: e.g. division code =  \"07\" \n\n* `divisionTitle` - classification description for HEC classification: 4 levels class, group, subdivision and division. e.g. class title =  \"Household furnishings and equipment \"",
    "6-1": "Amount classified as spent that month (repeated each month of data):",
    "8-1": "* `date`  - month expense relates e.g. \"2018-09\"\n\n* `amount` - amount of expense that period",
    "10-1": "note: aggregated expenses are rounded (to the nearest dollar) for each individual expense and then returned as the sum of the rounded figures for each month ."
  },
  "cols": 2,
  "rows": 11
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Aggregated expenses are rounded (to the nearest dollar) for each individual expense and then returned as the sum of the rounded figures for each month .",
  "title": "Rounding of aggregated expenses"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"summary\": \"monthly\",\n  \"category\": {\n    \"hec\": {\n      \"class\": {\n        \"code\": \"0704019999\",\n        \"title\": \"Glassware, tableware, cutlery and household utensils nec\"\n      },\n      \"group\": {\n        \"code\": \"070401\",\n        \"title\": \"Glassware, tableware, cutlery and household utensils\"\n      },\n      \"subdivision\": {\n        \"code\": \"0704\",\n        \"title\": \"Glassware, tableware, cutlery and household utensils\"\n      },\n      \"division\": {\n        \"code\": \"07\",\n        \"title\": \"Household furnishings and equipment\"\n      }\n    }\n  },\n  \"changeHistory\": [\n    {\n      \"date\": \"2018-09\",\n      \"amount\": \"-29.65\"\n    },\n    {\n      \"date\": \"2018-10\",\n      \"amount\": \"-25.52\"\n    }\n  ]\n}",
      "language": "json",
      "name": "Example of a single living expense by category"
    }
  ],
  "sidebar": true
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Other",
    "0-0": "`cashWithdrawals`",
    "4-0": "`bankfees`",
    "8-0": "`externalTransfers`",
    "0-1": "Average monthly amount for *cash-withdrawal* for defined period:",
    "4-1": "Average monthly amount for *bank-fee* for defined period:",
    "8-1": "Average monthly amount for *external-transfer* for defined period:",
    "2-1": "* `avgMonthly` - average amount monthly\n\n* `summary` -  summary period  \"monthly\"\n\n* `changeHistory` -  each amount classified, repeated by month, ordered by most recent\n\n     * `date`  - month expense relates e.g. \"2018-09\"\n\n     * `amount` - amount of classified that period",
    "6-1": "* `avgMonthly` - average amount monthly\n\n* `summary` -  summary period  \"monthly\"\n\n* `changeHistory` -  each amount classified, repeated by month, ordered by most recent\n\n     * `date`  - month expense relates e.g. \"2018-09\"\n\n     * `amount` - amount of classified that period",
    "10-1": "* `avgMonthly` - average amount monthly\n\n* `summary` -  summary period  \"monthly\"\n\n* `changeHistory` -  each amount classified, repeated by month, ordered by most recent\n\n     * `date`  - month expense relates e.g. \"2018-09\"\n\n     * `amount` - amount of classified that period",
    "12-0": "`loanInterests`",
    "16-0": "`loanRepayments`",
    "12-1": "Average monthly amount debited for *loan-interest* for defined period:",
    "16-1": "[coming soon] Average monthly amount for *loan-repayment* for defined period:",
    "14-1": "* `avgMonthly` - average amount monthly\n\n* `summary` -  summary period  \"monthly\"\n\n* `changeHistory` -  each amount classified, repeated by month, ordered by most recent\n\n     * `date`  - month expense relates e.g. \"2018-09\"\n\n     * `amount` - amount of classified that period",
    "18-1": "* `avgMonthly` - average amount monthly\n\n* `summary` -  summary period  \"monthly\"\n\n* `changeHistory` -  each amount classified, repeated by month, ordered by most recent\n\n     * `date`  - month expense relates e.g. \"2018-09\"\n\n     * `amount` - amount of classified that period"
  },
  "cols": 2,
  "rows": 20
}
[/block]

[block:parameters]
{
  "data": {
    "2-0": "",
    "h-0": "Links",
    "2-1": "- `self` link to the requested expenses resource\n\n- `accounts` an array of [accounts](ref:accounts) \nlinks",
    "0-0": "`links`",
    "0-1": "A links object containing the following members:"
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "You will need to create a user and create or refresh all connections before creating the expenses resource."
}
[/block]
**Returns**

Returns a created expenses resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.11.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"expenses\",\n  \"id\": \"s55bf5\",\n  \"fromMonth\": \"2017-12\",\n  \"toMonth\": \"2018-12\",\n  \"payments\": [\n    {\n      \"division\": \"Alcoholic beverages\",\n      \"avgMonthly\": \"-850.00\",\n      \"percentageTotal\": 13.41,\n      \"subCategory\": [\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"0401000101\",\n              \"classTitle\": \"Alcoholic beverages nfd for consumption off licensed premises\",\n              \"divisionCode\": \"04\",\n              \"divisionTitle\": \"Alcoholic beverages\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-07\",\n              \"amount\": \"-2173.00\"\n            },\n            {\n              ...\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"division\": \"Food and non-alcoholic beverages\",\n      \"avgMonthly\": \"-1933.00\",\n      \"percentageTotal\": 30.5,\n      \"subCategory\": [\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"0311010202\",\n              \"classTitle\": \"Fast food and takeaway exc. coffee (not frozen)\",\n              \"divisionCode\": \"03\",\n              \"divisionTitle\": \"Food and non-alcoholic beverages\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-06\",\n              \"amount\": \"-183.00\"\n            },\n            {\n              ...\n            }\n          ]\n        },\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"0300000000\",\n              \"classTitle\": \"Food and non-alcoholic beverages nfd\",\n              \"divisionCode\": \"03\",\n              \"divisionTitle\": \"Food and non-alcoholic beverages\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-06\",\n              \"amount\": \"-682.00\"\n            },\n            {\n              ...\n            },\n          ]\n        }\n      ]\n    },\n    {\n      \"division\": \"Transport\",\n      \"avgMonthly\": \"-3553.00\",\n      \"percentageTotal\": 56.08,\n      \"subCategory\": [\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"1001030101\",\n              \"classTitle\": \"Petrol\",\n              \"divisionCode\": \"10\",\n              \"divisionTitle\": \"Transport\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-06\",\n              \"amount\": \"-2577.00\"\n            },\n            {\n              ...\n            }\n          ]\n        }\n      ]\n    }\n  ],\n  \"cashWithdrawals\": {\n    \"avgMonthly\": \"-913.14\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-240.00\"\n      },\n      {\n        ...\n      }\n    ]\n  },\n  \"bankFees\": {\n    \"avgMonthly\": \"-3273.69\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-3550.25\"\n      },\n      {\n       ...\n      }\n    ]\n  },\n  \"externalTransfers\": {\n    \"avgMonthly\": \"-300.00\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-1000.00\"\n      },\n      {\n        ...\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5\",\n    \"accounts\": [\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056\"\n     ]\n  }\n}",
      "language": "json",
      "name": "Example Expense object"
    }
  ],
  "sidebar": true
}
[/block]