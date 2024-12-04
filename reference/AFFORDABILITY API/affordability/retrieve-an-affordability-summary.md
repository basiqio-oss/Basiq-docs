---
title: Retrieve an affordability summary
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
[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "0-0": "**id**\n*required*",
    "0-1": "A string that uniquely identifies the affordability summary as a resource",
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
  "body": "You will need an affordability id from an object you have created to retrieve an affordability object."
}
[/block]
**Returns**

Returns a created affordability resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:callout]
{
  "type": "info",
  "title": "PDF Response also available",
  "body": "The affordability API returns a JSON response by default however you can specify to return a PDF report version of the affordability summary (examples below)"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/affordability/{afforability.id} HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nAccept: application/json\n\n\n",
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
      "code": "GET /users/25c8d1ed77/affordability/s55bf3 HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nAccept: application/json",
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
      "code": "HTTP/1.11.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"affordability\",\n  \"id\": \"s55bf3\",\n  \"fromMonth\": \"2019-03\",\n  \"toMonth\": \"2020-03\",\n  \"coverageDays\": 392,\n  \"generatedDate\": \"2020-03-26T06:56:44\",\n  \"summary\": {\n    \"assets\": \"59983.11\",\n    \"liabilities\": \"-323946.20\",\n    \"netPosition\": \"-263963.09\",\n    \"creditLimit\": \"20000.00\",\n    \"expenses\": \"-12046.00\",\n    \"savings\": \"93.00\",\n    \"regularIncome\": {\n      \"previous3Months\": {\n        \"avgMonthly\": \"18098.00\"\n      }\n    }\n  },\n  \"assets\": [\n    {\n      \"currency\": \"AUD\",\n      \"balance\": \"35298.67\",\n      \"availableFunds\": \"35298.67\",\n      \"institution\": \"Hooli\",\n      \"type\": \"account\",\n      \"account\": {\n        \"product\": \"Hooli Saver\",\n        \"type\": \"savings\"\n      },\n      \"previous6Months\": {\n        \"minBalance\": \"32427.79\",\n        \"maxBalance\": \"34798.67\"\n      }\n    },\n    {\n      \"currency\": \"AUD\",\n      \"balance\": \"24684.44\",\n      \"availableFunds\": \"24684.44\",\n      \"institution\": \"Hooli\",\n      \"type\": \"account\",\n      \"account\": {\n        \"product\": \"Hooli Transaction\",\n        \"type\": \"transaction\"\n      },\n      \"previous6Months\": {\n        \"minBalance\": \"10032.81\",\n        \"maxBalance\": \"38309.44\"\n      }\n    }\n  ],\n  \"liabilities\": {\n    \"loan\": [\n      {\n        \"currency\": \"AUD\",\n        \"balance\": \"-312233.00\",\n        \"availableFunds\": \"87767.00\",\n        \"institution\": \"Hooli\",\n        \"account\": {\n          \"type\": \"mortgage\",\n          \"product\": \"Hooli Home Loan\"\n        },\n        \"previousMonth\": {\n          \"totalCredits\": \"5768.00\",\n          \"totalDebits\": \"-4303.50\",\n          \"totalInterestCharged\": \"-4303.50\",\n          \"totalRepayments\": \"5768.00\"\n        },\n        \"changeHistory\": [\n          {\n            \"direction\": \"debit\",\n            \"amount\": \"-4220.75\",\n            \"date\": \"2019-03-19\",\n            \"source\": \"Mortgage Interest Payment 746833\"\n          },\n          {\n            \"direction\": \"credit\",\n            \"amount\": \"5768.00\",\n            \"date\": \"2019-03-31\",\n            \"source\": \"Transfer Platnm Homeloan 346454\"\n          },\n          {\n            \"direction\": \"debit\",\n            \"amount\": \"-4228.50\",\n            \"date\": \"2019-04-19\",\n            \"source\": \"Mortgage Interest Payment 746833\"\n          }\n        ],\n        \"previous6Months\": {\n          \"arrears\": false\n        }\n      }\n    ],\n    \"credit\": [\n      {\n        \"currency\": \"AUD\",\n        \"balance\": \"-11713.20\",\n        \"availableFunds\": \"8286.80\",\n        \"institution\": \"Hooli\",\n        \"creditLimit\": \"20000.00\",\n        \"account\": {\n          \"type\": \"credit-card\",\n          \"product\": \"Hooli Visa\"\n        },\n        \"previousMonth\": {\n          \"totalCredits\": \"0.00\",\n          \"totalDebits\": \"-8287.10\",\n          \"minBalance\": \"-3174.16\",\n          \"maxBalance\": \"-12329.16\"\n        },\n        \"previous6Months\": {\n          \"cashAdvances\": \"-2053.50\"\n        }\n      }\n    ]\n  },\n  \"external\": [\n    {\n      \"source\": \"afterpay\",\n      \"payments\": {\n        \"first\": \"2019-11-15\",\n        \"last\": \"2019-11-15\",\n        \"noOccurrences\": 2,\n        \"amountAvg\": \"-146.50\",\n        \"amountAvgMonthly\": \"-12.00\",\n        \"total\": \"-146.50\"\n      },\n      \"changeHistory\": [\n        {\n          \"amount\": \"-146.50\",\n          \"date\": \"2019-11-15\",\n          \"source\": \"AFTERPAY MELBOURNE VI AUS Card xx3854 Value Date: 10/11/2019\"\n        },\n        {\n          ...\n        }\n      ]\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/25c8d1ed77/affordability/s55bf3\",\n    \"income\": \"https://au-api.basiq.io/users/25c8d1ed77/income/s55bf4\",\n    \"expenses\": \"https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5\",\n    \"accounts\": [\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08\",\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430\",\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089\",\n      \"https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056\"\n    ]\n  }\n}",
      "language": "json",
      "name": "Example Reponse"
    }
  ],
  "sidebar": true
}
[/block]