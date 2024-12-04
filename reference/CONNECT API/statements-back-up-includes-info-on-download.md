---
title: Statements - back up - includes info on download
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
The statement object represents an official bank statement for an account or accounts held with a financial institution (e.g. a savings account). You can use this object to **retrieve** official bank statements downloaded from a financial institution for which you have created a connection.  Alternatively, you can **create** a statement object by uploading official pdf bank statements which are parsed to extract and expose the user's latest account and transaction data. 
[block:callout]
{
  "type": "info",
  "title": "Download Bank Statements from Created Connection",
  "body": "When a new Connection request is made, the server will [create a job](https://basiq.readme.io/v2.0/reference#jobs) that will process an additional step to download the most recent bank statement for each account held by the user."
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Upload Official Bank Statements by Creating a Statement resource",
  "body": "When a new Statement request is made, the server will [create a job](https://basiq.readme.io/v2.0/reference#jobs) that will processes 3 steps verify the file, retrieve accounts and transactions"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "`type`",
    "0-1": "Value is \"statement\".",
    "2-0": "`id`",
    "2-1": "A string that uniquely identifies the statement.",
    "4-1": "A links object containing the following members for this statement:",
    "8-1": "- **[accounts](https://basiq.readme.io/v2.0/reference#accounts)**  All accounts or a single user account extracted from this statement.",
    "10-1": "A links object containing the following members:",
    "4-0": "**links**",
    "8-0": "",
    "10-0": "**links**",
    "12-1": "- `self` link to the list of **all** statements for this user",
    "6-1": "- `self` link to the this **single** bank statement"
  },
  "cols": 2,
  "rows": 14
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"list\",\n    \"data\": [\n        {\n            \"type\": \"statement\",\n            \"id\": \"1a73e\",\n            \"links\": {\n                \"self\": \"/users/ea3a81/statements/1a73e\",\n                \"account\": \"/users/ea3a81/accounts/e40f6\"\n            }\n        }\n    ],\n    \"links\": {\n        \"self\": \"/users/ea3a81/statements\"\n    }\n}",
      "language": "json",
      "name": "Example Statements Object"
    }
  ],
  "sidebar": true
}
[/block]