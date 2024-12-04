---
title: Accounts
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
The account object represents an account held with a financial institution (e.g. a savings account). You can use this object to retrieve specific account details such as the account number, balance and available funds.
[block:parameters]
{
  "data": {
    "0-0": "**type**\n*string, readonly*",
    "h-0": "Attributes",
    "0-1": "Value is \"account\".",
    "1-0": "**id**\n*string, readonly*",
    "1-1": "Uniquely identifies the account.",
    "2-0": "**accountNo**\n*string, readonly*",
    "2-1": "Full account number.",
    "3-0": "**name**\n*string, readonly*",
    "3-1": "Account name as defined by institution or user.",
    "4-0": "**currency**\n*string, readonly*",
    "4-1": "The currency the funds are stored in, using [ISO 4217](https://www.iban.com/currency-codes.html) standard.",
    "5-0": "**balance**\n*string, readonly*",
    "5-1": "How much funds are in the account right now - excluding any pending transactions.",
    "6-0": "**availableFunds**\n*string, readonly*",
    "6-1": "Funds that are available to an account holder for withdrawal or other use. This may include funds from an overdraft facility or line of credit, as well as funds classified as the available balance, such as from cleared and existing deposits.",
    "7-0": "**lastUpdated**\n*string, readonly*",
    "7-1": "Timestamp of last update, UTC, RFC 3339 format.",
    "8-0": "**class**\n*object, readonly*",
    "8-1": "Identifies the **account type** and **product** as defined by institution. \n\nPossible values for **account type** are:\n\n- `credit-card` - a credit card account.\n- `foreign` - a foreign cash account e.g. travelcard.\n- `insurance` - an insurance account.\n- `investment` - a investment account.\n- `loan` - a loan (e.g. personal or business loan).\n- `mortgage` - a home loan.\n- `savings` - savings account.\n- `term-deposit` - a term deposit account.\n- `transaction` - a keycard or chequing account.\n- `unknown`",
    "9-0": "**product**\n*string, readonly*",
    "9-1": "A property of class object. Product name as defined by institution.",
    "10-0": "**status**\n*enum, readonly*",
    "10-1": "Indicates the account status. Possible values include:\n\n- `available` newest account data is available.\n- `unavailable` account information is no longer available.",
    "11-0": "**institution**\n*string, readonly*",
    "11-1": "The id of the [institution](https://basiq.readme.io/v1.0/reference#institutions) resource the account originated from.",
    "12-1": "The id of the [connection](https://basiq.readme.io/v1.0/reference#connections) resource that was used to retrieve the account.",
    "12-0": "**connection**\n*string, readonly*",
    "13-0": "**links**\n*object, read-only*",
    "13-1": "A links object containing the following members:\n\n- `self` link to the requested account\n- `transactions` link to the transactions associated with this connection"
  },
  "cols": 2,
  "rows": 14
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"account\",\n  \"id\": \"s55bf3\",\n  \"accountNo\": \"600000-157441965\",\n  \"name\": \"Master Savings\",\n  \"currency\": \"AUD\",\n  \"balance\": \"356.50\",\n  \"availableFunds\": \"420.28\",\n  \"lastUpdated\": \"2017-09-28T13:39:33.144Z\",\n  \"class\": {\n    \"type\": \"savings\",\n    \"product\": \"Saver\"\n  },\n  \"status\": \"available\",\n  \"institution\": \"AU00000\",\n  \"connection\": \"8fce3b\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')\",\n    \"connection\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\",\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n  }\n}",
      "language": "json",
      "name": "Example Account Object"
    }
  ],
  "sidebar": true
}
[/block]