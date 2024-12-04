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
[block:parameters]
{
  "data": {
    "0-0": "**type**\n*string, readonly*",
    "h-0": "Attributes",
    "0-1": "Value is \"transaction\".",
    "1-0": "**id**\n*string, readonly*",
    "1-1": "Uniquely identifies the transaction for this connection.",
    "2-0": "**status**\n*enum, readonly*",
    "2-1": "Identifies if a transaction is `pending` or `posted`. A pending transaction is an approved debit or credit transaction that has not been fully processed yet (i.e. has not been posted). Find out more about [pending transaction and how to deal with them within your app.](http://docs.basiq.io/the-basiq-platform/what-is-a-pending-transaction)",
    "3-0": "**description**\n*string, readonly*",
    "3-1": "The transaction description as submitted by the institution.",
    "4-0": "**postDate**\n*string, readonly* ",
    "4-1": "Date the transaction was posted (this is the same date that appears on a bank statement). This value is null if the record is pending.",
    "5-0": "**transactionDate**\n*string, readonly*",
    "5-1": "Date that the user executed the transaction. Note that not all transactions provide this value (varies by institution).",
    "6-0": "**amount**\n*string, readonly*",
    "6-1": "Transaction amount. Outgoing funds are expressed as negative values.",
    "7-0": "**balance**\n*string, readonly*",
    "7-1": "Value of the account balance at time the transaction was completed.",
    "8-0": "**bankCategory**\n*string, readonly*",
    "8-1": "Category as defined by the institution itself. Note that not all institutions define this category.",
    "9-0": "**class**\n*string, readonly*",
    "9-1": "Describes the class(type) of transaction. Possible values depend on the `direction` field, and include: \n\n\n**Debit Classes:**\n- `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.\n- `payment` - payment made to a merchant.\n- `cash-withdrawal` - funds withdrawn via atm facility.\n- `internal-transfer` - funds transferred to an account (within the same connection).\n- `external-transfer` - funds transferred to an account (outside of the connection).\n\n\n**Credit Classes:**\n- `refund` - funds returned due to refund.\n- `direct-credit` - funds deposited into an account.\n- `interest` - interest earned.\n- `internal-transfer` - funds received from an account (within the same connection)\n- `external-transfer` - funds received from an account (outside of the same connection)",
    "10-0": "**[account](https://basiq.readme.io/v1.0/reference#accounts)**\n*string, readonly*",
    "10-1": "The id of the account resource the transaction belongs to.",
    "11-0": "**[institution](https://basiq.readme.io/v1.0/reference#institutions)**\n*string, readonly*",
    "11-1": "The id of the [institution](https://basiq.readme.io/v1.0/reference#institutions) resource the transaction originated from.",
    "12-0": "**[connection](https://basiq.readme.io/v1.0/reference#connections)**\n*string, readonly*",
    "12-1": "The id of the [connection](https://basiq.readme.io/v1.0/reference#connections) resource that was used to retrieve the transaction.",
    "13-0": "**links**\n*object, read-only*",
    "13-1": "A links object containing the following members:\n\n- `self` link to the requested transaction"
  },
  "cols": 2,
  "rows": 14
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"type\": \"transaction\",\n  \"id\": \"fx789e\",\n  \"status\": \"posted\",\n  \"description\": \"FLIGHT CENTRE CO    BRISB    QL\",\n  \"postDate\": \"2016-01-01\",\n  \"transactionDate\": \"\",\n  \"amount\": \"-139.98\",\n  \"balance\": \"356.50\",\n  \"bankCategory\": \"\",\n  \"account\": \"s55bf3\",\n  \"institution\": \"AU00101\",\n  \"connection\": \"8fce3b\",\n  \"direction\": \"debit\",\n  \"class\": \"payment\",\n  \"subClass\": {\n    \"code\": \"722\",\n    \"title\": \"Travel Agency and Tour Arrangement Services\"\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/users/ea3a81/transactions/fx789e\",\n    \"account\": \"https://au-api.basiq.io/users/ea3a81/accounts/s55bf3\",\n    \"institution\": \"https://au-api.basiq.io/institutions/AU00101\",\n    \"connection\": \"https://au-api.basiq.io/users/ea3a81/connections/8fce3b\"\n  }\n}",
      "language": "json",
      "name": "Example Transaction Object"
    }
  ],
  "sidebar": true
}
[/block]