---
title: Create a statement
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
A user can choose to share their financial data by uploading official pdf bank statements instead of creating a bank connection. Once the statement object is successfully created you can use it to obtain the user's latest financial data extracted from the bank statement i.e. accounts and transactions. 
[block:callout]
{
  "type": "success",
  "body": "The endpoint also accepts csv files conforming to our file specification.  Contact us directly for more details."
}
[/block]
Create a new statement by uploading an official pdf bank statement or csv file statement. When a new statement request is made, the server will [create a job](https://api.basiq.io/v2.1/reference/jobs) that will process the following steps:
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
    "0-2": "The server will verify the file, validate the statement layout and attempt to parse the target statement",
    "2-2": "The server will retrieve the complete list of accounts and their details e.g. account number, name and balances",
    "4-2": "The server will fetch the associated transactions for each of the accounts",
    "5-0": ""
  },
  "cols": 3,
  "rows": 6
}
[/block]
You can [check the status of each step](https://api.basiq.io/v2.1/reference/jobs) by querying the job resource (returned when the statement is created).
[block:parameters]
{
  "data": {
    "0-0": "**statement**\n*file, required*",
    "h-0": "Arguments",
    "0-1": "Official PDF bank statement for the specified [institution](ref:retrieve-an-institution) to be uploaded.  Csv files conforming to our file specification are also accepted.",
    "2-0": "**institutionId**\n*string, required*",
    "2-1": "The identifier of the [institution](ref:retrieve-an-institution) to which the statement relates e.g. \"AU01001\".  Note that sandbox institutions (i.e. AU00000 **do not** support the file upload option."
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "Note that the time it takes to complete the processes above will vary depending on the volume of data along with the complexity of the bank statement. As a rough guide this entire process could take anywhere between 10 - 30 secs. Upload multiple statements in parallel to provide the best user experience"
}
[/block]
**Returns**

Returns a created job resource, if the operation succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if the post failed (e.g. not supplying required properties).
[block:code]
{
  "codes": [
    {
      "code": "POST /users/{user.id}/statements",
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
      "code": "POST /users/ea3a81/statements HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN\nContent-Type: multipart/form-data; boundary=----xxxxxxxx\n\nContent-Disposition: form-data; name=\"statement\"; filename=\"/Users/DSmith/bankstatement_filename.pdf\"\n\nContent-Disposition: form-data; name=\"institutionId\"\nAU04301\n\nContent-Disposition: form-data; name=\"Accept\"\n\nmultipart/form-data\n------xxxxxxxx--",
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