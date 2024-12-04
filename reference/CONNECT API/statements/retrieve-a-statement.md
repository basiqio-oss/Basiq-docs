---
title: Retrieve a statement
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
Use this to download a specific bank statement. This request will return back a pdf file to save locally.

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
        *required*
      </td>

      <td style={{ textAlign: "left" }}>
        The identifier of the statement to be retrieved.
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

> 📘
>
> Specify attribute application/pdf or application/json in the Accept header of your request.

**Returns**

Returns pdf bank statement if a valid statement ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.

```json
GET /users/{user.id}/statements/{statement.id}
```

```json Example Request
GET /users/ea3a81/statements/1a73e HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
Accept: application/pdf
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/pdf
```
