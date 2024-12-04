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
Use this to create a new connection. When a new connection request is made the server will [create a job](https://api.basiq.io/reference/jobs) that will process the following steps:
[block:parameters]
{
  "data": {
    "h-0": "#",
    "h-1": "Step",
    "h-2": "Description",
    "0-0": "1",
    "2-0": "2",
    "4-0": "3",
    "0-1": "verify-credentials",
    "2-1": "retrieve-accounts",
    "4-1": "retrieve-transactions",
    "0-2": "The server will attempt to authenticate with the target institution using the supplied credentials",
    "2-2": "The server will retrieve the complete list of accounts and their details e.g. account number, name and balances",
    "4-2": "The server will fetch the associated transactions for each of the accounts"
  },
  "cols": 3,
  "rows": 6
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Check institution authorization type",
  "body": "To create a connection you need to check the authorization type for the institution.\n* If [Institutions](ref:institutions) authorization = `user` then **loginId** and **password** are mandatory, and user token is not required\n* If [Institutions](ref:institutions) authorization = `token` then **userToken** is mandatory and login credentials are not required"
}
[/block]
You can [check the status of each step](https://api.basiq.io/reference/retrieve-a-job) by querying the job resource (returned when the connection is created).
[block:parameters]
{
  "data": {
    "0-0": "**loginId**\n*string, conditional*",
    "h-0": "Arguments",
    "0-1": "The users institution login ID.  Mandatory if [Institutions](ref:institutions) authorization = `user`.",
    "2-0": "**password**\n*string, conditional*",
    "2-1": "The users institution password. Mandatory if [Institutions](ref:institutions) authorization = `user`.",
    "6-0": "**securityCode**\n*string, conditional*",
    "6-1": "User's institution security code. Mandatory if required by institution's login process",
    "8-0": "**secondaryLoginId**\n*string, conditional*",
    "8-1": "User's institution secondary login id. Mandatory if required by institution's login process",
    "10-0": "**[institution](https://api.basiq.io/reference/institutions)**\n*object, required*",
    "10-1": "Only the id of the institution is required",
    "4-0": "**userToken**\n*string, conditional*",
    "4-1": "The userToken.  Mandatory if [Institutions](ref:institutions) authorization = `token`."
  },
  "cols": 2,
  "rows": 11
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "Note that the time it takes to complete the processes above will vary depending on the volume of data along with the general latency between our servers and the financial institution. As a rough guide this entire process could take anywhere between 3 - 30 secs."
}
[/block]
**Returns**

Returns a created job resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:callout]
{
  "type": "info",
  "body": "If you attempt to create or refresh a connection while a job is either queued or still in progress, the API will return a 200 status with the original job instead of a newly created job.",
  "title": "In order to avoid duplicate jobs"
}
[/block]

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
      "name": "Example Request LoginId/Password"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "POST /users/ea3a81/connections HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: application/json\n{\n  \"userToken\": \"token:PTln18RhwL\",\n  \"institution\":{\n    \"id\":\"AU19301\"\n  }\n}",
      "language": "json",
      "name": "Example Request User Token"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "This response **does not contain connection ID**",
  "body": "Instead it will return a link to the job which has been created. You can use this to obtain the connection ID and track the status of the job. See [here](https://api.basiq.io/docs/handling-jobs) for more on handling jobs."
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