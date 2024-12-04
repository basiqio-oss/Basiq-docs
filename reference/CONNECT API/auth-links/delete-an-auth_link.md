---
title: Delete an auth_link
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
Permanently deletes an auth\_link resource. Once deleted the URL associated with the deleted object will no longer be valid.  

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

> ❗️ Note that this action cannot be undone.

> 📘 The auth\_link is a URL that directs a User to Basiq's hosted consent workflow to link banks and securely share data. When the user selects 'I have disclosed all my accounts' the auth\_link is automatically deleted.

**Returns**\
Returns an empty body if the delete succeeded. Otherwise, this call returns an error in the event of a failure.

```json Definition
DELETE /users/ea3a81/auth_link
```

```json Example Request
DELETE /users/ea3a81/auth_link HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 204 No Content
```
