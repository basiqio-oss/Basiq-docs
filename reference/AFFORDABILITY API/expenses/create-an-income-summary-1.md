---
title: Create an expense summary
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
Use this to create a new expense summary for an individual user. 
[block:callout]
{
  "type": "warning",
  "body": "You will need to create a user and create or refresh all connections before creating the expenses resource."
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Arguments (body)",
    "0-0": "**fromMonth**\n*string, conditional*",
    "0-1": "the first/start month to be included in the expense output e.g. \"fromMonth\":\"2019-05\". Resulting income resource will be based on data between fromMonth and toMonth",
    "1-0": "**toMonth**\n*string, conditional*",
    "1-1": "the last/end month to be included in the expense output e.g. \"toMonth\":\"2019-09\". Resulting income resource will be based on data between fromMonth and toMonth",
    "2-1": "e.g. of body text\n{\n\"fromMonth\":\"2019-05\",\n\"toMonth\":\"2019-09\"\n}",
    "3-0": "**accounts**\n*array, conditional*",
    "3-1": "an array of account ids",
    "4-1": "e.g. of body text\n\n{\n  \"accounts\": [\n    \"20024b08\",\n    \"64880430\"\n  ]\n}"
  },
  "cols": 2,
  "rows": 6
}
[/block]
If the **optional** arguments (above) are not specified then the expense resource will be created for the default dates: 13 months ago until current month and the resource is created for all accounts under the user if none are specified as arguments.  **All transactions in non-specified accounts are ignored.**

**Returns**

Returns a created expenses resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/expenses HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n\n",
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
      "code": "POST /users/25c8d1ed77/expenses HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.11.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"expenses\",\n  \"id\": \"s55bf5\",\n  \"fromMonth\": \"2017-12\",\n  \"toMonth\": \"2018-12\",\n  \"payments\": [\n    {\n      \"division\": \"Alcoholic beverages\",\n      \"avgMonthly\": \"-850.00\",\n      \"percentageTotal\": 13.41,\n      \"subCategory\": [\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"0401000101\",\n              \"classTitle\": \"Alcoholic beverages nfd for consumption off licensed premises\",\n              \"divisionCode\": \"04\",\n              \"divisionTitle\": \"Alcoholic beverages\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-07\",\n              \"amount\": \"-2173.00\"\n            },\n            {\n              ...\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"division\": \"Food and non-alcoholic beverages\",\n      \"avgMonthly\": \"-1933.00\",\n      \"percentageTotal\": 30.5,\n      \"subCategory\": [\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"0311010202\",\n              \"classTitle\": \"Fast food and takeaway exc. coffee (not frozen)\",\n              \"divisionCode\": \"03\",\n              \"divisionTitle\": \"Food and non-alcoholic beverages\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-06\",\n              \"amount\": \"-183.00\"\n            },\n            {\n              ...\n            }\n          ]\n        },\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"0300000000\",\n              \"classTitle\": \"Food and non-alcoholic beverages nfd\",\n              \"divisionCode\": \"03\",\n              \"divisionTitle\": \"Food and non-alcoholic beverages\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-06\",\n              \"amount\": \"-682.00\"\n            },\n            {\n              ...\n            },\n          ]\n        }\n      ]\n    },\n    {\n      \"division\": \"Transport\",\n      \"avgMonthly\": \"-3553.00\",\n      \"percentageTotal\": 56.08,\n      \"subCategory\": [\n        {\n          \"summary\": \"monthly\",\n          \"category\": {\n            \"expenseClass\": {\n              \"classCode\": \"1001030101\",\n              \"classTitle\": \"Petrol\",\n              \"divisionCode\": \"10\",\n              \"divisionTitle\": \"Transport\"\n            }\n          },\n          \"changeHistory\": [\n            {\n              \"date\": \"2019-06\",\n              \"amount\": \"-2577.00\"\n            },\n            {\n              ...\n            }\n          ]\n        }\n      ]\n    }\n  ],\n  \"cashWithdrawals\": {\n    \"avgMonthly\": \"-913.14\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-240.00\"\n      },\n      {\n        ...\n      }\n    ]\n  },\n  \"bankFees\": {\n    \"avgMonthly\": \"-30.69\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-3550.25\"\n      },\n      {\n       ...\n      }\n    ]\n  },\n  \"externalTransfers\": {\n    \"avgMonthly\": \"-300.00\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-1000.00\"\n      },\n      {\n        ...\n      }\n    ]\n  },\n  \"loanInterests\": {\n    \"avgMonthly\": \"-4226.00\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n      \"date\": \"2018-06\",\n      \"amount\": \"-1000.00\"\n      },\n      {\n        ...\n      }\n    ]\n  },\n  \"loanRepayments\": {\n    \"avgMonthly\": \"5658.00\",\n    \"summary\": \"monthly\",\n    \"changeHistory\": [\n      {\n        \"date\": \"2018-06\",\n        \"amount\": \"-1000.00\"\n      },\n      {\n        ...\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/25c8d1ed77/expenses/s55bf5\",\n    \"accounts\": [\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/20024b08\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/64880430\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/55bf3089\",\n         \"https://au-api.basiq.io/users/25c8d1ed77/accounts/6jk43056\"\n     ]\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]