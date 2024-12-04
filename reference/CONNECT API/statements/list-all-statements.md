---
title: List all statements
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
Use this collection to retrieve a list of [statements](https://basiq.readme.io/v2.0/reference#statements)

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
        **[filter](https://basiq.readme.io/v2.0/reference#filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://basiq.readme.io/v2.0/reference#filters) by the following properties: `upload` , `download`.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a list with a data property that contains an array of statements. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.

```json Definition
GET /users/{user.id}/statements
```

```json Example Request
GET users/ea3a81/statements HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
    "type": "list",
    "data": [
        {
            "type": "statement",
            "id": "1a73e",
            "links": {
                "self": "/users/ea3a81/statements/1a73e",
                "account": "/users/ea3a81/accounts/e40f6"
            }
        }
    ],
    "links": {
        "self": "/users/ea3a81/statements"
    }
}
```
