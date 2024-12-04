---
title: Users
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
The user object represents an end-user of your application. This object encapsulates all of the financial details of an individual (such as list of accounts and transactions) along with the relationships that they hold with each institution (i.e. connections).

Use this object to keep your list of users in sync with the Basiq server. Once a user ceases to use your application, it is strongly recommended that the user object is deleted.

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
        `type`
      </td>

      <td style={{ textAlign: "left" }}>
        Value is "user".
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
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        A string that uniquely identifies the user.
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
        `email`
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users email address.
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
        `mobile`
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users mobile number.
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
        `firstName`
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users first name.
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
        `lastName`
      </td>

      <td style={{ textAlign: "left" }}>
        The end-users last name.
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

```json Example User Object
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
