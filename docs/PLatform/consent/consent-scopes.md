---
title: Consent Scopes
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Here we provide a breakdown on the configurable scopes for your very own customisable consent policy. You can see the **name and description**, the **API endpoints** where it returns the data, as well as what **specific data points** are fetched with each one. 

[block:parameters]
{
  "data": {
    "h-0": "Consent Scope",
    "h-1": "Entity",
    "h-2": "Description",
    "h-3": "Attributes",
    "0-0": "Name and occupation",
    "0-1": "Basiq API  \n  \n- `/connections`CDR Scope  \n  \n- `common:customer.basic:read`",
    "0-2": "The scope allows access to personally identifiable information about the customer. Includes name and occupation of the individual.",
    "0-3": "- Name\n- Occupation",
    "1-0": "Name, occupation, contact details",
    "1-1": "Basiq API  \n  \n- `/connections`CDR Scope  \n  \n- `common:customer.detail:read`",
    "1-2": "The scope allows access to more detailed information about the customer. Includes the data available with the Basic Customer Data scope plus contact details. Includes basic data plus phone, email and address information.",
    "1-3": "- Name\n- Occupation\n- Phone\n- Email address\n- Mail address\n- Residential address",
    "2-0": "Organisation profile",
    "2-1": "Basiq API  \n  \n- `/identities`CDR Scope  \n  \n- `common:customer.basic:read`",
    "2-2": "The scope allows access to identifiable information about the customer. Includes business numbers and industry code for organisations",
    "2-3": "- Agent name and role\n- Organisation name\n- Organisation numbers (ABN or ACN)\n- Charity status\n- Establishment date\n- Industry\n- Organisation type\n- Country of registration",
    "3-0": "Organisation profile and contact details",
    "3-1": "Basiq API  \n`/identities`  \n  \nCDR Scope  \n  \n- `common:customer.detail:read`",
    "3-2": "The scope allows access to more detailed information about the customer. Includes the data available with the Basic Customer Data scope plus contact details. Includes basic data plus phone, email and address information.",
    "3-3": "- Agent name and role\n- Organisation name\n- Organisation numbers (ABN or ACN)\n- Charity status\n- Establishment date\n- Industry\n- Organisation type\n- Country of registration\n- Organisation address\n- Mail address\n- Phone number",
    "4-0": "Account name, type and balance ",
    "4-1": "Basiq API  \n  \n- `/accounts`CDR Scope  \n  \n- `bank:accounts.basic:read`",
    "4-2": "This scope allows access to basic information of the customer's accounts.  \n  \nIncludes simple account information including balance. This scope does not include account numbers, product information or transaction data.  \n  \n**Account number in this scope is masked**   \n  \n**Account name, type and balance are required.**  \n![](https://files.readme.io/dca0227-permissions.png)",
    "4-3": "- Name of account\n- Account number\n- Type of account\n- Account balance",
    "5-0": "Account numbers and features  \n  \n_requires Account name, type and balance scope_",
    "5-1": "Basiq API  \n  \n- `/accounts`CDR Scope  \n  \n- `bank:accounts.detail:read`",
    "5-2": "This scope allows access to detailed information of the customer's accounts. Includes basic account information plus account identifiers and product information. Does not include transaction data.",
    "5-3": "- Account number\n- Interest rates\n- Fees\n- Discounts\n- Account terms\n- Account mail address",
    "6-0": "Transaction details",
    "6-1": "Basiq API  \n  \n- `/transactions`CDR Scope  \n  \n- `bank:transactions:read`",
    "6-2": "This scope allows access to transaction data for accounts. Includes all account transaction data.",
    "6-3": "- Incoming and outgoing transactions\n- Amounts\n- Dates\n- Descriptions of transactions\n- Who you have sent money to and received money from"
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]