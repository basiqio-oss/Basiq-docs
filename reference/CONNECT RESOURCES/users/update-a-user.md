---
title: Update a user
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
Updates the specified user by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

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
        **email**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users email address.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **mobile**\
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users mobile number.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Returns the user object if the update succeeded. Returns an [error](https://basiq.readme.io/v1.0/reference#errors) if update parameters are invalid (e.g. specifying an email address).

```json Definition
POST /users/{user.id}
```

```json Example Request
POST /users/ea3a81 HTTP/1.1
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

{
  "email": "gavin@hooli.xyz"
}
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "user",
  "id": "ea3a81",
  "email": "gavin@hooli.xyz",
  "mobile": "+61410888666",
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81",
    "connections": "https://au-api.basiq.io/users/ea3a81/connections"
  }
}
```
