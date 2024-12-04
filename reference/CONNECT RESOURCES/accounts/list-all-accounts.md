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
Use this collection to retrieve a list of [accounts](https://basiq.readme.io/v1.0/reference#accounts). Each entry in the array is a separate account object.



**Returns**

Returns a list with a data property that contains an array of accounts. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v1.0/reference#errors) in the event of a failure.
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
      "code": "GETGET  /users/ea3a81/accounts/users/ea3a81/a  HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"data\": [\n    {\n      \"type\": \"account\",\n      \"id\": \"s55bf3\",\n      \"accountNo\": \"600000-157441965\",\n      \"name\": \"Master Savings\",\n      \"currency\": \"AUD\",\n      \"balance\": \"356.50\",\n      \"availableFunds\": \"420.28\",\n      \"lastUpdated\": \"2017-09-28T13:39:33.144Z\",\n      \"class\": {\n        \"type\": \"savings\",\n        \"product\": \"Saver\"\n      },\n      \"status\": \"available\",\n      \"institution\": \"AU00000\",\n      \"connection\": \"8fce3b\",\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n        \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')\",\n        \"connection\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n    {\n      \"type\": \"account\",\n      \"id\": \"s55bf4\",\n      \"accountNo\": \"600000-157441111\",\n      \"name\": \"Basiq loan\",\n      \"currency\": \"AUD\",\n      \"balance\": \"303000.50\",\n      \"availableFunds\": \"525.28\",\n      \"lastUpdated\": \"2017-09-28T13:39:33.144Z\",\n      \"class\": {\n        \"type\": \"mortgage\",\n        \"product\": \"Home Loan\",\n        \"meta\": {\n          \"accountNumber\": \"600000-157441111\",\n          \"availableRedraw\": \"5098.64\",\n          \"endDate\": \"12/01/25\",\n          \"fee\": \"Waived\",\n          \"instalmentAmount\": \"1768.23\",\n          \"interestRate\": \"4.8% p.a.\",\n          \"interestType\": \"Fixed rate\",\n          \"nextInstalmentDate\": \"22/02/18\",\n          \"offsetAccountNumber\": \"1098 5678\",\n          \"repaymentFrequency\": \"Weekly\",\n          \"repaymentType\": \"Interest only\"\n        }\n      },\n      \"status\": \"available\",\n      \"institution\": \"AU00000\",\n      \"connection\": \"8fce3b\",\n      \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf4\",\n        \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf4')\",\n        \"connection\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]