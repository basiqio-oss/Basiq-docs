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
The connection object is created whenever a user links their financial institution with your app. Connections act as conduits that retrieve account holders' data (i.e. accounts and transactions) from the institution and store it against the User object. Connections can be deleted and recreated so it is recommended that apps access accounts via the User object rather than the connection.

After a connection is successfully established, you can fetch data created after this point by refreshing the connection. This process ensures on-demand data synchronization between your system and Institution itself. Basiq recommends using the Smart Cache to ensure you always have access to the latest data.
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
    "18-1": "UTC Date and Time the connection was last used, in RFC 3339 format.",
    "26-1": "The institution the connection relates to.",
    "28-1": "User's accounts in this institution.",
    "30-1": "A links object containing the following members:",
    "18-0": "`lastUsed`",
    "26-0": "[**institution**](https://basiq.readme.io/v2.0/reference/institutions)",
    "28-0": "**[accounts](https://basiq.readme.io/v2.0/reference/accounts)**",
    "30-0": "**links**",
    "14-1": "- `pending` the connection is in this status briefly until credentials are verified\n\n- `active` the connection is valid (is working!) and the credentials have been verified (the jobs steps will continue)\n\n- `invalid` the connection is no longer valid and requires the user to update their logon details.  Invalid connections cannot refreshed until the password is updated.",
    "32-1": "- `self` link to the requested connection\n\n- `accounts` link to the accounts associated with this connection\n- `transactions` link to the transactions associated with this connection",
    "22-0": "`profile`",
    "22-1": "Available profile data for the logged in user or data sharer.  Where no data is available the attribute is \"null\". This attribute contains the following properties and will return \"null\" for data that is unavailable:",
    "24-1": "- `fullName`\n\n- `firstName`\n\n- `lastName`\n\n- `middleName`\n\n- `phoneNumbers` - a collection of phone numbers\n\n- `emailAddresses` - a collection of email addresses\n\n- `physicalAddresses` - a collection of addresses\n         - `addressLine1`\n         - `addressLine2`\n         - `addressLine3`\n         - `postcode`\n         - `city`\n         - `state`\n         - `country`\n         - `countryCode`\n         - `formattedAddress` - full address as a string",
    "16-0": "`createdDate`",
    "16-1": "UTC Date and Time the connection was created, in RFC 3339 format.",
    "20-0": "`mfaEnabled`",
    "20-1": "**[new]** Indicates whether MFA (multi factor authentication) is enabled for this connection. Where the value is `true` then expect an additional step in the [Jobs](ref:jobs) response. Otherwise value is `false`."
  },
  "cols": 2,
  "rows": 34
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n{\n    \"type\": \"connection\",\n    \"id\": \"c7231718\",\n    \"status\": \"active\",\n    \"createdDate\": \"2020-12-02T02:20:49Z\",\n    \"lastUsed\": \"2020-12-02T02:20:59Z\",\n    \"mfaEnabled\": false,\n    \"profile\": {\n        \"fullName\": \"Max Wentworth-Smith\",\n        \"firstName\": \"Max\",\n        \"lastName\": \"Wentworth-Smith\",\n        \"middleName\": \"\",\n        \"phoneNumbers\": [\n            \"040534555 ### 991\"\n        ],\n        \"emailAddresses\": [\n            \"maxsmith@gmail.com\"\n        ],\n        \"physicalAddresses\": [\n            {\n                \"addressLine1\": \"91 Fisher Road\",\n                \"addressLine2\": null,\n                \"addressLine3\": null,\n                \"postcode\": \"2099\",\n                \"city\": \"Dee Why\",\n                \"state\": \"NSW\",\n                \"country\": \"Australia\",\n                \"countryCode\": \"AU\",\n                \"formattedAddress\": \"13/91 Fisher Rd, Dee Why NSW 2099, Australia\"\n            }\n        ]\n    },\n    \"institution\": {\n        \"type\": \"institution\",\n        \"id\": \"AU00000\",\n        \"links\": {\n            \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n        }\n    },\n    \"accounts\": {\n        \"type\": \"list\",\n        \"data\": [\n            {\n                \"type\": \"account\",\n                \"id\": \"29a1e18b\",\n                \"accountNo\": \"2\",\n                \"name\": \"Transaction 14000\",\n                \"currency\": \"AUD\",\n                \"class\": {\n                    \"type\": \"transaction\",\n                    \"product\": \"Hooli Transaction\"\n                },\n                \"balance\": \"49084.34\",\n                \"availableFunds\": \"49084.34\",\n                \"lastUpdated\": \"2020-12-02T02:21:01Z\",\n                \"status\": \"available\",\n                \"links\": {\n                    \"self\": \"https://au-api.basiq.io/users/9ac25c19/accounts/29a1e18b\",\n                    \"transactions\": \"https://au-api.basiq.io/users/9ac25c19/transactions?filter=account.id.eq('29a1e18b')\"\n                }\n            }\n        ]\n    },\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/users/9ac25c19/connections/c7231718\",\n        \"user\": \"https://au-api.basiq.io/users/9ac25c19\",\n        \"accounts\": \"https://au-api.basiq.io/users/9ac25c19/accounts?filter=institution.id.eq('AU00000')\",\n        \"transactions\": \"https://au-api.basiq.io/users/9ac25c19/transactions?filter=institution.id.eq('AU00000')\"\n    }\n}",
      "language": "json",
      "name": "Example Connection Object"
    }
  ],
  "sidebar": true
}
[/block]