---
title: Statements
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
The statement object represents an official bank statement for an account or accounts held with a financial institution (e.g. a savings account). You can **create** a statement object by uploading official pdf bank statements which are parsed to extract and expose the user's latest account and transaction data. 
[block:callout]
{
  "type": "info",
  "title": "Upload Official Bank Statements by Creating a Statement resource",
  "body": "When a new Statement request is made, the server will [create a job](https://basiq.readme.io/v2.0/reference#jobs) that will processes 3 steps verify the file, retrieve accounts and transactions"
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "",
  "body": "Note that the sandbox environment (AU00000) - does not support the Statement upload function. The Statements endpoint should be used to upload csv files or official bank statements against the correct institution."
}
[/block]