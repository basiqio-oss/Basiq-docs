---
title: List all accounts
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
Use this collection to retrieve a list of [accounts](https://basiq.readme.io/v2.0/reference#accounts). Each entry in the array is a separate account object.
[block:parameters]
{
  "data": {
    "0-0": "**[filter](https://basiq.readme.io/v2.1/reference/accounts)**\n*string, optional*",
    "0-1": "This list can be [filtered](https://basiq.readme.io/v2.1/reference/filters) by the following properties:\n\n- `account.id`\n\n- `connection.id`\n\n- `institution.id`\n\nOnly equals (eq) and not equals (ne) operations are currently supported."
  },
  "cols": 2,
  "rows": 1
}
[/block]
**Returns**

Returns a list with a data property that contains an array of accounts. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v2.1/reference/errors) in the event of a failure.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/accounts",
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
      "code": "GET  /users/ea3a81/accounts  HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"data\": [\n    {\n      \"type\": \"account\",\n      \"id\": \"2682e4bf\",\n      \"accountNo\": \"12345612345678\",\n      \"name\": \"Mortgage 746833\",\n      \"currency\": \"AUD\",\n      \"class\": {\n        \"type\": \"mortgage\",\n        \"product\": \"Hooli Home Loan\",\n        \"meta\": {\n          \"accountNumber\": \"12345612345678\",\n          \"availableRedraw\": \"200.00\",\n          \"endDate\": \"2040-01-13T08:00:00.000Z\",\n          \"fee\": \"300.00\",\n          \"instalmentAmount\": null,\n          \"interestRate\": null,\n          \"interestType\": \"variable\",\n          \"nextInstalmentDate\": \"2021-02-01T00:00:00.000Z\",\n          \"offsetAccountNumber\": \"12-999-000\",\n          \"repaymentFrequency\": \"monthly\",\n          \"repaymentType\": \"interest and principal\"\n        }\n      },\n      \"balance\": \"-367576.75\",\n      \"availableFunds\": \"32423.25\",\n      \"lastUpdated\": \"2021-01-19T04:17:17Z\",\n      \"transactionIntervals\": [\n        {\n          \"from\": \"2019-04-30\",\n          \"to\": \"2021-01-19\"\n        }\n      ],\n      \"institution\": \"AU00000\",\n      \"accountHolder\": \"Max Wentworth-Smith & Paul Wentworth-Smith\",\n      \"connection\": \"575f762e\",\n      \"status\": \"available\",\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/bf3399fg0/accounts/2682e4bf\",\n        \"transactions\": \"https://au-api.basiq.io/users/bf3399fg0/transactions?filter=account.id.eq('2682e4bf)\",\n        \"connection\": null,\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n    {\n      \"type\": \"account\",\n      \"id\": \"99bd6065\",\n      \"accountNo\": \"23456723456789\",\n      \"name\": \"Credit Card 13000\",\n      \"currency\": \"AUD\",\n      \"class\": {\n        \"type\": \"credit-card\",\n        \"product\": \"Hooli Visa\"\n      },\n      \"balance\": \"10260.81\",\n      \"availableFunds\": \"30260.81\",\n      \"lastUpdated\": \"2021-01-19T04:17:17Z\",\n      \"transactionIntervals\": [\n        {\n          \"from\": \"2019-05-13\",\n          \"to\": \"2021-01-19\"\n        }\n      ],\n      \"institution\": \"AU00000\",\n      \"accountHolder\": \"Max Wentworth-Smith\",\n      \"connection\": \"575f762e\",\n      \"status\": \"available\",\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/bf3399fg0/accounts/99bd6065\",\n        \"transactions\": \"https://au-api.basiq.io/users/bf3399fg0/transactions?filter=account.id.eq('99bd6065')\",\n        \"connection\": null,\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/bf3399fg0/accounts\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]