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

> 🚧 Pending Transactions
>
> * Pending transactions are temporary and can be filtered (to exclude/include) via transaction status attribute
> * When a connection is refreshed pending transactions are deleted and reimported 
> * It is recommended, not to store pending transactions, or delete them prior to a connection refresh, as they often **change in amount, date and description**.  
> * When a connection is deleted and recreated, pending transactions are deleted from existing transaction data prior to retrieval of the latest data 
> * Check out [this](https://api.basiq.io/docs/pending-transactions-1) knowledge base article for more details on pending transactions.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Attributes
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "transaction".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the transaction for this connection. Note that when a connection is refreshed pending transactions will receive new id's, whilst posted transactions will receive the same id's as before the refresh. Find out more about [pending transaction](https://api.basiq.io/docs/pending-transactions-1)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `status`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies if a transaction is `pending` or `posted`. A pending transaction is an approved debit or credit transaction that has not been fully processed yet (i.e. has not been posted). Find out more about [pending transaction](https://api.basiq.io/docs/pending-transactions-1) and how to deal with them within your app. Note that pending transactions are not available for all institutions.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `description`
      </td>

      <td style={{ textAlign: "left" }}>
        The transaction description as submitted by the institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `postDate`
      </td>

      <td style={{ textAlign: "left" }}>
        Date the transaction was posted as provided by the institution (this is the same date that appears on a bank statement). This value is null if the record is pending. e.g. "2017-11-10T21:46:44Z" or 2017-11-10T00:00:00Z
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `transactionDate`
      </td>

      <td style={{ textAlign: "left" }}>
        Date that the user executed the transaction as provided by the institution. Note that not all transactions provide this value (varies by institution) e.g. "2017-11-10T00:00:00Z"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `amount`
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction amount. Outgoing funds are expressed as negative values.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `balance`
      </td>

      <td style={{ textAlign: "left" }}>
        Value of the account balance at time the transaction was completed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `direction`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies if the transaction is of `debit` or `credit` type.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `class`
      </td>

      <td style={{ textAlign: "left" }}>
        Describes the class(type) of transaction. Possible values depend on the `direction` field, and include:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        **Debit Classes:**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.

        * `payment` - payment made to a merchant.

        * `cash-withdrawal` - funds withdrawn via atm facility.

        * `transfer` - funds transferred to an account.

        * `loan-interest` - interest charged on a loan account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        **Credit Classes:**
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `refund` - funds returned due to refund.

        * `direct-credit` - funds deposited into an account.

        * `interest` - interest earned.

        * `transfer` - funds received from an account.

        * `loan-repayment` - loan repayment credited to a loan account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `subclass`
      </td>

      <td style={{ textAlign: "left" }}>
        Attribute includes a `code` and `title` property. The `subClass` attribute will only return values for payment transactions (i.e. will be empty for all others)  plus **[new]** bank fee transactions for those relating to account conduct such as account overdrawn and direct debit dishonours. [Changelog](ref:2021-06) and call-out below for examples.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        * \*[new]\*\* `enrich`
      </td>

      <td style={{ textAlign: "left" }}>
        * `merchant`  - details relating to the store or merchant such as business name, website and contact details

        * `location` - details relating to the location of the entity such as address and geocode location

        * `category` - industry standard categorisation with a 4 level hierarchy for banking transactions.

        * `links` - links to the merchant logos

        Example JSON provided, also see [Enrich API](https://api.basiq.io/reference/enrich)  for full details on attributes returned.

        * \*For partners not enabled for Enrich API then this attribute returns null\*\* -   `"enrich": null`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [account](https://basiq.readme.io/v2.0/reference#accounts)
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [account](https://basiq.readme.io/v2.1/reference/accounts) resource the transaction belongs to.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [institution](https://basiq.readme.io/v2.0/reference#institutions)
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [institution](https://basiq.readme.io/v2.1/reference/institutions) resource the transaction originated from.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        [connection](https://basiq.readme.io/v2.0/reference#connections)
      </td>

      <td style={{ textAlign: "left" }}>
        This attribute is always null [Changelog](ref:2019-07) .
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>
        * `self` link to the requested transaction

        * `account` link to the account

        * `institution` link to institution
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Get more Enriched data via Transactions endpoint
>
> Added ability to retrieve fully enriched data via Transactions endpoint for **partners enabled for Enrich API** . This means, no extra round trip to Enrich endpoint for each transaction.  For partners not enabled for Enrich then the attribute will return null.

```json Example Transaction Object (standard)
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "transaction",
  "id": "fx789e",
  "status": "posted",
  "description": "FLIGHT CENTRE CO    BRISB    QL",
  "postDate": "2017-08-01T00:00:00Z",
  "transactionDate": "",
  "amount": "-139.98",
  "balance": "356.50",
  "account": "s55bf3",
  "institution": "AU00101",
  "connection": "8fce3b",
  "enrich": null,
  "direction": "debit",
  "class": "payment",
  "subClass": {
    "code": "722",
    "title": "Travel Agency and Tour Arrangement Services"
  },
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/transactions/fx789e",
    "account": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf3",
    "institution": "https://au-api.basiq.io/institutions/AU00101",
    "connection": null
  }
}
```

```json Example Transaction Object (Enrich API enabled)
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "transaction",
  "id": "fx789e",
  "status": "posted",
  "description": "EZIDEBIT HEALTHFITNES FORT",
  "amount": "-39.50",
  "account": "s55bf3",
  "balance": "567.53",
  "direction": "debit",
  "class": "payment",
  "institution": "AU00000",
  "connection": "0f198f59",
  "transactionDate": "",
  "postDate": "2021-01-25T00:00:00Z",
  "subClass": {
    "title": "Sports and Physical Recreation Activities",
    "code": "911"
  },
  "enrich": {
    "merchant": {
      "businessName": "Ezidebit",
      "website": "http://www.ezidebit.com/",
      "phoneNumber": {
        "local": "1300 763 256",
        "international": "+61 1300 763 256"
      }
    },
    "location": {
      "routeNo": "480",
      "route": "St Pauls Terrace",
      "postalCode": "4006",
      "suburb": "Fortitude Valley",
      "state": "QLD",
      "country": "Australia",
      "formattedAddress": "480 St Pauls Terrace, Fortitude Valley QLD 4006",
      "geometry": {
        "lat": "-27.453115",
        "lng": "153.034106"
      }
    },
    "category": {
      "anzsic": {
        "division": {
          "code": "R",
          "title": "Arts and Recreation Services"
        },
        "subdivision": {
          "code": "91",
          "title": "Sports and Recreation Activities"
        },
        "group": {
          "code": "911",
          "title": "Sports and Physical Recreation Activities"
        },
        "class": {
          "code": "9111",
          "title": "Health and Fitness Centres and Gymnasia Operation"
        }
      }
    },
    "links": {
      "logo-master": "https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/guzman_y_gomez-master.svg",
    	"logo-thumb": "https://enrich-enrichmerchantslogobucket-6or17iuhdvs9.s3-ap-southeast-2.amazonaws.com/guzman_y_gomez-thumb.svg"
    }
  },
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/transactions/fx789e",
    "account": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf3",
    "institution": "https://au-api.basiq.io/institutions/AU00000",
    "connection": null
  }
}
```

> 🚧 Bank fee subclass - account conduct indications
>
> To provide meta data for bank fee transactions for transaction accounts only (account.accountType = `transaction`) - to indicate account conduct or red flags  
>
> * `overdrawn` - indicating overdrawn or overlimit fee
> * `dishonour`  - indicating direct debit dishonour fee
> * `late` - indicating a late payment fee 
> * `interest` - indicating interest charged on a transaction account

```json Example bank-fee subclass responses
"class": "bank-fee",
 "subClass": {
   "code": "overdrawn",
    title": "bank fee debited for account overdrawn on limit"
  },
    
"class": "bank-fee",
"subClass": {
   "code": "dishonour",
   "title": "bank fee debited for payment dishonour"
  },
    
"class": "bank-fee",
"subClass": {
   "code": "late",
   "title": "bank fee debited for late payment"
  },
    
"class": "bank-fee",
"subClass": {
   "code": "interest",
   "title": "bank fee debited for interest"
  },
    
"class": "bank-fee",
"subClass": null,
```
