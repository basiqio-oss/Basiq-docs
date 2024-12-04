---
title: Retrieve an auth_link
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
Use this to retrieve the latest/last auth\_link generated for the specified user..

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
        *no arguments required*
      </td>

      <td style={{ textAlign: "left" }}>

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

Returns the latest/last auth\_link generated for the specified user. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.

```json
GET /users/{user.id}/auth_link
```

```json Example Request
GET /users/{user.id}/auth_link HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/json
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "auth_link",
  "id": "63448be4",
  "userId": "ec4ea48d",
  "expiresAt": "2019-11-21T04:08:50Z",
  "mobile": "+61410000000",
  "links": {
    "self": "https://au-api.basiq.io/users/ec4ea48d/auth_link",
    "public": "https://connect.basiq.io/63448be4"
  }
}
```
