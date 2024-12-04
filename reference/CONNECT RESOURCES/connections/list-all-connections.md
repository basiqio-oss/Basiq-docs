---
title: List all connections
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
Use this collection to retrieve a list of [connections](https://basiq.readme.io/v1.0/reference#connections).

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
        **[filter](https://basiq.readme.io/v1.0/reference#filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://basiq.readme.io/v1.0/reference#filters) by the following properties: `id` , `status` , `institution.id`.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a list with a data property that contains an array of connections. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.

```json Definition
GET /users/{user.id}/connectionsGET /users
```

```json Example Request
GET users/ea3a81/connections HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "data": [
    {
      "type": "connection",
      "id": "8fce3b",
      "status": "active",
      "lastUsed": "2017-09-28T11:15:09Z",
      "institution": {
        "type": "institution",
        "id": "AU00000",
        "links": {
          "self": "https://au-api.basiq.io/institutions/AU00000"
        }
      },
      "links": {
        "self": "https://au-api.basiq.io/connections/8fce3b",
        "accounts": "https://au-api.basiq.io/users/ea3a81/accounts?filter=connection.id.eq('8fce3b')",
        "transactions": "https://au-api.basiq.io/users/ea3a81/transactions?filter=connection.id.eq('8fce3b')"
      }
    }
  ],
  "links": {
    "self": "/users/ea3a81/connections"
  }
}
```
