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
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "account".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `accountNo`
      </td>

      <td style={{ textAlign: "left" }}>
        Full account number.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `name`
      </td>

      <td style={{ textAlign: "left" }}>
        Account name as defined by institution or user.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `currency`
      </td>

      <td style={{ textAlign: "left" }}>
        The currency the funds are stored in, using [ISO 4217](https://www.iban.com/currency-codes.html) standard.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `balance`
      </td>

      <td style={{ textAlign: "left" }}>
        Amount of funds in the account right now - excluding any pending transactions.  For a credit card this would be zero or the minus amount spent.  *For an account providing no balance then the value provided by the bank would be passed on which could be empty string or null e.g. an insurance account.* 
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `availableFunds`
      </td>

      <td style={{ textAlign: "left" }}>
        Funds that are available to an account holder for withdrawal or other use. This may include funds from an overdraft facility or line of credit. As well as funds classified as the available balance, such as from cleared and existing deposits.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `lastUpdated`
      </td>

      <td style={{ textAlign: "left" }}>
        Timestamp of last update, UTC, RFC 3339 format e.g. "2017-09-28T13:39:33Z"
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `class`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies the **account type** and **product** as defined by institution. 

        Possible values for **account type** are:

        * `transaction` - a keycard or chequing account.

        * `savings` - savings account.

        * `credit-card` - a credit card account.

        * `mortgage` - a home loan.

        * `loan` - a loan (e.g. personal or business loan).

        * `investment` - a investment account.

        * `term-deposit` - a term deposit account.

        * `insurance` - an insurance account.

        * `foreign` - a foreign cash account e.g. travel card - note, there is no support to retrieve transactions for travel cards.

        * `unknown`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `transactionIntervals`
      </td>

      <td style={{ textAlign: "left" }}>
        An array of date intervals indicating the coverage of the transaction data relating to the account.\
        Will return a single element for accounts sourced from a single bank connection.\
        Will return multiple elements in cases where there have been multiple PDF/CSV uploads for an account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `product`
      </td>

      <td style={{ textAlign: "left" }}>
        A property of class object. Product name as defined by institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `meta`
      </td>

      <td style={{ textAlign: "left" }}>
        A property of `class` object. Meta data related to account type. 

        For account type `mortgage` meta data include:

        * `accountNumber` - full account number.

        * `interestType` - loan interest rate type `fixed rate` or `variable`

        * `repaymentType` - loan repayment type `interest only` or `interest and principal`

        * `repaymentFrequency` - loan repayment\
          frequency `weekly`, `fortnightly` or `monthly`

        * `nextInstalmentDate` - next loan instalment date

        * `instalmentAmount` - next loan instalment amount

        * `interestRate` - current loan percentage interest rate - 4.8% p.a expressed as "4.08" 

        * `endDate` - loan maturity date

        * `fee` - loan service fees "500.00" or text such as "waived"

        * `availableRedraw` - loan paid off that is available for redraw (variable loans only)

        * `offsetAccountNumber` - account linked to loan account, balance is offset against loan.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `status`
      </td>

      <td style={{ textAlign: "left" }}>
        Indicates the account status. Always set to 'available'. Field kept for backward compatibility. Possible values include:

        * `available` newest account data is available.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `institution`
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [institution](https://api.basiq.io/reference/institutions) resource the account originated from.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `accountHolder`
      </td>

      <td style={{ textAlign: "left" }}>
        The name of the account holder as returned by the institution. No formatting is applied. Returns a string or null when not available.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `connection`
      </td>

      <td style={{ textAlign: "left" }}>
        The **latest** id of the [connection](https://api.basiq.io/reference/connections) resource that was used to retrieve the account.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:

        * `self` link to the requested account

        * `transactions` link to the transactions associated with this connection

        * `connection` link is always null, use the `connection` attribute for the most recent connection  [Changelog](ref:2019-07) 

        * `institution` link to institution
      </td>
    </tr>
  </tbody>
</Table>

```json Example Account Object
{
  "type": "account",
  "id": "s55bf3",
  "accountNo": "34567834567890",
  "name": "Savings 123890",
  "currency": "AUD",
  "balance": "26978.76",
  "availableFunds": "26978.76",
  "lastUpdated": "2019-09-28T13:39:33Z",
  "class": {
    "type": "savings",
    "product": "Hooli Saver"
  },
  "transactionIntervals": [
    {
      "from": "2019-04-30",
      "to": "2021-01-08"
    }
  ],
  "status": "available",
  "institution": "AU00000",
  "accountHolder": "Max Wentworth-Smith",
  "connection": "8fce3b",
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf3",
    "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')",
    "connection": null,
    "institution": "https://au-api.basiq.io/institutions/AU00000"
  }
}
```

```json excerpt - example account meta attribute
{
  "meta": {
    "accountNumber": "60000015744111",
    "availableRedraw": "525.28",
    "endDate": "2025-05-12T00:00:00Z",
    "fee": "waived",
    "instalmentAmount": "1768.23",
    "interestRate": "4.8",
    "interestType": "fixed rate",
    "nextInstalmentDate": "2018-02-228T00:00:00Z",
    "offsetAccountNumber": "60000045564000",
    "repaymentFrequency": "weekly",
    "repaymentType": "interest only"
  }
}
```
