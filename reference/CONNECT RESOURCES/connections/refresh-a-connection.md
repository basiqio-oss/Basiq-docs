---
title: Refresh a connection
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
Use this to retrieve the latest financial data. 

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
        **id**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the connection to be refreshed.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Returns a [connection](https://basiq.readme.io/v0.9/reference#connections) object if the request succeeded. The returned object will have an embedded accounts collection object, as well as links to the latest [account](https://basiq.readme.io/v0.9/reference#accounts) and [transaction](https://basiq.readme.io/v0.9/reference#transactions) data.

Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors).

```json Definition
POST /connections/{connection.id}/refresh
```

```json Example Request
POST /connections/1/refresh HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "connection",
  "id": "1",
  "externalUserId": "721832",
  "status": "active",
  "lastUsed": "2017-09-28T11:15:09.756Z",
  "institution": {
    "type": "institution",
    "id": "AU00000",
    "links": {
      "self": "https://au-api.basiq.io/institutions/AU00000"
    }
  },
  "accounts": {
    "type": "list",
    "data": [
      {
        "type": "account",
        "id": "1",
        "accountNo": "105148119695",
        "name": "Business account",
        "currency": "AUD",
        "balance": "10.00",
        "availableFunds": "0.00",
        "lastUpdated": "2017-09-28T11:15:09.756Z",
        "class": {
            "type": "savings",
            "product": "Saver"
        },
        "status": "available",
        "links": {
          "self": "https://au-api.basiq.io/connections/1/accounts/1",
          "transactions": "https://au-api.basiq.io/connections/1/transactions?filter[account.id]=1"
        }
      },
      {
        "type": "account",
        "id": "2",
        "accountNo": "533705985043",
        "name": "Choice Account",
        "currency": "AUD",
        "balance": "-10.09",
        "availableFunds": "0.00",
        "lastUpdated": "2017-09-28T11:15:09.756Z",
        "class": {
            "type": "savings",
            "product": "Saver"
        },
        "status": "available",
        "links": {
          "self": "https://au-api.basiq.io/connections/1/accounts/2",
          "transactions": "https://au-api.basiq.io/connections/1/transactions?filter[account.id]=2"
        }
      }
    ]
  },
  "links": {
    "self": "https://au-api.basiq.io/connections/1",
    "accounts": "https://au-api.basiq.io/connections/1/accounts",
    "transactions": "https://au-api.basiq.io/connections/1/transactions"
  }
```
