---
title: List all users
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
Use this collection to retrieve a list of [Users](ref:users)

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
        **[filter](https://api.basiq.io/docs/collections-filters)**
        *optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://api.basiq.io/docs/collections-filters) by the following properties: *coming soon*
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a list with a data property that contains an array of connections. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an error in the event of a failure.

```json Definition
GET /users
```

```json Example Request
GET users HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json

{
  "type": "list",
  "size": 431,
  "data": [
    {
      "type": "user",
      "id": "9ac25c19",
      "email": "bertram@anton.com",
      "mobile": "",
      "createdTime": "2021-05-25T06:29:44Z",
      "links": {
        "self": "https://au-api.basiq.io/users/9ac25c19"
      }
    },
    {
      "type": "user",
      "id": "63e0025d5",
      "firstName": "Dinesh",
      "lastName": "Chugtai",
      "email": "dinesh@piperchat.io",
      "mobile": "+61555444776",
      "createdTime": "2021-01-19T01:42:30Z",
      "links": {
        "self": "https://au-api.basiq.io/users/63e0025d5"
      }
    }
  ],
  "links": {
    "self": "https://au-api.basiq.io/users"
  }
}
```
