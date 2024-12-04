---
title: List all affordability transactions
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
Use this collection to retrieve a paginated list of [transactions](https://basiq.readme.io/v2.0/reference#transactions). The transactions are returned sorted by account and then posted date descending order - with pending transactions appearing first. Transactions are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.
[block:parameters]
{
  "data": {
    "0-0": "**limit**\n*string, optional*",
    "h-0": "Arguments",
    "0-1": "This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.",
    "2-0": "**[filter](https://api.basiq.io/docs/collections-filters)**\n*string, optional*",
    "2-1": "This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties:\n\n- `transaction.class`\n\n&nbsp;\n&nbsp;\n**Note**: this filter applies only to JSON structure, due to the difference in CSV formatting*"
  },
  "cols": 2,
  "rows": 4
}
[/block]
**Returns**

Returns a paginated list with a data property that contains an array of transactions from the affordability snapshot. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v2.0/reference#errors) in the event of a failure.
[block:callout]
{
  "type": "info",
  "title": "Affordability Transactions",
  "body": "The array of transactions used to generate Affordability insights is the full snapshot of transactions as per the [transactions](https://api.basiq.io/reference/transactions) resource where the following attributes are specific to Affordability:\n* there is no link to self\n* `class`: enums specific to affordability provide more granularity around transfer transactions - detailed in the table \n* `subClass`: attribute returns HEC class for payments by default or alternatively the custom class configured for a partner account"
}
[/block]
Each affordability transaction contains the same attributes however the data extends the  [transactions](https://basiq.readme.io/v2.0/reference#transactions) resource as follows:
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "0-1": "Describes the class(type) of transaction. Possible values depend on the `direction` field, and include:",
    "0-0": "`class`",
    "2-1": "**Debit Classes:**",
    "4-1": "- `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.\n\n- `payment` - payment made to a merchant.\n\n- `cash-withdrawal` - funds withdrawn via atm facility.\n\n- `internal-transfer` - funds transferred between shared accounts. **[affordability only]**\n\n- `external-transfer` - funds transferred to an external account (not included in accounts shared) **[affordability only]**\n\n- `loan-interest` - interest charged on a loan account.",
    "6-1": "**Credit Classes:**",
    "8-1": "- `refund` - funds returned due to refund.\n\n- `direct-credit` - funds deposited into an account.\n\n- `interest` - interest earned.\n\n- `internal-transfer` - funds transferred between shared accounts. **[affordability only]**\n\n- `external-transfer` - funds transferred to an external account (not included in accounts shared) **[affordability only]**\n\n- `loan-repayment` - loan repayment credited to a loan account.",
    "10-1": "Attribute includes a `code` and `title` property. The `subClass` attribute will only return values for payment transactions (i.e. will be empty for all others) ( **[affordability only]** - HEC classification class is returned by default **or** custom class is returned if configured - ask us about custom category mapping)",
    "10-0": "`subClass`",
    "12-1": "A links object containing the following members:",
    "12-0": "`links`",
    "14-1": "-  `account` link to the account\n\n-  `institution` link to institution\n\n(note: no link to self)"
  },
  "cols": 2,
  "rows": 15
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "GET /users/{user.id}/affordability/{affordability.id}/transactions",
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
      "code": "GET /users/115dc708/affordability/9dedbb28/transactions HTTP/1.1\nAuthorization: Bearer YOUR_ACCESS_TOKEN",
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
      "code": "HTTP/1.1 200 OK\nContent-Type: application/json\n\n{\n  \"type\": \"list\",\n  \"count\": 500,\n  \"size\": 4434,\n  \"data\": [\n    {\n      \"type\": \"transaction\",\n      \"id\": \"8272d3cb\",\n      \"status\": \"posted\",\n      \"description\": \"DDEBIT Only About Children Seaforth\",\n      \"amount\": \"-114.88\",\n      \"account\": \"5b45bd2e\",\n      \"balance\": \"-114.34\",\n      \"direction\": \"debit\",\n      \"class\": \"payment\",\n      \"institution\": \"AU00000\",\n      \"transactionDate\": \"\",\n      \"postDate\": \"2017-06-12T00:00:00Z\",\n      \"subClass\": {\n        \"title\": \"Formal child care services nec\",\n        \"code\": \"0801050199\"\n      },\n      \"links\": {\n        \"account\": \"https://au-api.basiq.io/users/115dc708/accounts/5b45bd2e\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n    {\n      \"type\": \"transaction\",\n      \"id\": \"4258e66b\",\n      \"status\": \"posted\",\n      \"description\": \"TFR Acc14000 TO 12389\",\n      \"amount\": \"-500.00\",\n      \"account\": \"5b45bd2e\",\n      \"balance\": \"7895.00\",\n      \"direction\": \"debit\",\n      \"class\": \"internal-transfer\",\n      \"institution\": \"AU00000\",\n      \"transactionDate\": \"\",\n      \"postDate\": \"2017-06-13T00:00:00Z\",\n      \"subClass\": null,\n      \"links\": {\n        \"account\": \"https://au-api.basiq.io/users/115dc708/accounts/5b45bd2e\",\n        \"institution\": \"https://au-api.basiq.io/institutions/AU00000\"\n      }\n    },\n  ],\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/115dc708/affordability/9dedbb28/transactions\",\n    \"next\": \"https://au-api.basiq.io/users/115dc708/affordability/9dedbb28/transactions?next=9b7d9a64\"\n  }\n}",
      "language": "json",
      "name": "Example Response"
    }
  ],
  "sidebar": true
}
[/block]