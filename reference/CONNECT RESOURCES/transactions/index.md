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
        Value is "transaction".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **id**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the transaction for this connection.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **status**\
        *enum, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies if a transaction is `pending` or `posted`. A pending transaction is an approved debit or credit transaction that has not been fully processed yet (i.e. has not been posted). Find out more about [pending transaction and how to deal with them within your app.](http://docs.basiq.io/the-basiq-platform/what-is-a-pending-transaction)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **description**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The transaction description as submitted by the institution.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **postDate**\
        *string, readonly* 
      </td>

      <td style={{ textAlign: "left" }}>
        Date the transaction was posted (this is the same date that appears on a bank statement). This value is null if the record is pending.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **transactionDate**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Date that the user executed the transaction. Note that not all transactions provide this value (varies by institution).
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **amount**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction amount. Outgoing funds are expressed as negative values.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **balance**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Value of the account balance at time the transaction was completed.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **bankCategory**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Category as defined by the institution itself. Note that not all institutions define this category.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **class**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        Describes the class(type) of transaction. Possible values depend on the `direction` field, and include: 

        **Debit Classes:**

        * `bank-fee` - a fee incurred by the user from their bank e.g. ATM withdrawal fee.
        * `payment` - payment made to a merchant.
        * `cash-withdrawal` - funds withdrawn via atm facility.
        * `internal-transfer` - funds transferred to an account (within the same connection).
        * `external-transfer` - funds transferred to an account (outside of the connection).

        **Credit Classes:**

        * `refund` - funds returned due to refund.
        * `direct-credit` - funds deposited into an account.
        * `interest` - interest earned.
        * `internal-transfer` - funds received from an account (within the same connection)
        * `external-transfer` - funds received from an account (outside of the same connection)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[account](https://basiq.readme.io/v1.0/reference#accounts)**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the account resource the transaction belongs to.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[institution](https://basiq.readme.io/v1.0/reference#institutions)**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [institution](https://basiq.readme.io/v1.0/reference#institutions) resource the transaction originated from.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[connection](https://basiq.readme.io/v1.0/reference#connections)**\
        *string, readonly*
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [connection](https://basiq.readme.io/v1.0/reference#connections) resource that was used to retrieve the transaction.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **links**\
        *object, read-only*
      </td>

      <td style={{ textAlign: "left" }}>
        A links object containing the following members:

        * `self` link to the requested transaction
      </td>
    </tr>
  </tbody>
</Table>

```json Example Transaction Object
{
  "type": "transaction",
  "id": "fx789e",
  "status": "posted",
  "description": "FLIGHT CENTRE CO    BRISB    QL",
  "postDate": "2016-01-01",
  "transactionDate": "",
  "amount": "-139.98",
  "balance": "356.50",
  "bankCategory": "",
  "account": "s55bf3",
  "institution": "AU00101",
  "connection": "8fce3b",
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
    "connection": "https://au-api.basiq.io/users/ea3a81/connections/8fce3b"
  }
}
```
