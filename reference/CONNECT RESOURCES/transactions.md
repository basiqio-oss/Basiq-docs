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
    "9-1": "Identifies if the transaction is of debit or credit type. This object contains a list of the following types of subclasses: \n\n**Debit Subclasses:**\n- `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.\n- `direct-debit` - funds directly debited from the user’s bank account.\n- `payment` - payment made to a merchant.\n- `cash-withdrawal` - funds withdrawn via atm facility.\n- `internal-transfer` - funds transferred to an account (within the same connection).\n- `external-transfer` - funds transferred to an account (outside of the connection).\n\n**Credit Subclasses:**\n- `refund` - funds returned due to refund.\n- `direct-credit` - funds deposited into an account.\n- `interest` - interest earned.\n- `internal-transfer` - funds received from an account (within the same connection)\n- `external-transfer` - funds received from an account (outside of the same connection)\n\n**Notes:**\n- Note that some transactions may be classified into multiple subclasses of the same class, for e.g. when a customer pays a merchant and withdraws cash from the same facility.\n-Debit transactions with a subclass of type `payment` may also include details of the `merchant` through which the payment took place. Merchant details may change over time (e.g. businesses may change address) - Basiq retains copies of these changes, and will ensure that the correct details are returned with each transaction record to indicate the validity at the date the payment took place.",
    "10-0": "**[account](https://basiq.readme.io/v0.9/reference#accounts)**\n*string, readonly*",
    "10-1": "User's accounts in this institution.",
    "11-0": "**[institution](https://basiq.readme.io/v0.9/reference#institutions)**\n*string, readonly*",
    "11-1": "The institution this transaction relates to.",
    "12-0": "**[connection](https://basiq.readme.io/v0.9/reference#connections)**\n*string, readonly*",
    "12-1": "The connection this transaction relates to.",
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
      "code": "{\n  \"type\": \"transaction\",\n  \"id\": \"fx789e\",\n  \"status\": \"posted\",\n  \"description\": \"FLIGHT CENTRE CO    BRISB    QL\",\n  \"postDate\": \"2016-01-01\",\n  \"transactionDate\": \"\",\n  \"amount\": \"-139.98\",\n  \"balance\": \"356.50\",\n  \"bankCategory\": \"\",\n  \"class\": {\n    \"type\": \"debit\",\n    \"subclass\": [\n      {\n        \"type\": \"payment\",\n        \"merchant\": {\n          \"type\": \"merchant\",\n          \"id\": \"88ab27\",\n          \"created\": \"2015-09-27T16:23:02Z\",\n          \"updated\": \"2015-09-27T16:23:02Z\",\n          \"identity\": {\n            \"entityName\": \"FLIGHT CENTRE TRAVEL GROUP LIMITED\",\n            \"businessName\": \"FLIGHT CENTRE\",\n            \"businessNumber\": \"25003377188\",\n            \"status\": \"active\",\n            \"phoneNumber\": {\n              \"local\": \"(07) 3221 4821\",\n              \"international\": \"+61 7 3221 4821\"\n            },\n            \"website\": \"https://www.flightcentre.com.au/\",\n            \"operatingHours\": {\n              \"monday\": [\n                {\n                  \"begin\": \"09:00\",\n                  \"end\": \"17:30\"\n                }\n              ],\n              \"tuesday\": [\n                {\n                  \"begin\": \"09:00\",\n                  \"end\": \"17:30\"\n                }\n              ],\n              \"wednesday\": [\n                {\n                  \"begin\": \"09:00\",\n                  \"end\": \"17:30\"\n                }\n              ],\n              \"thursday\": [\n                {\n                  \"begin\": \"09:00\",\n                  \"end\": \"17:30\"\n                }\n              ],\n              \"friday\": [\n                {\n                  \"begin\": \"09:00\",\n                  \"end\": \"12:00\"\n                },\n                {\n                  \"begin\": \"12:30\",\n                  \"end\": \"17:30\"\n                }\n              ],\n              \"saturday\": [                \n              ],\n              \"sunday\": [              \n              ]\n            }\n          },\n          \"location\": {\n            \"routeNo\": \"327\",\n            \"route\": \"George Street\",\n            \"postalCode\": \"4000\",\n            \"locality\": {\n              \"longName\": \"Brisbane City\",\n              \"shortName\": \"Brisbane\"\n            },\n            \"administrativeArea2\": {\n              \"longName\": \"Brisbane City\",\n              \"shortName\": \"Brisbane City\"\n            },\n            \"administrativeArea1\": {\n              \"longName\": \"Queensland\",\n              \"shortName\": \"QLD\"\n            },\n            \"country\": {\n              \"name\": \"Australia\",\n              \"code\": \"AU\"\n            },\n            \"formattedAddress\": \"327 George St Brisbane City QLD 4000 Australia\",\n            \"geometry\": {\n              \"lat\": \"-27.4687768\",\n              \"lng\": \"153.0216079\"\n            }\n          },\n          \"classification\": {\n            \"mcc\": {\n              \"code\": \"4722\",\n              \"title\": \"Travel Agencies and Tour Operations\"\n            },\n            \"anzsic\": {\n              \"division\": {\n                \"code\": \"N\",\n                \"title\": \"Administrative and Support Services\"\n              },\n              \"subdivision\": {\n                \"code\": \"72\",\n                \"title\": \"Administrative Services\"\n              },\n              \"group\": {\n                \"code\": \"722\",\n                \"title\": \"Travel Agency and Tour Arrangement Services\"\n              },\n              \"class\": {\n                \"code\": \"7220\",\n                \"title\": \"Travel Agency and Tour Arrangement Services\"\n              }\n            }\n          }\n        }\n      }\n    ]\n  },\n  \"institution\": {\n    \"type\": \"institution\",\n    \"id\": \"AU00101\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/institutions/AU00101\"\n    }\n  },\n  \"connection\": {\n    \"type\": \"connection\",\n    \"id\": \"8fce3b\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/connections/8fce3b\"\n    }\n  },\n  \"account\": {\n    \"type\": \"account\",\n    \"id\": \"s55bf3\",\n    \"links\": {\n      \"self\": \"https://au-api.basiq.io/connections/8fce3b/accounts/s55bf3\"\n    }\n  },\n  \"links\": {\n    \"self\": \"https://au-api.basiq.io/connections/8fce3b/transactions/fx789e\"\n  }\n}",
      "language": "json",
      "name": "Example Transaction Object"
    }
  ],
  "sidebar": true
}
[/block]