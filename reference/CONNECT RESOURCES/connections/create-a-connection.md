---
title: Create a connection
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
Use this to add new user [connection](https://basiq.readme.io/v0.9/reference#connections).

If the server was successful the `status` will be set to `active`. Otherwise, if the server was unable to acquire the data using the supplied connection details, the status will be se to `invalid`.

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
        **loginId**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The users institution login ID
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **password**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The users institution password
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **securityCode**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution security code. Mandatory if required by institution's login process
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **externalLoginId**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution secondary login id. Mandatory if required by institution's login process
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[institution](https://basiq.readme.io/v0.9/reference#institutions)**\
        *object, required*
      </td>

      <td style={{ textAlign: "left" }}>
        Only the id of the institution is required
      </td>
    </tr>
  </tbody>
</Table>

> 🚧 Note that the time it takes to complete the processes above will vary depending on the volume of data along with the general latency between our servers and the financial institution. As a rough guide this entire process could take anywhere between 3 - 30 secs.

**Returns**\
Returns a [connection](https://basiq.readme.io/v0.9/reference#connections) object if the request succeeded. The returned object will have links to the acquired [account](https://basiq.readme.io/v0.9/reference#accounts) and [transaction](https://basiq.readme.io/v0.9/reference#transactions) data. Note that if the server was unable to acquire the data immediately the links will still be returned.

Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors).

```json Definition
POST /connections
```

```json Example Request
POST /connections HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "loginId": "gavinBelson",
  "password": "hooli2016",
  "externalUserId": "01",    
  "institution":{
    "id":"AU00000"
  }
}
```

```json Example Response
HTTP/1.1 201 Created
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
}
```
