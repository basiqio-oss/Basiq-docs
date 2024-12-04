---
title: Managing float accounts
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
#### *Float accounts* are used to manage incoming and outgoing funds for payments through the Basiq platform.

Float accounts are virtual accounts that can hold funds and are managed by Basiq and/or its 3rd party providers. As part of setting you up within the Basiq platform for payments you will be assigned a float account. With this float account you can:

  * Have any direct debits you perform settle to your float account.
  * Manage your liquidity by holding funds in the float account.
  * Pay out funds from your float account to external bank accounts.

### Your float account details
Once you are set up for payments you can access your float account by calling [List float accounts](ref:listfloataccounts) and [Get a float account by its Id](ref:getfloataccount) if you know the float account's Id.

The API will provide you with the following details:
  * Float account Id `id` : The identifier of the float account assigned by Basiq and/or its 3rd party providers. Please note this down if you want to access it using [Get a float account by its Id](ref:getfloataccount) 
  * Bank Branch Code `bankBranchCode` : The bank branch code (e.g. BSB in Australia)
  * Account Number `accountNumber` : The account number of the float account
  * Available Balance `availableBalance` : The balance of the account
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"list\",\n    \"count\": 1,\n    \"data\": [\n        {\n            \"type\": \"floataccount\",\n            \"id\": \"786ffcce-a112-43d8-8bad-b38393fe0a9f\",\n            \"bankBranchCode\": \"802919\",\n            \"accountNumber\": \"1111111\",\n            \"availableBalance\": 14733.15,\n            \"status\": \"active\",\n            \"links\": {\n                \"self\": \"https://au-api.basiq.io/payments/float-accounts/786ffcce-a112-43d8-8bad-b38393fe0a9f\"\n            }\n        }\n    ],\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/payments/float-accounts\"\n    }\n}",
      "language": "json",
      "name": "List float accounts"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"type\": \"floataccount\",\n    \"id\": \"786ffcce-a112-43d8-8bad-b38393fe0a9f\",\n    \"bankBranchCode\": \"802919\",\n    \"accountNumber\": \"1111111\",\n    \"availableBalance\": 14733.15,\n    \"status\": \"active\",\n    \"links\": {\n        \"self\": \"https://au-api.basiq.io/payments/float-accounts/786ffcce-a112-43d8-8bad-b38393fe0a9f\"\n    }\n}",
      "language": "json",
      "name": "Get float account"
    }
  ]
}
[/block]
### Managing your float account

In order to perform Send (payouts) as per [Send workflow](doc:send-workflow) you will need to maintain enough funds in your float account. There are a few ways to manage funds in your float account which are detailed as follows:

## Auto top-up
Using this feature you can maintain a target balance for your float account. As part of setting auto top-ups you can provide a target balance and a bank account. When your float account drops below the target balance our systems will automatically debit your nominated bank account to get the funds back to the target balance. As the funding is done using direct debit it will be subject to direct debit processing times as described in [Processing times](doc:payments-processing-times).
[block:callout]
{
  "type": "info",
  "body": "The bank account needs to be set up within the Basiq platform and verified as part of your onboarding."
}
[/block]
Please reach out to us at [support@basiq.io](mailto:support@basiq.io) to setup auto top-ups.

## Manually funding your float account
As the float account has an account number you can send funds to your float whenever needed from your bank account. If your bank account is enabled for fast/real-time payments then the funds could be available in your float account within minute(s) (this is dependent on your bank sending the payment via fast network rails). Alternatively, if the payment is made using batch mode then the funds should be available within 2 business days.

## Funding your float account using direct debits
Collect (payrequest) instructions can be set up to settle to your float account. There are two ways to perform this:
1. As part of your set up by default all Collect (payrequests) funds to settle to your float account.
2. If as part of your set up you have indicated that you do not want Collect (payrequests) to settle to your float, then you can indicate a flag within Collect (payrequests) to settle the funds to your float account as per the field `collectFundsToFloat` shown in the example below:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"payrequests\": [\n        {\n            \"requestId\": \"0952a101-5179-4209-baa3-ffbd3530eaa8\",\n            \"amount\": 48.00,\n            \"description\": \"Smart Investment\",\n            \"collectFundsToFloat\": true,\n            \"payer\": {\n                \"payerUserId\": \"1952a101-5179-4209-baa3-ffbd3530eaa9\"\n            }\n        }\n    ]\n}",
      "language": "json",
      "name": null
    }
  ]
}
[/block]