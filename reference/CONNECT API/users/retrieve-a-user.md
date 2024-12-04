---
title: Retrieve a user
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
Retrieves the details of an existing user. You need only supply the unique user identifier that was returned upon user creation.

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
        The identifier of the user to be retrieved.
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

**Returns**\
Returns a user if a valid user ID was provided. Returns an [error](https://api.basiq.io/docs/errors-1) otherwise.

```http Defintion
GET /users/{user.id}
```

```json Example Request
GET /users/ea3a81 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "user",
  "id": "ea3a81",
  "email": "gavin@hooli.com",
  "mobile": "+61410888666",
  "firstName": "Joe",
  "lastName": "Bloggs",
  "connections": {
    "type": "list",
    "count": 1,
    "data": [
      {
        "type": "connection",
        "id": "aaaf2c3b",
        "links": {
          "self": "https://au-api.basiq.io/users/ea3a81/connections/aaaf2c3b"
        }
      }
    ]
  },
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81",
    "connections": "https://au-api.basiq.io/users/ea3a81/connections"
  }
}
```
