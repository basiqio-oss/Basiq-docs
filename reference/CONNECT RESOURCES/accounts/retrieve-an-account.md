---
title: Retrieve an account
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
Use this to retrieve the details of a specific account. This request will return back an account object with the latest data since the last refresh. If you require the latest account details you will need to call the [connection refresh](https://basiq.readme.io/v1.0/reference#refresh-a-connection) resource.

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
        The identifier of the account to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns an account if a valid account ID was provided. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) otherwise.

```json Definition
GET /users/{user.id}/accounts/{account.id}
```

```json Example Request
GET /users/ea3a81/accounts/s55bf3 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.11.1 200 OK
 Content-TypeContent-Type::  application/jsonapplication/json

{
  "type": "account",
  "id": "s55bf3",
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
  "institution": "AU00000",
  "connection": "8fce3b",
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/accounts/s55bf3",
    "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=account.id.eq('s55bf3')",
    "connection": "https://au-api.basiq.io/users/ea3a81/connections/8fce3b",
    "institution": "https://au-api.basiq.io/institutions/AU00000"
  }
}
```
