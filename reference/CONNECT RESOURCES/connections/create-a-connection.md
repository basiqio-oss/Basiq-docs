---
title: Create a connection
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
Use this to add new user [connection](https://basiq.readme.io/v0.9/reference#connections).

If the server was successful the `status` will be set to `active`. Otherwise, if the server was unable to acquire the data using the supplied connection details, the status will be se to `invalid`.
[block:parameters]
{
  "data": {
    "0-0": "**loginId**\n*string, required*",
    "h-0": "Attributes",
    "0-1": "The users institution login ID",
    "1-0": "**password**\n*string, required*",
    "1-1": "The users institution password",
    "2-0": "**securityCode**\n*string, conditional*",
    "2-1": "User's institution security code. Mandatory if required by institution's login process",
    "3-0": "**externalLoginId**\n*string, optional*",
    "3-1": "User's institution secondary login id. Mandatory if required by institution's login process",
    "4-0": "**[institution](https://basiq.readme.io/v0.9/reference#institutions)**\n*object, required*",
    "4-1": "Only the id of the institution is required"
  },
  "cols": 2,
  "rows": 5
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "Note that the time it takes to complete the processes above will vary depending on the volume of data along with the general latency between our servers and the financial institution. As a rough guide this entire process could take anywhere between 3 - 30 secs."
}
[/block]
**Returns**
Returns a [connection](https://basiq.readme.io/v0.9/reference#connections) object if the request succeeded. The returned object will have links to the acquired [account](https://basiq.readme.io/v0.9/reference#accounts) and [transaction](https://basiq.readme.io/v0.9/reference#transactions) data. Note that if the server was unable to acquire the data immediately the links will still be returned.

Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors).
[block:code]
{
  "codes": [
    {
      "code": "POST /connections",
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
      "code": "POST /connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n{\n  \"loginId\": \"gavinBelson\",\n  \"password\": \"hooli2016\",\n  \"externalUserId\": \"01\",    \n  \"institution\":{\n    \"id\":\"AU00000\"\n  }\n}",
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
      "code": "HTTP/1.1 201 Created\nContent-Type: application/json\n\n{\n  \"type\": \"connection\",\n  \"id\": \"1\",\n  \"externalUserId\": \"721832\",\n  \"status\": \"active\",\n  \"lastUsed\": \"2017-09-28T11:15:09.756Z\",\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00000\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00000\"\n    }\n  },\n  \"accounts\": {\n    \"type\": \"list\",\n    \"data\": [\n      {\n        \"type\": \"account\",\n        \"id\": \"1\",\n        \"accountNo\": \"105148119695\",\n        \"name\": \"Business account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"10.00\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/1/accounts/1\",\n          \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1\"\n        }\n      },\n      {\n        \"type\": \"account\",\n        \"id\": \"2\",\n        \"accountNo\": \"533705985043\",\n        \"name\": \"Choice Account\",\n        \"currency\": \"AUD\",\n        \"balance\": \"-10.09\",\n        \"availableFunds\": \"0.00\",\n        \"lastUpdated\": \"2017-09-28T11:15:09.756Z\",\n        \"class\": {\n            \"type\": \"savings\",\n            \"product\": \"Saver\"\n        },\n        \"status\": \"available\",\n        \"links\": {\n          \"self\": \"https://au-api.basiq.io/connections/1/accounts/2\",\n          \"transactions\": \"https://au-api.basiq.io/connections/1/transactions?filter[account.id]=2\"\n        }\n      }\n    ]\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/1\",\n    \"accounts\": \"https://au-api.basiq.io/connections/1/accounts\",\n    \"transactions\": \"https://au-api.basiq.io/connections/1/transactions\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]