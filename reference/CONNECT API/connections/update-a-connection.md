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
Use this to update the details of a specific connection.

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
        The identifier of the connection to be updated.
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
        **password**\
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        User's (new or old) institution password.
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
        **securityCode**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution security code.
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
        **secondaryLoginId**\
        *string, conditional*
      </td>

      <td style={{ textAlign: "left" }}>
        User's institution secondary login id.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a [job](https://basiq.readme.io/v2.1/reference/jobs) object if the request succeeded.

Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1).

```json Definition
POST /users/{user.id}/connections/{connection.id}
```

```json Example Request
POST /users/ea3a81/connections/8fce3b HTTP/1.1
Content-Type: application/json
Authorization: Bearer YOUR_ACCESS_TOKEN

{
  "password": "Pied-Piper"
}
```

```json Example Response
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "type": "job",
  "id": "61724",
  "links": {
    "self": "https://au-api.basiq.io/jobs/61724"
  }
}
```
