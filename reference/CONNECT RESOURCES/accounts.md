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
        **type**
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "account".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **id**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **accountNo**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Full account number.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **name**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Account name as defined by institution or user.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **currency**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The currency the funds are stored in, using [ISO 4217](https://www.iban.com/currency-codes.html) standard.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **balance**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        How much funds are in the account right now - excluding any pending transactions.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **availableFunds**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Funds that are available to an account holder for withdrawal or other use. This may include funds from an overdraft facility or line of credit, as well as funds classified as the available balance, such as from cleared and existing deposits.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **lastUpdated**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Timestamp of last update, UTC, RFC 3339 format.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **class**\
        *object, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the **account type** and **product** as defined by institution. 

        Possible values for **account type** are:

        * `credit-card` - a credit card account.
        * `foreign` - a foreign cash account e.g. travelcard.
        * `insurance` - an insurance account.
        * `investment` - a investment account.
        * `loan` - a loan (e.g. personal or business loan).
        * `mortgage` - a home loan.
        * `savings` - savings account.
        * `term-deposit` - a term deposit account.
        * `transaction` - a keycard or chequing account.
        * `unknown`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **product**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        A property of class object. Product name as defined by institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **status**\
        *enum, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Indicates the account status. Possible values include:

        * `available` newest account data is available.
        * `unavailable` account information is no longer available.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **institution**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [institution](https://basiq.readme.io/v0.9/reference#institutions) resource the account originated from.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **connection**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [connection](https://basiq.readme.io/v0.9/reference#connections) resource that was used to retrieve the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **links**\
        *object, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:

        * `self` link to the requested account
        * `transactions` link to the transactions associated with this connection
      </td>
    </tr>
  </tbody>
</Table>

```json Example Account Object
{
  "type": "account",
  "id": "1",
  "accountNo": "600000-157441965",
  "name": "Master Savings",
  "currency": "AUD",
  "balance": "356.50",
  "availableFunds": "420.28",
  "lastUpdated": "2017-09-28T13:39:33.144Z",
  "class": {
    "type": "savings",
    "product": "Saver"
  },
  "status": "available",
  "institution": {
    "type": "institution",
    "id": "AU0000",
    "links": {
      "self": "https://au-api.basiq.io/institutions/AU00000"
    }
  },
  "connection": {
    "type": "connection",
    "id": "1",
    "links": {
      "self": "https://au-api.basiq.io/connections/1"
    }
  },
  "links": {
    "self": "https://au-api.basiq.io/connections/1/accounts/1",
    "transactions": "https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1"
  }
}
```
