---
title: Connections
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
The connection object is created whenever a user links their financial institution with your app. Once a connection is successfully created - you can use it to obtain the user's latest financial data i.e. accounts and transactions.
After a connection is successfully established, you can fetch data created after this point by [refreshing](https://basiq.readme.io/v1.0/reference#refresh-a-connection) the connection. This process ensures on-demand data syncronization between your system and Institution itself.
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-0": "**type**\n*string, read-only*",
    "0-1": "Value is \"connection\".",
    "1-0": "**id**\n*string, read-only*",
    "1-1": "A string that uniquely identifies the user connection.",
    "2-0": "**loginId**\n*string, required*",
    "2-1": "User's institution login ID. This value cannot be read.",
    "3-0": "**password**\n*string, required*",
    "3-1": "User's institution password. This value cannot be read.",
    "4-0": "**securityCode**\n*string, conditional*",
    "4-1": "User's institution security code. This value cannot be read.",
    "5-0": "**secondaryLoginId**\n*string, conditional*",
    "5-1": "User's institution secondary login id. This value cannot be read.",
    "6-0": "**status**\n*enum, read-only* ",
    "6-1": "Indicates the connection status. Possible values include:\n- `active` the connection is valid (is working!)\n- `invalid` the connection is no longer valid and requires the user to update their logon details",
    "7-1": "UTC Date and Time of when the connection was last used, in RFC 3339 format.",
    "8-1": "The institution the connection relates to.",
    "9-1": "User's accounts in this institution.",
    "10-1": "A links object containing the following members:\n- `self` link to the requested connection\n- `accounts` link to the accounts associated with this connection\n- `transactions` link to the transactions associated with this connection",
    "7-0": "**lastUsed**\n*string, optional*",
    "8-0": "[**institution**](https://basiq.readme.io/v1.0/reference#institutions)\n*object, read-only*",
    "9-0": "**[accounts](https://basiq.readme.io/v1.0/reference#accounts)**\n*list of objects, read-only*",
    "10-0": "**links**\n*object, read-only*"
  },
  "cols": 2,
  "rows": 11
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "To minimise the exposure of credential details, loginId, password and securityCode are omitted from all server responses."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"connection\",\n  \"id\": \"8fce3b\",\n  \"loginId\": ...,\n  \"password\": ...,\n  \"status\": \"active\",\n  \"lastUsed\": \"2017-09-28T11:15:09Z\",\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"accounts\": {\n    \"type\": \"list\",\n    \"data\": [\n      {\n        \"type\": \"account\",\n        \"id\": \"s55bf3\",\n        \"accountNo\": \"105148119695\",\n        \"name\": \"Business account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"10.00\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')'\"\n        }\n      },\n      {\n        \"type\": \"account\",\n        \"id\": \"ar36y2\",\n        \"accountNo\": \"533705985043\",\n        \"name\": \"Choice Account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"-10.09\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/ar36y2\",\n          \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('ar36y2')\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n    \"accounts\": \"https://au-api.basiq.io/users/ea3a81/accounts?filter=connection.id.eq('8fce3b')\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=connection.id.eq('8fce3b')\"\n  }\n}",
      "language": "json",
      "name": "Example Connection Object"
    }
  ],
  "sidebar": true
}
[/block]