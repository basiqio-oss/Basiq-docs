---
title: Retrieve a transaction
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
Retrieves the details of an existing transaction. You need only supply the unique transaction identifier.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Arguments
      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **id**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the transaction to be retrieved.
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

**Returns**

Returns a transaction if a valid transaction ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.

```json Definition
GET /users/{user.id}/transactions/{transaction.id}
```

```json Example Request
GET /users/ea3a81/transactions/fx789e HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Transaction Object (standard)
HTTP/1.11.1 200 OK
Content-Type: application/json

{
  "type": "transaction",
  "id": "fx789e",
  "status": "posted",
  "description": "FLIGHT CENTRE CO    BRISB    QL",
  "postDate": "2017-11-10T21:46:44Z",
  "transactionDate": "",
  "amount": "-139.98",
  "balance": "356.50",
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
    "connection": null
  }
}
```
