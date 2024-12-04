---
title: Affordability
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
The affordability object includes a summary of financial position, assets, liabilities, with links to an income object and an expenses object, for an individual user for account and transaction data stored against that user
[block:callout]
{
  "type": "info",
  "title": "PDF response also available",
  "body": "The affordability API returns a JSON response by default however you can specify to return a PDF report version of the affordability summary"
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "Sandbox testing the Affordability endpoint",
  "body": "You will need to create a user and create or refresh all connections before creating an affordability resource.  Use the *Wentworth-Smith* test credentials to create a connection for our test institution AU00000 before calling the Affordability endpoint. See our [testing](https://api.basiq.io/v2.1/reference/testing) section for more information."
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "`type`",
    "0-1": "Value of this resource is \"affordability\"",
    "2-0": "`id`",
    "2-1": "The identifier of the affordability resource to be retrieved.",
    "4-0": "`fromMonth`",
    "6-0": "`toMonth`",
    "10-0": "`generatedDate`",
    "4-1": "Start month for the period for which the Affordability summary is generated. The period of time relates to the account and transaction data used as input into the report.",
    "6-1": "End month (usually the current month)  for the period for which the Affordability summary is generated.",
    "10-1": "Date the report was generated. e.g. \"2018-09-12T00:59:28\"",
    "5-1": "",
    "8-0": "`coverageDays`",
    "8-1": "Number of days included in the report period."
  },
  "cols": 2,
  "rows": 12
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Summary",
    "0-0": "",
    "9-0": "`regularIncome`",
    "11-0": "`expenses`",
    "15-0": "`currentBalance`",
    "17-0": "`availableFunds`",
    "19-0": "`minBalancePrevious6months`",
    "21-0": "`maxBalancePrevious6months`",
    "23-0": "`currency`",
    "1-0": "`assets`",
    "1-1": "Total of cash based assets",
    "9-1": "Provides an average of monthly - `avgMonthly` regular income calculated over the previous 3 month period `previous3Months`.\n\nFor example:\n\"regularIncome\": {\n            \"previous3Months\": {\n                \"avgMonthly\": \"5000.00\"\n            }\n        }",
    "13-0": "`savings`",
    "11-1": "Provides an average of monthly expenses calculated for the whole period of data retrieved (e.g. 13 months)",
    "13-1": "Average of monthly savings calculated for the whole period of data retrieved (e.g. 13 months)",
    "3-0": "`liabilities`",
    "5-0": "`netPosition`",
    "7-0": "`creditLimit`",
    "3-1": "Total of account based liabilities split into credit and loan liabilities",
    "5-1": "Total assets minus total liabilities",
    "7-1": "Total credit limit across all credit cards and overdrafts"
  },
  "cols": 2,
  "rows": 15
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Assets",
    "0-0": "`type`",
    "4-0": "`balance`",
    "6-0": "`availableFunds`",
    "8-0": "`account`",
    "8-1": "Identifies the **type** and **product** of the account:",
    "12-0": "`institution`",
    "12-1": "The name of the financial institution with whom the account is held.",
    "14-0": "`previous6months`",
    "0-1": "Value of this resource is \"account\"",
    "4-1": "The balance at the time of the query.",
    "6-1": "The available funds at the time of the query.",
    "14-1": "Includes minimum and maximum balances recorded in the account of the queried period.",
    "16-1": "- `minBalance`\n\n- `maxBalance`",
    "10-1": "- `type` (values as defined in `class` object `Account Type` in [Accounts](ref:accounts)\n\n- `product` (as defined by the institution)",
    "2-0": "`currency`",
    "2-1": "The currency in which the account is recorded."
  },
  "cols": 2,
  "rows": 18
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Credit Liabilities",
    "16-0": "`previous6months`",
    "20-0": "`creditLimit`",
    "0-0": "`currency`",
    "0-1": "The currency in which the account is recorded.",
    "2-0": "`balance`",
    "2-1": "The balance at the time of the query.",
    "4-0": "`availableFunds`",
    "4-1": "The available funds at the time of the query.",
    "6-0": "`account`",
    "6-1": "Identifies the **type** and **product** of the account:",
    "10-1": "The name of the financial institution with whom the account is held.",
    "10-0": "`institution`",
    "12-0": "`previousMonth`",
    "12-1": "A summary of the credit facility activity of the previous month, consisting of:",
    "16-1": "Acknowledges any cash advances made in the previous 6 months:",
    "20-1": "Total credit limit available for the specified credit facility.",
    "8-1": "- `type` (values as defined in `class` object `Account Type` in [Accounts](ref:accounts)\n\n- `product` (as defined by the institution)",
    "14-1": "- `totalCredits`\n\n- `totalDebits`\n\n- `minBalance`\n\n- `maxBalance`",
    "18-1": "- `cashAdvances` - value of cash advances in period"
  },
  "cols": 2,
  "rows": 22
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Loan Liabilities",
    "2-0": "`balance`",
    "4-0": "`availableFunds`",
    "6-0": "`account`",
    "10-0": "`institution`",
    "12-0": "`previousMonth`",
    "19-0": "`previous6months`",
    "20-0": "",
    "0-0": "`currency`",
    "0-1": "The currency in which the account is recorded.",
    "2-1": "The balance at the time of the query.",
    "4-1": "The available funds at the time of the query.",
    "6-1": "Identifies the **type** and **product** of the account:",
    "10-1": "The name of the financial institution with whom the account is held.",
    "12-1": "A summary of the credit facility activity of the previous month, consisting of:",
    "19-1": "Acknowledges if the account is in repayment arrears:",
    "14-1": "- `totalCredits`\n\n- `totalDebits`\n\n- `totalInterestCharged`\n \n- `totalRepayments`",
    "21-1": "- `arrears` - has the loan been in arrears in the past 6 months -  returned as a **string** value (*true* or *false* or *null*)",
    "8-1": "- `type` (values as defined in `class` object `Account Type` in [Accounts](ref:accounts)\n\n- `product` (as defined by the institution)",
    "16-0": "`changeHistory`",
    "17-1": "* `direction`  - debit or credit\n\n* `amount` - amount loan-interest or loan-repayment\n\n* `date`  - date  e.g. \"2019-03-15T17:00:00\"\n\n* `source` - cleaned transaction description"
  },
  "cols": 2,
  "rows": 23
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "New Affordability feature to surface external relationships (e.g. Latitude Loans) that are held externally to the bank accounts that have not been disclosed or linked by the user e.g. surfacing buy now pay later services. These are now represented now as external payments rather than living expenses. Identified external relationships are grouped under this new attribute `external`.",
  "title": "External Relationships"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "External",
    "0-0": "`source`",
    "0-1": "Source of external payment (cleaned transaction description).",
    "2-0": "`payments`",
    "2-1": "Aggregated attributes relating to payments for this source (identified as an external)",
    "6-1": "Each transaction (repeated for each source ordered by most recent):",
    "6-0": "`changeHistory`",
    "8-1": "* `amount` - amount of payment\n\n* `date`  - date  e.g. \"2019-03-15\"\n\n* `source` - full transaction description",
    "4-1": "* `first`  - date of first payment e.g. \"2019-03-15\"\n\n* `last` - date of last payment e.g. \"2020-03-15\"\n\n* `noOccurrences`  - number of occurrences for same source (in this group)\n\n* `amountAvg` - average amount of payment e.g. \"-50.50\"\n\n* `amountAvgMonthly` - average monthly payment amount e.g. \"-20.00\"\n\n* `total` - amount of total payments identified for source in the affordability snapshot e.g. \"-146.50\""
  },
  "cols": 2,
  "rows": 10
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Links",
    "2-0": "",
    "0-0": "`links`",
    "0-1": "A links object containing the following members:",
    "2-1": "- `self` - link to the affordability resource\n\n- `income` - [income](https://basiq.readme.io/v2.1/reference/income)\n\n- `expenses` - [expenses](https://basiq.readme.io/v2.1/reference/expenses)\n\n- `accounts` - an array of [accounts](ref:accounts) \nlinks"
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "You will need to create a user and create or refresh all connections before creating the affordability resource."
}
[/block]
**Returns**

Returns a created affordability resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"affordability\",\n  \"id\": \"s55bf3\",\n  \"fromMonth\": \"2019-03\",\n  \"toMonth\": \"2020-03\",\n  \"coverageDays\": 392,\n  \"generatedDate\": \"2020-03-26T06:56:44\",\n  \"summary\": {\n    \"assets\": \"59983.11\",\n    \"liabilities\": \"-323946.20\",\n    \"netPosition\": \"-263963.09\",\n    \"creditLimit\": \"20000.00\",\n    \"expenses\": \"-12046.00\",\n    \"savings\": \"93.00\",\n    \"regularIncome\": {\n      \"previous3Months\": {\n        \"avgMonthly\": \"18098.00\"\n      }\n    }\n  },\n  \"assets\": [\n    {\n      \"currency\": \"AUD\",\n      \"balance\": \"35298.67\",\n      \"availableFunds\": \"35298.67\",\n      \"institution\": \"Hooli\",\n      \"type\": \"account\",\n      \"account\": {\n        \"product\": \"Hooli Saver\",\n        \"type\": \"savings\"\n      },\n      \"previous6Months\": {\n        \"minBalance\": \"32427.79\",\n        \"maxBalance\": \"34798.67\"\n      }\n    },\n    {\n      \"currency\": \"AUD\",\n      \"balance\": \"24684.44\",\n      \"availableFunds\": \"24684.44\",\n      \"institution\": \"Hooli\",\n      \"type\": \"account\",\n      \"account\": {\n        \"product\": \"Hooli Transaction\",\n        \"type\": \"transaction\"\n      },\n      \"previous6Months\": {\n        \"minBalance\": \"10032.81\",\n        \"maxBalance\": \"38309.44\"\n      }\n    }\n  ],\n  \"liabilities\": {\n    \"loan\": [\n      {\n        \"currency\": \"AUD\",\n        \"balance\": \"-312233.00\",\n        \"availableFunds\": \"87767.00\",\n        \"institution\": \"Hooli\",\n        \"account\": {\n          \"type\": \"mortgage\",\n          \"product\": \"Hooli Home Loan\"\n        },\n        \"previousMonth\": {\n          \"totalCredits\": \"5768.00\",\n          \"totalDebits\": \"-4303.50\",\n          \"totalInterestCharged\": \"-4303.50\",\n          \"totalRepayments\": \"5768.00\"\n        },\n        \"changeHistory\": [\n          {\n            \"direction\": \"debit\",\n            \"amount\": \"-4220.75\",\n            \"date\": \"2019-03-19\",\n            \"source\": \"Mortgage Interest Payment 746833\"\n          },\n          {\n            \"direction\": \"credit\",\n            \"amount\": \"5768.00\",\n            \"date\": \"2019-03-31\",\n            \"source\": \"Transfer Platnm Homeloan 346454\"\n          },\n          {\n            \"direction\": \"debit\",\n            \"amount\": \"-4228.50\",\n            \"date\": \"2019-04-19\",\n            \"source\": \"Mortgage Interest Payment 746833\"\n          }\n        ],\n        \"previous6Months\": {\n          \"arrears\": false\n        }\n      }\n    ],\n    \"credit\": [\n      {\n        \"currency\": \"AUD\",\n        \"balance\": \"-11713.20\",\n        \"availableFunds\": \"8286.80\",\n        \"institution\": \"Hooli\",\n        \"creditLimit\": \"20000.00\",\n        \"account\": {\n          \"type\": \"credit-card\",\n          \"product\": \"Hooli Visa\"\n        },\n        \"previousMonth\": {\n          \"totalCredits\": \"0.00\",\n          \"totalDebits\": \"-8287.10\",\n          \"minBalance\": \"-3174.16\",\n          \"maxBalance\": \"-12329.16\"\n        },\n        \"previous6Months\": {\n          \"cashAdvances\": \"-2053.50\"\n        }\n      }\n    ]\n  },\n  \"external\": [\n    {\n      \"source\": \"afterpay\",\n      \"payments\": {\n        \"first\": \"2019-11-15\",\n        \"last\": \"2019-11-15\",\n        \"noOccurrences\": 2,\n        \"amountAvg\": \"-146.50\",\n        \"amountAvgMonthly\": \"-12.00\",\n        \"total\": \"-146.50\"\n      },\n      \"changeHistory\": [\n        {\n          \"amount\": \"-146.50\",\n          \"date\": \"2019-11-15\",\n          \"source\": \"AFTERPAY MELBOURNE VI AUS Card xx3854 Value Date: 10/11/2019\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/25c8d1ed77/affordability/s55bf3\",\n    \"income\": \"https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4\",\n    \"expenses\": \"https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5\",\n    \"accounts\": [\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08\",\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430\",\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089\",\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056\"\n    ]\n  }\n}",
      "language": "json",
      "name": "Example Affordability object"
    }
  ],
  "sidebar": true
}
[/block]