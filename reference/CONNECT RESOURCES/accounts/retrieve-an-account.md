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
Use this to retrieve the details of a specific account. This request will return back an account object with the latest data since the last refresh. If you require the latest account details you will need to call the [connection refresh](https://basiq.readme.io/v0.9/reference#refresh-a-connection) resource.

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

Returns an account if a valid account ID was provided. Returns an [error](https://basiq.readme.io/v0.9/reference#errors) otherwise.

```json Definition
GET /connections/{connection.id}/accounts/{account.id}
```

```json Example Request
GET /connections/1/accounts/1 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

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
