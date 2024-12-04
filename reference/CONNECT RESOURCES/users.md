---
title: Users
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
The user object represents an end-user of your application. This object encapsulates all of the financial details of an individual (such as list of accounts and transactions) along with the relationships that they hold with each institution (i.e. connections).

Use this object to keep your list of users in sync with the Basiq server. Once a user ceases to use your application, it is strongly recommended that the user object is deleted.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-1": "Value is \"user\".",
    "0-0": "**type**\n*readonly*",
    "1-1": "A string that uniquely identifies the user.",
    "1-0": "**id**\n*readonly*",
    "2-0": "**email**\n*string, conditional*",
    "2-1": "The end-users email address.",
    "3-0": "**mobile**\n*string, conditional*",
    "3-1": "The end-users mobile number."
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"user\",\n  \"id\": \"ea3a81\",\n  \"email\": \"gavin@hooli.com\",\n  \"mobile\": \"+61410888666\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81\"\n  }\n}",
      "language": "json",
      "name": "Example User Object"
    }
  ],
  "sidebar": true
}
[/block]