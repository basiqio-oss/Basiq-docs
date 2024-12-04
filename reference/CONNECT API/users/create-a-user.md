---
title: Create a user
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
Use this to create a new user object. 

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
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users email address. **Mandatory if mobile is not supplied.**
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
        **mobile**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users mobile number, supplied in international format\
        `+[country-code][mobileno] e.g. +61410888999` . **Mandatory if email is not supplied**
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
        **firstName**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users first name as an optional additional parameter
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
        **lastName**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users last name as an optional additional parameter
      </td>
    </tr>
  </tbody>
</Table>

**Returns**\
Returns the user object if the request succeeded. Returns an [error](https://api.basiq.io/docs/errors-1) if update parameters are invalid (e.g. supplying an empty email address).

```json Definition
POST /users
```

```json Example Request
POST /users HTTP/1.1
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

{
  "email": "gavin@hooli.com",
  "mobile": "+61410888666",
  "firstName": "Joe",
  "lastName": "Bloggs"
}
```

```json Example Response
HTTP/1.1 201 Created
Content-Type: application/json

{
  "type": "user",
  "id": "ea3a81",
  "email": "gavin@hooli.com",
  "mobile": "+61410888666",
  "firstName": "Joe",
  "lastName": "Bloggs",
  "links": {
    "self": "https://au-api.basiq.io/users/ea3a81"
  }
}
```
