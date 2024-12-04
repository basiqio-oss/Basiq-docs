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
Use this collection to retrieve a paginated list of [transactions](https://basiq.readme.io/v2.1/reference/transactions). The transactions are returned sorted by account and then posted date descending order - with pending transactions appearing first. Transactions are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.

[block:parameters]
{
  "data": {
    "h-0": "Arguments",
    "h-1": "",
    "0-0": "**limit**  \n_string, optional_",
    "0-1": "This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.",
    "1-0": "",
    "1-1": "",
    "2-0": "**[filter](https://api.basiq.io/docs/collections-filters)**  \n_string, optional_",
    "2-1": "This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties:  \n  \n- `transaction.class`  \n  \n   \n  \n   \n**Note**: this filter applies only to JSON structure, due to the difference in CSV formatting\\*",
    "3-0": "",
    "3-1": ""
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


**Returns**

Returns a paginated list with a data property that contains an array of transactions from the affordability snapshot. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1) in the event of a failure.

> 📘 Affordability Transactions
> 
> The array of transactions used to generate Affordability insights is the full snapshot of transactions as per the [transactions](https://basiq.readme.io/v2.1/reference/transactions) resource where the following attributes are specific to Affordability:
> 
> - there is no link to self
> - `class`: enums specific to affordability provide more granularity around transfer transactions - detailed in the table 
> - `subClass`: attribute returns HEC class for payments by default or alternatively the custom class configured for a partner account

Each affordability transaction contains the same attributes however the data extends the  [transactions](https://basiq.readme.io/v2.1/reference/transactions) resource as follows:

[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "h-1": "",
    "0-0": "`class`",
    "0-1": "Describes the class(type) of transaction. Possible values depend on the `direction` field, and include:",
    "1-0": "",
    "1-1": "",
    "2-0": "",
    "2-1": "**Debit Classes:**",
    "3-0": "",
    "3-1": "",
    "4-0": "",
    "4-1": "- `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.  \n  \n- `payment` - payment made to a merchant.  \n  \n- `cash-withdrawal` - funds withdrawn via atm facility.  \n  \n- `internal-transfer` - funds transferred between shared accounts. **[affordability only]**  \n  \n- `external-transfer` - funds transferred to an external account (not included in accounts shared) **[affordability only]**  \n  \n- `loan-interest` - interest charged on a loan account.",
    "5-0": "",
    "5-1": "",
    "6-0": "",
    "6-1": "**Credit Classes:**",
    "7-0": "",
    "7-1": "",
    "8-0": "",
    "8-1": "- `refund` - funds returned due to refund.  \n  \n- `direct-credit` - funds deposited into an account.  \n  \n- `interest` - interest earned.  \n  \n- `internal-transfer` - funds transferred between shared accounts. **[affordability only]**  \n  \n- `external-transfer` - funds transferred from an external account (not included in accounts shared) **[affordability only]**  \n  \n- `loan-repayment` - loan repayment credited to a loan account.",
    "9-0": "",
    "9-1": "",
    "10-0": "`subClass`",
    "10-1": "Attribute includes a `code` and `title` property. The `subClass` attribute will only return values for payment transactions (i.e. will be empty for all others) ( **[affordability only]** - HEC classification class is returned by default **or** custom class is returned if configured - ask us about custom category mapping)",
    "11-0": "",
    "11-1": "",
    "12-0": "`links`",
    "12-1": "A links object containing the following members:",
    "13-0": "",
    "13-1": "",
    "14-0": "",
    "14-1": "-  `account` link to the account  \n  \n-  `institution` link to institution  \n  \n(note: no link to self)"
  },
  "cols": 2,
  "rows": 15,
  "align": [
    "left",
    "left"
  ]
}
[/block]


```json Definition
GET /users/{user.id}/affordability/{affordability.id}/transactions
```

```json Example Request
GET /users/115dc708/affordability/9dedbb28/transactions HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "count": 500,
  "size": 4434,
  "data": [
    {
      "type": "transaction",
      "id": "8272d3cb",
      "status": "posted",
      "description": "DDEBIT Only About Children Seaforth",
      "amount": "-114.88",
      "account": "5b45bd2e",
      "balance": "-114.34",
      "direction": "debit",
      "class": "payment",
      "institution": "AU00000",
      "transactionDate": "",
      "postDate": "2017-06-12T00:00:00Z",
      "subClass": {
        "title": "Formal child care services nec",
        "code": "0801050199"
      },
      "links": {
        "account": "https://au-api.basiq.io/users/115dc708/accounts/5b45bd2e",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
    {
      "type": "transaction",
      "id": "4258e66b",
      "status": "posted",
      "description": "TFR Acc14000 TO 12389",
      "amount": "-500.00",
      "account": "5b45bd2e",
      "balance": "7895.00",
      "direction": "debit",
      "class": "internal-transfer",
      "institution": "AU00000",
      "transactionDate": "",
      "postDate": "2017-06-13T00:00:00Z",
      "subClass": null,
      "links": {
        "account": "https://au-api.basiq.io/users/115dc708/accounts/5b45bd2e",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    },
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/115dc708/affordability/9dedbb28/transactions",
    "next": "https://au-api.basiq.io/users/115dc708/affordability/9dedbb28/transactions?next=9b7d9a64"
  }
}
```