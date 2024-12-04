---
title: Update a connection
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
Use this to update an existing [connection](https://basiq.readme.io/v0.9/reference#connections).

If the server has successfully acquired the financial records, connection's `status` will be set to `active`. Otherwise, if the server was unable to acquire the data using the supplied connection details, the status will be se to `invalid`.

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
        The identifier of the connection to be updated.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **password**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        User's (new or old) institution password.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **securityCode**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution security code.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **externalUserId**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        A identifier that uniqely identifies a user within your application.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Returns a [connection](https://basiq.readme.io/v0.9/reference#connections) object if the request succeeded. The returned object will have links to the acquired [account](https://basiq.readme.io/v0.9/reference#accounts) and [transaction](https://basiq.readme.io/v0.9/reference#transactions) data.

Otherwise, this call returns an [error](https://basiq.readme.io/v0.9/reference#errors).

```json Definition
POST /connections/{connection.id}
```

```json Example Request
PUT /connections/1 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "password": "Pied-Piper",
  "externalUserId": "1"
}
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "connection",
  "id": "1",
  "externalUserId": "1",
  "status": "active",
  "lastUsed": "2017-09-28T11:15:09.756Z",
  "institution": {
    "type": "institution",
    "id": "AU00000",
    "links": {
      "self": "https://au-api.basiq.io/institutions/AU00000"
    }
  },
  "links": {
    "self": "https://au-api.basiq.io/connections/1",
    "accounts": "https://au-api.basiq.io/connections/1/accounts",
    "transactions": "https://au-api.basiq.io/connections/1/transactions"
  }
}
```
