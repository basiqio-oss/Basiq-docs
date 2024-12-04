---
title: Create an affordability summary
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
Use this to create a new affordability summary for an individual user. 
[block:callout]
{
  "type": "warning",
  "body": "You will need to create a user and create or refresh all connections before creating the affordability resource."
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Arguments (body)",
    "0-0": "**fromMonth**\n*string, conditional*",
    "0-1": "the first/start month to be included in the affordability output e.g. \"fromMonth\":\"2019-05\". Resulting affordability resource will be based on data between fromMonth and toMonth",
    "1-0": "**toMonth**\n*string, conditional*",
    "1-1": "the last/end month to be included in the affordability output e.g. \"toMonth\":\"2019-09\". Resulting affordability resource will be based on data between fromMonth and toMonth",
    "2-0": "",
    "2-1": "e.g. of body text\n{\n    \"fromMonth\":\"2019-05\",\n    \"toMonth\":\"2019-09\"\n}",
    "6-0": "",
    "3-0": "**accounts**\n*array, conditional*",
    "3-1": "an array of account ids",
    "4-1": "e.g. of body text\n\n{\n  \"accounts\": [\n    \"20024b08\",\n    \"64880430\"\n  ]\n}"
  },
  "cols": 2,
  "rows": 6
}
[/block]
If the **optional** arguments (above) are not specified then the affordability resource will be created for the default dates: 13 months ago until current month and the resource is created for all accounts under the user if none are specified as arguments. **All transactions in non-specified accounts are ignored.**

**Returns**

Returns a created affordability resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:callout]
{
  "type": "info",
  "body": "The affordability API returns a JSON response by default however you can specify to return a PDF report version of the affordability summary (examples below)",
  "title": "PDF response also available"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n",
      "language": "json",
      "name": "Create affordability"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/25c8d1ed77/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n",
      "language": "json",
      "name": "Create affordability"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/25c8d1ed77/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n{\n  \"fromMonth\":\"2020-07\",\n  \"toMonth\":\"2020-11\",\n  \"accounts\": [\n    \"20024b08\",\n    \"64880430\",\n    \"55bf3089\",\n    \"6jk43056\"\n  ]\n} \n",
      "language": "json",
      "name": "Create affordability - filter by specified accounts and report period"
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
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]
**Returns PDF Report**

Returns a created affordability PDF Report, if the operation succeeded. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nAccept: application/pdf",
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
      "code": "POST /users/25c8d1ed77/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nAccept: application/pdf",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]