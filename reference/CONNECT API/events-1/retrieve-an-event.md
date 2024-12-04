---
title: Retrieve an event
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
Use this to retrieve the details of a specific event. This request will return back an event object with the latest data. 

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
        The identifier of the event to be retrieved.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns an account if a valid event ID was provided. Returns an [error](https://basiq.readme.io/v2.0/reference#errors) otherwise.

```json Definition
GET /events/{event.id}
```

```json Example Request
GET /events/40f8bb39 HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.11.1 200 OK
Content-Type:application/json

{
    "type": "event",
    "id": "40f8bb39",
    "createdDate": "2021-06-23T10:29:15Z",
    "eventType": "user.deleted",
    "userId": "86d1124d",
    "dataRef": "https://au-api.basiq.io/users/86d1124d",
    "data": {
        "email": "test@updatemyemail.com",
        "firstName": "Joe",
        "id": "86d1124d",
        "lastName": "Bloggs",
        "links": {
            "self": "https://au-api.basiq.io/users/86d1124d"
        },
        "mobile": "+61410777555",
        "type": "user"
    },
    "links": {
        "self": "https://au-api.basiq.io/events/40f8bb39"
    }
}
```
