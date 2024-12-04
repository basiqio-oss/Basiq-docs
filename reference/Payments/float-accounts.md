---
title: Float accounts
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
#### *Float accounts* are used to manage incoming and outgoing funds for payments through the Basiq platform.

Float accounts are virtual accounts that can hold funds and are managed by Basiq and/or its 3rd party providers. As part of setting you up within the Basiq platform for payments you will be assigned a float account. With this float account you can:

  * Have any direct debits you perform settle to your float account.
  * Manage your liquidity by holding funds in the float account.
  * Pay out funds from your float account to external bank accounts.

### Your float account details
Once you are set up for payments you can access your float account by calling [List float accounts](ref:listfloataccounts) and [Retrieve Float account](ref:getfloataccount)] if you know the float account's Id.

The API will provide you with the following details:
  * `id` : The identifier of the float account assigned by Basiq and/or its 3rd party providers. 
  * `bankBranchCode` : The bank branch code (e.g. BSB in Australia)
  * `accountNumber` : The account number of the float account
  * `availableBalance` : The balance of the account
[block:callout]
{
  "type": "info",
  "title": "Note",
  "body": "Please note this down if you want to access it using [Retrieve Float account](ref:getfloataccount)"
}
[/block]