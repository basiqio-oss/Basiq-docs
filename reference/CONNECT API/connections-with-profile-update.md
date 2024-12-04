---
title: Connections with profile update
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
The connection object is created whenever a user links their financial institution with your app. Connections act as conduits that retrieve account holders' data (i.e. accounts and transactions) from the institution and store it against the User object. Connections can be deleted and recreated so it is recommended that apps access accounts via the User object rather than the connection.

After a connection is successfully established, you can fetch data created after this point by refreshing the connection. This process ensures on-demand data synchronization between your system and Institution itself. Basiq recommends using the Scheduler if connections are to be refreshed multiple times per day.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "`type`",
    "0-1": "Value is \"connection\".",
    "2-0": "`id`",
    "2-1": "A string that uniquely identifies the user connection.",
    "4-0": "`loginId`",
    "4-1": "User's institution login ID. This value cannot be read.  *required*",
    "6-0": "`password`",
    "6-1": "User's institution password. This value cannot be read. *required*",
    "8-0": "`securityCode`",
    "8-1": "User's institution security code. This value cannot be read. *conditional*",
    "10-0": "`secondaryLoginId`",
    "10-1": "User's institution secondary login id. This value cannot be read. *conditional*",
    "12-0": "`status`",
    "12-1": "Indicates the connection status. Possible values include:",
    "16-1": "UTC Date and Time of when the connection was last used, in RFC 3339 format.",
    "20-1": "The institution the connection relates to.",
    "22-1": "User's accounts in this institution.",
    "24-1": "A links object containing the following members:",
    "16-0": "`lastUsed`",
    "20-0": "[**institution**](https://basiq.readme.io/v2.0/reference#institutions)",
    "22-0": "**[accounts](https://basiq.readme.io/v2.0/reference#accounts)**",
    "24-0": "**links**",
    "14-1": "- `active` the connection is valid (is working!)\n\n- `invalid` the connection is no longer valid and requires the user to update their logon details",
    "26-1": "- `self` link to the requested connection\n\n- `accounts` link to the accounts associated with this connection\n- `transactions` link to the transactions associated with this connection",
    "18-0": "`profile`",
    "18-1": "Profile data relating to the login used to access the institution. Does not apply to PDF or CSV upload connections"
  },
  "cols": 2,
  "rows": 28
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "To minimise the exposure of credential details, loginId, password and securityCode are omitted from all server responses."
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "profile data",
  "body": "The profile attribute is not populated for all institutions. This data is exposed only when available from the institution. Applies only to direct connections to institutions and not to statement uploads."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"connection\",\n  \"id\": \"8fce3b\",\n  \"loginId\": ...,\n  \"password\": ...,\n  \"status\": \"active\",\n  \"lastUsed\": \"2017-09-28T11:15:09Z\",\n  \"profile\": {\n        \"fullName\": \"Test User\",\n        \"firstName\": \"Test\",\n        \"lastName\": \"User\",\n        \"middleName\": \"\",\n        \"phoneNumbers\": [],\n        \"emailAddresses\": [],\n        \"physicalAddresses\": [\n            {\n                \"addressLine1\": \"1 SMITH STREET, Sydney, NSW, 2000\",\n                \"addressLine2\": null,\n                \"addressLine3\": null,\n                \"postcode\": \"2000\",\n                \"city\": \"Sydney\",\n                \"state\": \"NSW\",\n                \"country\": \"Australia\",\n                \"countryCode\": \"AU\",\n                \"formattedAddress\": \"1 Smith Street, Sydney NSW 2000, Australia\"\n            }\n        ]\n  },\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"accounts\": {\n    \"type\": \"list\",\n    \"data\": [\n      {\n        \"type\": \"account\",\n        \"id\": \"s55bf3\",\n        \"accountNo\": \"105148119695\",\n        \"name\": \"Business account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"10.00\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')'\"\n        }\n      },\n      {\n        \"type\": \"account\",\n        \"id\": \"ar36y2\",\n        \"accountNo\": \"533705985043\",\n        \"name\": \"Choice Account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"-10.09\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/ar36y2\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('ar36y2')\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n    \"accounts\": \"https://au-api.basiq.io/users/ea3a81/accounts?filter=institution.id.eq('AU00000')\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=institution.id.eq('AU00000')\"\n  }\n}",
      "language": "json",
      "name": "Example Connection Object"
    }
  ],
  "sidebar": true
}
[/block]