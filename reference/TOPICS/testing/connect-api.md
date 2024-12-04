---
title: Connect API
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
The test data that we provide for the Connect API service (below) has been designed to mimic a real life user. This means that just a like a real user would spend and receive funds throughout the day - our test accounts have been designed to do the same thing. Therefore you should expect to see new transaction records being created throughout the day, and the account balances adjusted accordingly.

This should give you a good feel for the type of data that you should expect to see for your own customers. The transaction data is completely random, and even we are sometimes surprised by transactions that appear :-)
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
    "0-0": "gavinBelson",
    "0-1": "hooli2016"
  },
  "cols": 2,
  "rows": 1
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/ea3a81/connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN                                           \nContent-Type: application/json\n\n{\n  \"loginId\": \"gavinBelson\",\n  \"password\": \"hooli2016\",\n  \"externalUserId\": \"01\",\n  \"institution\":{\n    \"id\":\"AU00000\"\n  }\n}",
      "language": "json",
      "name": "Create Connection (using test account)"
    }
  ],
  "sidebar": true
}
[/block]