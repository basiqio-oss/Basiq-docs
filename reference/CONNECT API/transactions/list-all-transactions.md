---
title: List all transactions
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
Use this collection to retrieve a paginated list of [transactions](https://basiq.readme.io/v2.0/reference#transactions). The transactions are returned sorted by account and then posted date descending order - with pending transactions appearing first. Transactions are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.

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
        **limit**
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.
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
        **[filter](https://api.basiq.io/reference/collections)**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](ref:collections-and-filters) by the following properties:

        * `account.id`

        * `transaction.postDate`

        * `transaction.status`

        * `institution.id`

        * `transaction.direction`

        * `transaction.class`
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

Returns a paginated list with a data property that contains an array of transactions. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1) in the event of a failure.

```json Definition
GET /users/{user.id}/transactions
```

```json Example Request
GET /users/ea3a81/transactions HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "count": 1,
  "size": 432,
  "data": [
    {
      "type": "transaction",
      "id": "fx789e",
      "status": "posted",
      "description": "FLIGHT CENTRE CO    BRISB    QL",
      "postDate": "2017-11-10T21:46:44Z",
      "transactionDate": "2017-11-09T00:00:00Z",
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
  ],
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81/transactions",
    "next": "https://au-api.basiq.io/users/ea3a81/transactions?next=049fde"
  }
}
```
