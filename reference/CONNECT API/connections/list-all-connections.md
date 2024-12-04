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
Use this collection to retrieve a list of [connections](https://basiq.readme.io/v2.0/reference#connections).

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
        **[filter](https://api.basiq.io/docs/collections-filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties: `id` , `status` , `institution.id`.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a list with a data property that contains an array of connections. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.

```json Definition
GET /users/{user.id}/connections
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
      "id": "c7231718",
      "status": "active",
      "createdDate": "2020-12-02T02:20:49Z",
      "lastUsed": "2020-12-02T02:20:59Z",
      "institution": {
        "type": "institution",
        "id": "AU00000",
        "links": {
          "self": "https://au-api.basiq.io/institutions/AU00000"
        }
      },
      "links": {
        "self": "https://au-api.basiq.io/users/9ac25c19/connections/c7231718",
        "accounts": "https://au-api.basiq.io/users/9ac25c19/accounts?filter=institution.id.eq('AU00000')",
        "transactions": "https://au-api.basiq.io/users/9ac25c19/transactions?filter=institution.id.eq('AU00000')",
        "institution": "https://au-api.basiq.io/institutions/AU00000"
      }
    }
  ],
  "links": {
    "self": "/users/9ac25c19/connections"
  }
}
```
