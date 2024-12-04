---
title: Transactions
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
A transaction object is created whenever money is debited or credited from a particular account.
[block:callout]
{
  "type": "warning",
  "title": "Pending Transactions",
  "body": "- Pending transactions are temporary and can be filtered (to exclude/include) via transaction status attribute\n- When a connection is refreshed pending transactions are deleted and reimported \n- It is recommended, not to store pending transactions, or delete them prior to a connection refresh, as they often **change in amount, date and description**.  \n- When a connection is deleted and recreated, pending transactions are deleted from existing transaction data prior to retrieval of the latest data \n- Check out [this](https://api.basiq.io/docs/pending-transactions-1) knowledge base article for more details on pending transactions."
}
[/block]

[block:parameters]
{
  "data": {
    "0-0": "`type`",
    "h-0": "Attributes",
    "0-1": "Value is \"transaction\".",
    "2-0": "`id`",
    "2-1": "Uniquely identifies the transaction for this connection. Note that when a connection is refreshed pending transactions will receive new id's, whilst posted transactions will receive the same id's as before the refresh. Find out more about [pending transaction](https://api.basiq.io/docs/pending-transactions-1)",
    "4-0": "`status`",
    "4-1": "Identifies if a transaction is `pending` or `posted`. A pending transaction is an approved debit or credit transaction that has not been fully processed yet (i.e. has not been posted). Find out more about [pending transaction](https://api.basiq.io/docs/pending-transactions-1) and how to deal with them within your app. Note that pending transactions are not available for all institutions.",
    "6-0": "`description`",
    "6-1": "The transaction description as submitted by the institution.",
    "8-0": "`postDate`",
    "8-1": "Date the transaction was posted as provided by the institution (this is the same date that appears on a bank statement). This value is null if the record is pending. e.g. \"2017-11-10T21:46:44Z\" or 2017-11-10T00:00:00Z",
    "10-0": "`transactionDate`",
    "10-1": "Date that the user executed the transaction as provided by the institution. Note that not all transactions provide this value (varies by institution) e.g. \"2017-11-10T00:00:00Z\"",
    "12-0": "`amount`",
    "12-1": "Transaction amount. Outgoing funds are expressed as negative values.",
    "14-0": "`balance`",
    "14-1": "Value of the account balance at time the transaction was completed.",
    "16-0": "`direction`",
    "16-1": "Identifies if the transaction is of `debit` or `credit` type.",
    "18-0": "`class`",
    "18-1": "Describes the class(type) of transaction. Possible values depend on the `direction` field, and include:",
    "28-0": "`subclass`",
    "28-1": "Attribute includes a `code` and `title` property. The `subClass` attribute will only return values for payment transactions (i.e. will be empty for all others)  plus **[new]** bank fee transactions for those relating to account conduct such as account overdrawn and direct debit dishonours. [Changelog](ref:2021-06) and call-out below for examples.",
    "32-0": "[account](https://basiq.readme.io/v2.0/reference#accounts)",
    "32-1": "The id of the [account](https://basiq.readme.io/v2.1/reference/accounts) resource the transaction belongs to.",
    "34-0": "[institution](https://basiq.readme.io/v2.0/reference#institutions)",
    "34-1": "The id of the [institution](https://basiq.readme.io/v2.1/reference/institutions) resource the transaction originated from.",
    "36-0": "[connection](https://basiq.readme.io/v2.0/reference#connections)",
    "36-1": "This attribute is always null [Changelog](ref:2019-07) .",
    "38-0": "`links`",
    "38-1": "A links object containing the following members:",
    "22-1": "- `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.\n\n- `payment` - payment made to a merchant.\n\n- `cash-withdrawal` - funds withdrawn via atm facility.\n\n- `transfer` - funds transferred to an account.\n\n- `loan-interest` - interest charged on a loan account.",
    "26-1": "- `refund` - funds returned due to refund.\n\n- `direct-credit` - funds deposited into an account.\n\n- `interest` - interest earned.\n\n- `transfer` - funds received from an account.\n\n- `loan-repayment` - loan repayment credited to a loan account.",
    "20-1": "**Debit Classes:**",
    "24-1": "**Credit Classes:**",
    "40-1": "- `self` link to the requested transaction\n\n-  `account` link to the account\n\n-  `institution` link to institution",
    "30-1": "- `merchant`  - details relating to the store or merchant such as business name, website and contact details\n\n-  `location` - details relating to the location of the entity such as address and geocode location\n\n-  `category` - industry standard categorisation with a 4 level hierarchy for banking transactions.\n\n- `links` - links to the merchant logos\n\nExample JSON provided, also see [Enrich API](https://api.basiq.io/reference/enrich)  for full details on attributes returned.\n\n**For partners not enabled for Enrich API then this attribute returns null** -   `\"enrich\": null`",
    "30-0": "**[new]** `enrich`"
  },
  "cols": 2,
  "rows": 42
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Added ability to retrieve fully enriched data via Transactions endpoint for **partners enabled for Enrich API **. This means, no extra round trip to Enrich endpoint for each transaction.  For partners not enabled for Enrich then the attribute will return null.",
  "title": "Get more Enriched data via Transactions endpoint"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"transaction\",\n  \"id\": \"fx789e\",\n  \"status\": \"posted\",\n  \"description\": \"FLIGHT CENTRE CO    BRISB    QL\",\n  \"postDate\": \"2017-08-01T00:00:00Z\",\n  \"transactionDate\": \"\",\n  \"amount\": \"-139.98\",\n  \"balance\": \"356.50\",\n  \"account\": \"s55bf3\",\n  \"institution\": \"AU00101\",\n  \"connection\": \"8fce3b\",\n  \"enrich\": null,\n  \"direction\": \"debit\",\n  \"class\": \"payment\",\n  \"subClass\": {\n    \"code\": \"722\",\n    \"title\": \"Travel Agency and Tour Arrangement Services\"\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/transactions/fx789e\",\n    \"account\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00101\",\n    \"connection\": null\n  }\n}",
      "language": "json",
      "name": "Example Transaction Object (standard)"
    }
  ],
  "sidebar": true
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"transaction\",\n  \"id\": \"fx789e\",\n  \"status\": \"posted\",\n  \"description\": \"EZIDEBIT HEALTHFITNES FORT\",\n  \"amount\": \"-39.50\",\n  \"account\": \"s55bf3\",\n  \"balance\": \"567.53\",\n  \"direction\": \"debit\",\n  \"class\": \"payment\",\n  \"institution\": \"AU00000\",\n  \"connection\": \"0f198f59\",\n  \"transactionDate\": \"\",\n  \"postDate\": \"2021-01-25T00:00:00Z\",\n  \"subClass\": {\n    \"title\": \"Sports and Physical Recreation Activities\",\n    \"code\": \"911\"\n  },\n  \"enrich\": {\n    \"merchant\": {\n      \"businessName\": \"Ezidebit\",\n      \"website\": \"http://www.ezidebit.com/\",\n      \"phoneNumber\": {\n        \"local\": \"1300 763 256\",\n        \"international\": \"+61 1300 763 256\"\n      }\n    },\n    \"location\": {\n      \"routeNo\": \"480\",\n      \"route\": \"St Pauls Terrace\",\n      \"postalCode\": \"4006\",\n      \"suburb\": \"Fortitude Valley\",\n      \"state\": \"QLD\",\n      \"country\": \"Australia\",\n      \"formattedAddress\": \"480 St Pauls Terrace, Fortitude Valley QLD 4006\",\n      \"geometry\": {\n        \"lat\": \"-27.453115\",\n        \"lng\": \"153.034106\"\n      }\n    },\n    \"category\": {\n      \"anzsic\": {\n        \"division\": {\n          \"code\": \"R\",\n          \"title\": \"Arts and Recreation Services\"\n        },\n        \"subdivision\": {\n          \"code\": \"91\",\n          \"title\": \"Sports and Recreation Activities\"\n        },\n        \"group\": {\n          \"code\": \"911\",\n          \"title\": \"Sports and Physical Recreation Activities\"\n        },\n        \"class\": {\n          \"code\": \"9111\",\n          \"title\": \"Health and Fitness Centres and Gymnasia Operation\"\n        }\n      }\n    },\n    \"links\": {\n      \"logo-master\": \"https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/guzman_y_gomez-master.svg\",\n    \t\"logo-thumb\": \"https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/guzman_y_gomez-thumb.svg\"\n    }\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/transactions/fx789e\",\n    \"account\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00000\",\n    \"connection\": null\n  }\n}",
      "language": "json",
      "name": "Example Transaction Object (Enrich API enabled)"
    }
  ],
  "sidebar": true
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Bank fee subclass - account conduct indications",
  "body": "To provide meta data for bank fee transactions for transaction accounts only (account.accountType = `transaction`) - to indicate account conduct or red flags  \n*  `overdrawn` - indicating overdrawn or overlimit fee\n*  `dishonour`  - indicating direct debit dishonour fee\n*  `late` - indicating a late payment fee \n*  `interest` - indicating interest charged on a transaction account"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "\"class\": \"bank-fee\",\n \"subClass\": {\n   \"code\": \"overdrawn\",\n    title\": \"bank fee debited for account overdrawn on limit\"\n  },\n    \n\"class\": \"bank-fee\",\n\"subClass\": {\n   \"code\": \"dishonour\",\n   \"title\": \"bank fee debited for payment dishonour\"\n  },\n    \n\"class\": \"bank-fee\",\n\"subClass\": {\n   \"code\": \"late\",\n   \"title\": \"bank fee debited for late payment\"\n  },\n    \n\"class\": \"bank-fee\",\n\"subClass\": {\n   \"code\": \"interest\",\n   \"title\": \"bank fee debited for interest\"\n  },\n    \n\"class\": \"bank-fee\",\n\"subClass\": null,",
      "language": "json",
      "name": "Example bank-fee subclass responses"
    }
  ],
  "sidebar": true
}
[/block]