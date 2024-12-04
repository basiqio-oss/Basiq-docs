---
title: Delete a connection
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
Permanently deletes a connection. Once the connection has been deleted, all of the associated financial data e.g. accounts and transactions will no longer be accessible.

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
        **id**
        *string, required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the connection to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

> ❗️ Note that this action cannot be undone.

**Returns**\
Returns an empty body if the delete succeeded. Otherwise, this call returns an error in the event of a failure.

```json Definition
DELETE /users/ea3a81/connections/{connection.id}
```

```json Example Request
DELETE /users/ea3a81/connections/8fce3b HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 204 No Content
```
