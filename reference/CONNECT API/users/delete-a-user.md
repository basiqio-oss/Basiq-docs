---
title: Delete a user
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
Permanently deletes a user along with all of their associated connection details. All data associated with this user will deleted. You need only supply the unique user identifier that was returned upon user creation.

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
        \*string, required\*\*\*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the user to be deleted.
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

> ❗️ Note that this action cannot be undone

**Returns**\
Returns an empty body if the delete succeeded. Otherwise, this call returns an [error](https://api.basiq.io/docs/errors-1) in the event of a failure.

```json  
DELETE /users/{user.id}
```

```json Example Request
DELETE /users/ea3a81 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 204 No Content
```
