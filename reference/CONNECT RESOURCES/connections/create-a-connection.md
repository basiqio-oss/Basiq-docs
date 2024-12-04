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
Use this to create a new connection. When a new connection request is made the server will [create a job](https://basiq.readme.io/v1.0/reference#jobs) that will process the following steps:
[block:parameters]
{
  "data": {
    "h-0": "#",
    "h-1": "Step",
    "h-2": "Description",
    "0-0": "1",
    "1-0": "2",
    "2-0": "3",
    "0-1": "verify-credentials",
    "1-1": "retrieve-accounts",
    "2-1": "retrieve-transactions",
    "0-2": "The server will attempt to authenticate with the target institution using the supplied credentials",
    "1-2": "The server will retrieve the complete list of accounts and their details e.g. account number, name and balances",
    "2-2": "The server will fetch the associated transactions for each of the accounts"
  },
  "cols": 3,
  "rows": 3
}
[/block]
You can [check the status of each step](https://basiq.readme.io/v1.0/reference#retrieve-a-job) by querying the job resource (returned when the connection is created).
[block:parameters]
{
  "data": {
    "0-0": "**loginId**\n*string, required*",
    "h-0": "Arguments",
    "0-1": "The users institution login ID",
    "1-0": "**password**\n*string, required*",
    "1-1": "The users institution password",
    "2-0": "**securityCode**\n*string, conditional*",
    "2-1": "User's institution security code. Mandatory if required by institution's login process",
    "3-0": "**secondaryLoginId**\n*string, conditional*",
    "3-1": "User's institution secondary login id. Mandatory if required by institution's login process",
    "4-0": "**[institution](https://basiq.readme.io/v1.0/reference#institutions)**\n*object, required*",
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

Returns a created job resource, if the operation succeeded. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/connections",
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
      "code": "POST /users/ea3a81/connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n\n{\n  \"loginId\": \"gavinBelson\",\n  \"password\": \"hooli2016\",\n  \"institution\":{\n    \"id\":\"AU00000\"\n  }\n}",
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
      "code": "HTTP/1.1 202 Accepted\nContent-Type: application/json\n\n{\n  \"type\": \"job\",\n  \"id\": \"61723\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/jobs/61723\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]