---
title: Events
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
The event object represents an event that has occurred via another endpoint such as create user, update account or  failed job.  This feature is in `alpha` and this first release provides support for [user](ref:users) event types: `user.created`, `user.updated`, `user.deleted`.

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
        Value is "event".
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `id`
      </td>

      <td style={{ textAlign: "left" }}>
        Uniquely identifies the event.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `createdDate`
      </td>

      <td style={{ textAlign: "left" }}>
        Timestamp of event creation, UTC, RFC 3339 format e.g. "2021-06-23T10:29:15Z",
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `eventType`
      </td>

      <td style={{ textAlign: "left" }}>
        Identifies enum relating to the event type e.g `user.deleted`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `userId`
      </td>

      <td style={{ textAlign: "left" }}>
        The id of the [user](ref:users) resource the event is created for.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `dataRef`
      </td>

      <td style={{ textAlign: "left" }}>
        A URI reference to the data relating to the event e.g. link to the [account object](ref:retrieve-an-account)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `data`
      </td>

      <td style={{ textAlign: "left" }}>
        The payload that relates to the event. Note that all event types should include the same object type schema as defined in the API e.g. if an event of type user.created occurs, then the [user](ref:users)  schema is included within the event.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `links`
      </td>

      <td style={{ textAlign: "left" }}>
        A links object contains:

        * `self` link to the requested event
      </td>
    </tr>
  </tbody>
</Table>

```json Example Event Object
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
