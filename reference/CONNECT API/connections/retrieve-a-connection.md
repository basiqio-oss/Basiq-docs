---
title: Retrieve a connection
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
Use this to retrieve details of a specific connection. This request will return back a connection object with most of the fields that were submitted when the connection was first created. The connection object will also return a list of URLs to the associated account, transaction and institution objects.

The status property of the connection object identifies the state of the connection. Use this to work out if the connection is still valid, or whether to take further action (e.g. if the connection credentials are no longer valid you may ask the user to re-submit their details).
[block:parameters]
{
  "data": {
    "0-0": "**id**\n*required*",
    "0-1": "The identifier of the connection to be retrieved.",
    "h-0": "Arguments"
  },
  "cols": 2,
  "rows": 1
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Note that due to security the loginId, password, securityCode are never returned."
}
[/block]
**Returns**

Returns a connection if a valid connection ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.
[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/connections/{connection.id}",
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
      "code": "GET /users/ea3a81/connections/8fce3b HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
      "language": "json",
      "name": "Example Request"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Profile data",
  "body": "Profile data represents the name, phone, email and address of the logged in user or data sharer.  Only data made available by institution can be returned. An institution may offer the option for a customer to hide all personal data or add 2FA to access the data - in this case no data would be returned for all data points.  Note, that when a Connection is deleted - the profile data will also be deleted. If a phone number or email address is masked by the institution - the string will be shown exactly as it is provided by the institution."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"connection\",\n  \"id\": \"8fce3b\",\n  \"status\": \"active\",\n  \"createdDate\": \"2020-10-02T05:53:05Z\",\n  \"lastUsed\": \"2020-12-02T02:21:02Z\",\n  \"profile\": {\n    \"fullName\": \"Max James\",\n    \"firstName\": \"Max\",\n    \"lastName\": \"James\",\n    \"middleName\": \"\",\n    \"phoneNumbers\": [\n      \"XXXX 888 991\"\n    ],\n    \"emailAddresses\": [\n      \"XXXXames@hotmail.com\"\n    ],\n    \"physicalAddresses\": [\n      {\n        \"addressLine1\": \"13/91 Fisher Rd\",\n        \"addressLine2\": null,\n        \"addressLine3\": null,\n        \"postcode\": \"2099\",\n        \"city\": null,\n        \"state\": \"NSW\",\n        \"country\": \"Australia\",\n        \"countryCode\": \"AU\",\n        \"formattedAddress\": \"13/91 Fisher Rd, Dee Why NSW 2099, Australia\"\n      }\n    ]\n  },\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"accounts\": {\n    \"type\": \"list\",\n    \"data\": [\n      {\n        \"type\": \"account\",\n        \"id\": \"s55bf3\",\n        \"accountNo\": \"105148119695\",\n        \"name\": \"Business account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"10.00\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n          \"type\": \"savings\",\n          \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')\"\n        }\n      },\n      {\n        \"type\": \"account\",\n        \"id\": \"ar36y2\",\n        \"accountNo\": \"533705985043\",\n        \"name\": \"Choice Account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"-10.09\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n          \"type\": \"savings\",\n          \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/ar36y2\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('ar36y2')\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n    \"accounts\": \"https://au-api.basiq.io/users/ea3a81/accounts?filter=institution.id.eq('AU00000')\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=institution.id.eq('AU00000')\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]