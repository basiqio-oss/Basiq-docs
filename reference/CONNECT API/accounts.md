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
    "0-0": "`type`",
    "h-0": "Attributes",
    "0-1": "Value is \"account\".",
    "1-0": "`id`",
    "1-1": "Uniquely identifies the account.",
    "2-0": "`accountNo`",
    "2-1": "Full account number.",
    "3-0": "`name`",
    "3-1": "Account name as defined by institution or user.",
    "4-0": "`currency`",
    "4-1": "The currency the funds are stored in, using [ISO 4217](https://www.iban.com/currency-codes.html) standard.",
    "5-0": "`balance`",
    "5-1": "Amount of funds in the account right now - excluding any pending transactions.  For a credit card this would be zero or the minus amount spent.  *For an account providing no balance then the value provided by the bank would be passed on which could be null e.g. an insurance account.*",
    "6-0": "`availableFunds`",
    "6-1": "Funds that are available to an account holder for withdrawal or other use. This may include funds from an overdraft facility or line of credit. As well as funds classified as the available balance, such as from cleared and existing deposits.",
    "7-0": "`lastUpdated`",
    "7-1": "Timestamp of last update, UTC, RFC 3339 format e.g. \"2017-09-28T13:39:33Z\"",
    "8-0": "`class`",
    "8-1": "Identifies the **account type** and **product** as defined by institution. \n\nPossible values for **account type** are:\n\n- `transaction` - a keycard or chequing account.\n\n- `savings` - savings account.\n\n- `credit-card` - a credit card account.\n\n- `mortgage` - a home loan.\n\n- `loan` - a loan (e.g. personal or business loan).\n\n- `investment` - a investment account.\n\n- `term-deposit` - a term deposit account.\n\n- `insurance` - an insurance account.\n\n- `foreign` - a foreign cash account e.g. travel card - note, there is no support to retrieve transactions for travel cards.\n\n- `unknown`",
    "10-0": "`product`",
    "10-1": "A property of class object. Product name as defined by institution.",
    "11-0": "`meta`",
    "11-1": "A property of `class` object. Meta data related to account type. \n\nFor account type `mortgage` meta data include:\n\n- `accountNumber` - full account number.\n\n- `interestType` - loan interest rate type `fixed rate` or `variable`\n\n- `repaymentType` - loan repayment type `interest only` or `interest and principal`\n\n- `repaymentFrequency` - loan repayment \nfrequency `weekly`, `fortnightly` or `monthly`\n\n- `nextInstalmentDate` - next loan instalment date\n- `instalmentAmount` - next loan instalment amount\n\n- `interestRate` - current loan percentage interest rate - 4.8% p.a expressed as \"4.08\" \n\n- `endDate` - loan maturity date\n\n- `fee` - loan service fees \"500.00\" or text such as \"waived\"\n\n- `availableRedraw` - loan paid off that is available for redraw (variable loans only)\n\n- `offsetAccountNumber` - account linked to loan account, balance is offset against loan.",
    "12-0": "`status`",
    "12-1": "Indicates the account status. Always set to 'available'. Field kept for backward compatibility. Possible values include:\n- `available` newest account data is available.",
    "13-0": "`institution`",
    "13-1": "The id of the [institution](https://basiq.readme.io/v2.1/reference/institutions) resource the account originated from.",
    "15-1": "The **latest** id of the [connection](https://basiq.readme.io/v2.1/reference/connections) resource that was used to retrieve the account.",
    "15-0": "`connection`",
    "16-0": "`links`",
    "16-1": "A links object containing the following members:\n\n- `self` link to the requested account\n\n- `transactions` link to the transactions associated with this connection\n\n- `connection` link is always null, use the `connection` attribute for the most recent connection  [Changelog](ref:2019-07) \n\n- `institution` link to institution",
    "14-0": "`accountHolder`",
    "14-1": "The name of the account holder as returned by the institution. No formatting is applied. Returns a string or null when not available.",
    "9-0": "`transactionIntervals`",
    "9-1": "An array of date intervals indicating the coverage of the transaction data relating to the account.\nWill return a single element for accounts sourced from a single bank connection. \nWill return multiple elements in cases where there have been multiple PDF/CSV uploads for an account."
  },
  "cols": 2,
  "rows": 17
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"account\",\n  \"id\": \"s55bf3\",\n  \"accountNo\": \"34567834567890\",\n  \"name\": \"Savings 123890\",\n  \"currency\": \"AUD\",\n  \"balance\": \"26978.76\",\n  \"availableFunds\": \"26978.76\",\n  \"lastUpdated\": \"2019-09-28T13:39:33Z\",\n  \"class\": {\n    \"type\": \"savings\",\n    \"product\": \"Hooli Saver\"\n  },\n  \"transactionIntervals\": [\n    {\n      \"from\": \"2019-04-30\",\n      \"to\": \"2021-01-08\"\n    }\n  ],\n  \"status\": \"available\",\n  \"institution\": \"AU00000\",\n  \"accountHolder\": \"Max Wentworth-Smith\",\n  \"connection\": \"8fce3b\",\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"transactions\": \"https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')\",\n    \"connection\": null,\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n  }\n}",
      "language": "json",
      "name": "Example Account Object"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"meta\": {\n    \"accountNumber\": \"60000015744111\",\n    \"availableRedraw\": \"525.28\",\n    \"endDate\": \"2025-05-12T00:00:00Z\",\n    \"fee\": \"waived\",\n    \"instalmentAmount\": \"1768.23\",\n    \"interestRate\": \"4.8\",\n    \"interestType\": \"fixed rate\",\n    \"nextInstalmentDate\": \"2018-02-228T00:00:00Z\",\n    \"offsetAccountNumber\": \"60000045564000\",\n    \"repaymentFrequency\": \"weekly\",\n    \"repaymentType\": \"interest only\"\n  }\n}",
      "language": "json",
      "name": "excerpt - example account meta attribute"
    }
  ],
  "sidebar": true
}
[/block]