---
title: Affordability API
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
The test data that we provide for the Affordability API service has been designed to mimic a real life user. This means that just a like a real user would spend and receive funds throughout the day - our test accounts have been designed to do the same thing. Therefore you should expect to see new transaction records being created throughout the day, and the account balances adjusted accordingly.

[block:callout]
{
  "type": "warning",
  "body": "You can use our sandbox environment for free - contact us (via the \"help\" icon at the bottom of the page) to have your API key activated for Affordability."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Ensure that you pass the institution code AU00000 when using the test accounts"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "loginId",
    "h-1": "password",
    "0-0": "Wentworth-Smith",
    "0-1": "whislter"
  },
  "cols": 2,
  "rows": 1
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/ea3a81/connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN                                           \nContent-Type: application/json\n\n{\n \"loginId\": \"Wentworth-Smith\",\n \"password\": \"whislter\",\n \"institution\":{\n   \"id\":\"AU00000\"\n }\n}",
      "language": "json",
      "name": "Create Connection (using test account)"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "success",
  "body": "Once you have created a test connection you can access the Affordability, Income and Expense endpoints for this user.  The Affordability endpoint returns links to Income and Expense resources or you can use these endpoints independently without Affordability."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/affordability HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n",
      "language": "json",
      "name": "Definitions"
    }
  ],
  "sidebar": true
}
[/block]