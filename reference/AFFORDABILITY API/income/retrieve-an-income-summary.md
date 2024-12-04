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
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**id**\n*required*",
    "0-1": "A string that uniquely identifies the income summary as a resource",
    "3-0": "`totalLiabilities`",
    "3-1": "Total account based liabilities identified as credits, overdrafts or loans for a single customer",
    "5-0": "",
    "5-1": ""
  },
  "cols": 2,
  "rows": 2
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "You will need an income id from an object you have created to retrieve an income object."
}
[/block]
**Returns**

Returns a created income resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/income/{income.id} HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n\n",
      "language": "json",
      "name": "Definition"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/25c8d1ed77/income/s55bf4 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json",
      "language": "json"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.11.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"income\",\n  \"id\": \"s55bf4\",\n  \"fromMonth\": \"2018-11\",\n  \"toMonth\": \"2019-11\",\n  \"coverageDays\": 394,\n  \"generatedDate\": \"2019-12-10T05:49:15\",\n  \"summary\": {\n    \"regularIncomeAvg\": \"18098.00\",\n    \"regularIncomeYTD\": \"90490.00\",\n    \"regularIncomeYear\": \"217176.00\",\n    \"irregularIncomeAvg\": \"55.00\"\n  },\n  \"regular\": [\n    {\n      \"source\": \"payroll wfrms 15439393\",\n      \"frequency\": \"monthly\",\n      \"ageDays\": 334,\n      \"irregularity\": {\n        \"stability\": \"1.00\",\n        \"gaps\": []\n      },\n      \"previous3Months\": {\n        \"amountAvg\": \"18098.00\",\n        \"amountAvgMonthly\": \"18098.00\",\n        \"variance\": \"0.00\"\n      },\n      \"current\": {\n        \"date\": \"2018-11-30T09:23:37\",\n        \"amount\": \"18098.00\",\n        \"nextDate\": \"2018-12-30T18:30:49\"\n      },\n      \"changeHistory\": [\n        {\n          \"source\": \"Payroll WFRMS 15439393\",\n          \"date\": \"2018-11-30T09:23:37\",\n          \"amount\": \"18098.00\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"irregular\": [\n    {\n      \"source\": \"ctrlink carers 998r6789201610974v\",\n      \"frequency\": \"irregular\",\n      \"ageDays\": 253,\n      \"amountAvg\": \"55.00\",\n      \"noOccurrences\": 5,\n      \"avgMonthlyOccurence\": \"1\",\n      \"current\": {\n        \"date\": \"2018-10-13T20:03:37\",\n        \"amount\": \"62.00\"\n      },\n      \"changeHistory\": [\n        {\n          \"source\": \"CTRLINK CARERS Ref: 998R6789201610974V\",\n          \"date\": \"2018-10-13T20:03:37\",\n          \"amount\": \"62.00\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"otherCredit\": [\n    {\n      \"source\": \"savings interest cr bal - Account 1\",\n      \"frequency\": \"monthly\",\n      \"ageDay\": 335,\n      \"amountAvg\": \"110.85\",\n      \"noOccurrences\": 12,\n      \"avgMonthlyOccurence\": \"1\",\n      \"current\": {\n        \"date\": \"2019-10-29T00:00:00\",\n        \"amount\": \"92.99\",\n        \"otherCreditLabel\": \"regular income small amount\"\n      },\n      \"changeHistory\": [\n        {\n          \"source\": \"savings interest cr bal - Account 1\",\n          \"date\": \"2018-10-13T20:03:37\",\n          \"amount\": \"62.00\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4\",\n    \"accounts\": [\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056\"\n     ]\n  }\n}\n    ",
      "language": "json",
      "name": "Example Reponse"
    }
  ],
  "sidebar": true
}
[/block]