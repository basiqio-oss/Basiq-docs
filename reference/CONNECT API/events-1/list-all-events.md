---
title: List all events
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
Use this collection to retrieve a paginated list of events. The events are returned sorted by created date descending order. Events are paginated in chunks of 500. Absence of `next` link means that there are no more pages to retrieve.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>

      </th>

      <th style={{ textAlign: "left" }}>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        **limit**
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This represents the maximum number of items that may be included in the response (maximum of 500). Note that by default 500 items are returned if this value is not specified.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **[filter](https://basiq.readme.io/v2.0/reference#events)**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        This list can be [filtered](https://basiq.readme.io/v2.0/reference#filters) by the following properties:

        * `user.id`

        Only equals (eq) and not equals (ne) operations are currently supported.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        **next**\
        *string, optional*
      </td>

      <td style={{ textAlign: "left" }}>
        Use this to retrieve the next page when a link to `next` is returned in the response.
      </td>
    </tr>
  </tbody>
</Table>

**Returns**

Returns a list with a data property that contains an array of events for the past 30 days. Each entry in the array is a separate object. If no data is returned, the resulting array will be empty. Otherwise, this call returns an [error](https://basiq.readme.io/v2.0/reference#errors) in the event of a failure.

```json Definition
GET /events
```

```json Example Request
GET  /events  HTTP/1.1
Authorization: Bearer YOUR_ACCESS_TOKEN
```

```json Example Response
HTTP/1.1 200 OK
Content-Type: application/json
{
    "type": "list",
    "count": 3,
    "data": [
        {
            "type": "event",
            "id": "40f8bb39",
            "createdDate": "2021-06-23T10:29:15Z",
            "eventType": "user.deleted",
            "userId": "86d1124d-77e4-460a-8b3e-c67d50ee177f",
            "dataRef": "https://au-api.basiq.io/users/86d1124d",
            "data": {
                "email": "test@updatemyemail.com",
                "firstName": "Joe",
                "id": "86d1124d-77e4-460a-8b3e-c67d50ee177f",
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
        },
        {
            "type": "event",
            "id": "8ef41015-cd6f-4a34-b8f3-b83e59526648",
            "createdDate": "2021-06-23T10:29:04Z",
            "eventType": "user.updated",
            "userId": "86d1124d",
            "dataRef": "https://au-api.basiq.io/users/86d1124d-77e4-460a-8b3e-c67d50ee177f",
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
                "self": "https://au-api.basiq.io/events/8ef41015"
            }
        },
        {
            "type": "event",
            "id": "10f94af8-71df-44fe-a1b0-6e74318e52d2",
            "createdDate": "2021-06-21T04:42:06Z",
            "eventType": "user.created",
            "userId": "3e554d6e",
            "dataRef": "https://au-api.basiq.io/users/3e554d6e",
            "data": {
                "email": "test@test.com",
                "firstName": "Joe",
                "id": "3e554d6e",
                "lastName": "Bloggs",
                "links": {
                    "self": "https://au-api.basiq.io/users/3e554d6e"
                },
                "mobile": "+61410777555",
                "type": "user"
            },
            "links": {
                "self": "https://au-api.basiq.io/events/10f94af8"
            }
        }
    ],
    "links": {
        "self": "https://au-api.basiq.io/events"
    }
}
```
